"""Resumable uploads used by indicator CSV import and other large files.

Call these as ``nada.uploads.upload(path)``. The returned upload id is what
``nada.indicators.data.import_csv`` accepts.
"""

import math
from pathlib import Path

from .http import NadaError, delete_json, endpoint_url, get_json, post_json, requests, seg
from .http import _decode_json, _headers, _raise_for_status
from .http import download as download_response


def limits():
    """GET uploads/limits."""
    return get_json("uploads/limits")


def list(**params):
    """GET uploads. Lists uploads owned by the API key."""
    return get_json("uploads", params)


def init(filename, total_size, total_chunks, chunk_size, metadata=None):
    """POST uploads/init. Returns the NADA payload, including upload_id."""
    body = {
        "filename": filename,
        "total_size": int(total_size),
        "total_chunks": int(total_chunks),
        "chunk_size": int(chunk_size),
    }
    if metadata is not None:
        body["metadata"] = metadata
    return post_json("uploads/init", body)


def chunk(upload_id, chunk_number, data):
    """POST one raw chunk to uploads/chunk/{upload_id}."""
    payload = data if isinstance(data, (bytes, bytearray)) else bytes(data)
    headers = _headers(
        "application/octet-stream",
        {
            "X-Upload-Chunk-Number": str(int(chunk_number)),
            "X-Upload-Chunk-Size": str(len(payload)),
        },
    )
    endpoint = "uploads/chunk/" + seg(upload_id)
    response = requests.request(
        "POST",
        endpoint_url(endpoint),
        headers=headers,
        data=payload,
    )
    _raise_for_status(response, "POST", endpoint)
    return _decode_json(response, "POST", endpoint)


def status(upload_id):
    """GET uploads/status/{upload_id}."""
    return get_json("uploads/status/" + seg(upload_id))


def download(upload_id, output_path=None):
    """GET uploads/download/{upload_id}."""
    return download_response("uploads/download/" + seg(upload_id), output_path=output_path)


def delete(upload_id):
    """DELETE uploads/{upload_id}."""
    return delete_json("uploads/" + seg(upload_id))


def cleanup():
    """POST uploads/cleanup. Removes expired incomplete uploads."""
    return post_json("uploads/cleanup")


def _max_chunk_size():
    payload = limits()
    block = payload.get("limits") if isinstance(payload, dict) else None
    if not isinstance(block, dict):
        block = payload if isinstance(payload, dict) else {}
    size = block.get("max_chunk_size")
    if not size:
        raise NadaError("NADA did not return max_chunk_size")
    return int(size)


def upload(file_path, filename=None, chunk_size=None, metadata=None):
    """Upload a local file and return its upload_id once NADA marks it completed."""
    path = Path(file_path)
    if not path.is_file():
        raise NadaError("File not found: {}".format(file_path))
    total_size = path.stat().st_size
    if total_size <= 0:
        raise NadaError("File is empty: {}".format(file_path))
    if chunk_size is None:
        chunk_size = _max_chunk_size()
    chunk_size = int(chunk_size)
    if chunk_size <= 0:
        raise NadaError("chunk_size must be greater than zero")
    total_chunks = max(1, int(math.ceil(total_size / float(chunk_size))))
    started = init(
        filename or path.name,
        total_size,
        total_chunks,
        chunk_size,
        metadata,
    )
    upload_id = started.get("upload_id")
    if not upload_id:
        raise NadaError("NADA upload init did not return upload_id")
    with path.open("rb") as handle:
        for chunk_number in range(total_chunks):
            blob = handle.read(chunk_size)
            if not blob:
                break
            chunk(upload_id, chunk_number, blob)
    finished = status(upload_id)
    state = finished.get("upload_status")
    if state not in ("completed", "complete"):
        raise NadaError("NADA upload did not complete (status: {})".format(state))
    return upload_id
