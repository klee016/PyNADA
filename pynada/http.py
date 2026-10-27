"""HTTP helpers for the indicator and upload APIs.

Existing catalog calls keep using commons.make_*_request. These helpers
accept HTTP 201 and send JSON with an explicit content type.
"""

import json
from pathlib import Path
from urllib.parse import quote

import requests

from . import commons


class NadaError(Exception):
    """NADA returned an error response."""

    def __init__(self, message, status_code=None, body=None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


def seg(value):
    """Encode one URL path segment."""
    return quote(str(value), safe="")


def endpoint_url(endpoint):
    base = commons.api_base_url or ""
    endpoint = str(endpoint).lstrip("/")
    if base and not base.endswith("/"):
        return base + "/" + endpoint
    return base + endpoint


def _headers(content_type=None, extra=None):
    headers = dict(commons.http_headers)
    if content_type:
        headers["Content-Type"] = content_type
    if extra:
        headers.update(extra)
    return headers


def _raise_for_status(response, method, endpoint):
    if 200 <= response.status_code < 300:
        return
    raise NadaError(
        "{} /{} {} {}".format(method, endpoint, response.status_code, response.text),
        status_code=response.status_code,
        body=response.text,
    )


def _decode_json(response, method, endpoint):
    if response.status_code == 204 or not response.content:
        return {}
    try:
        return response.json()
    except ValueError:
        raise NadaError(
            "{} /{} {} {}".format(method, endpoint, response.status_code, response.text),
            status_code=response.status_code,
            body=response.text,
        )


def request_json(method, endpoint, params=None, body=None, ok_empty=False):
    """Send a JSON request and return the decoded body."""
    data = None
    content_type = None
    if body is not None:
        data = json.dumps(body)
        content_type = "application/json"
    response = requests.request(
        method,
        endpoint_url(endpoint),
        headers=_headers(content_type),
        params=params or None,
        data=data,
    )
    _raise_for_status(response, method, endpoint)
    if ok_empty and not response.content:
        return {}
    return _decode_json(response, method, endpoint)


def get_json(endpoint, params=None):
    clean = None
    if params:
        clean = {key: value for key, value in params.items() if value is not None}
    return request_json("GET", endpoint, params=clean)


def post_json(endpoint, body=None, params=None):
    return request_json("POST", endpoint, params=params, body=body)


def put_json(endpoint, body=None):
    return request_json("PUT", endpoint, body=body)


def delete_json(endpoint):
    return request_json("DELETE", endpoint)


def post_files(endpoint, fields=None, files=None, params=None):
    """Multipart POST. fields are form values; files is a requests files dict."""
    response = requests.request(
        "POST",
        endpoint_url(endpoint),
        headers=_headers(),
        params=params or None,
        data=fields or None,
        files=files,
    )
    _raise_for_status(response, "POST", endpoint)
    return _decode_json(response, "POST", endpoint)


def download(endpoint, params=None, output_path=None):
    """GET a file. JSON error bodies raise NadaError. Returns bytes or a saved-path dict."""
    clean = None
    if params:
        clean = {key: value for key, value in params.items() if value is not None}
    response = requests.request(
        "GET",
        endpoint_url(endpoint),
        headers=_headers(),
        params=clean,
    )
    _raise_for_status(response, "GET", endpoint)
    content_type = response.headers.get("Content-Type", "")
    if "json" in content_type.lower():
        return _decode_json(response, "GET", endpoint)
    if output_path:
        path = Path(output_path)
        path.write_bytes(response.content)
        return {"path": str(path), "content_type": content_type, "size": len(response.content)}
    return {"content": response.content, "content_type": content_type, "size": len(response.content)}


def load_document(document):
    """Accept a dict or a path to a JSON file."""
    if isinstance(document, dict):
        return document
    path = Path(document)
    if not path.is_file():
        raise NadaError("Document not found: {}".format(document))
    with path.open(encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise NadaError("JSON document must be an object")
    return loaded


def drop_none(values):
    return {key: value for key, value in values.items() if value is not None}
