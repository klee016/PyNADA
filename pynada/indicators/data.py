"""Indicator observation calls. Use ``nada.indicators.data``."""

import json

from ..http import NadaError, download, get_json, post_files, post_json, seg
from ..uploads import upload
from .filters import observation_params


def _data_path(idno, suffix=None):
    path = "admin/timeseries/data/{}".format(seg(idno))
    if suffix:
        path = path + "/" + suffix
    return path


def attach_structure(idno, data_structure_id=None, data_structure_reference=None, detach=False):
    """POST admin/timeseries/data/{idno}/attach-dsd.

    Pass a numeric data_structure_id, a catalogue idno as data_structure_reference,
    or detach=True to remove the link. Detaching deletes stored observations.
    """
    if detach:
        body = {"detach": True}
    else:
        body = {}
        if data_structure_id is not None:
            body["data_structure_id"] = data_structure_id
        if data_structure_reference is not None:
            body["data_structure_reference"] = data_structure_reference
        if not body:
            raise NadaError("Provide data_structure_id, data_structure_reference, or detach=True")
    return post_json(_data_path(idno, "attach-dsd"), body)


def query(idno, time_from=None, time_to=None, limit=None, offset=None, sort=None,
          sort_by=None, dimensions=None, components=None, params=None):
    """GET admin/timeseries/data/{idno}."""
    return get_json(_data_path(idno), observation_params(
        time_from, time_to, limit, offset, sort, sort_by, dimensions, components, params
    ))


def count(idno, time_from=None, time_to=None, dimensions=None, components=None, params=None):
    """GET admin/timeseries/data/{idno}/count."""
    return get_json(_data_path(idno, "count"), observation_params(
        time_from, time_to, dimensions=dimensions, components=components, params=params
    ))


def schema(idno):
    """GET admin/timeseries/data/{idno}/schema."""
    return get_json(_data_path(idno, "schema"))


def import_csv(idno, csv_path=None, upload_id=None, dsd_idno=None, delimiter=",",
               mapping=None, ensure_unique_index=None):
    """POST admin/timeseries/data/{idno}/import.

    Pass csv_path to resumable-upload the file first, or pass an existing upload_id.
    """
    if csv_path and upload_id:
        raise NadaError("Pass csv_path or upload_id, not both")
    if not csv_path and not upload_id:
        raise NadaError("csv_path or upload_id is required")
    if csv_path:
        upload_id = upload(csv_path)
    fields = {"idno": idno, "upload_id": upload_id}
    if dsd_idno:
        fields["dsd_idno"] = dsd_idno
    if delimiter:
        fields["delimiter"] = delimiter
    if mapping is not None:
        fields["mapping"] = mapping if isinstance(mapping, str) else json.dumps(mapping)
    if ensure_unique_index is not None:
        fields["ensure_unique_index"] = "1" if ensure_unique_index else "0"
    return post_files(_data_path(idno, "import"), fields)


def download_csv(idno, output_path=None):
    """GET admin/timeseries/data/{idno}/import-csv."""
    return download(_data_path(idno, "import-csv"), output_path=output_path)


def insert(idno, rows, ensure_unique_index=None):
    """POST a JSON batch of observations to admin/timeseries/data/{idno}."""
    body = {"data": rows}
    if ensure_unique_index is not None:
        body["ensure_unique_index"] = bool(ensure_unique_index)
    return post_json(_data_path(idno), body)


def clear(idno):
    """POST admin/timeseries/data/{idno}/clear-data. The DSD link stays in place."""
    return post_json(_data_path(idno, "clear-data"))


def rehash(idno, limit=None):
    """POST admin/timeseries/data/{idno}/rehash."""
    body = {"limit": limit} if limit is not None else None
    return post_json(_data_path(idno, "rehash"), body)


def duplicates(idno, **params):
    """GET admin/timeseries/data/{idno}/duplicates."""
    return get_json(_data_path(idno, "duplicates"), params)


def value_counts(idno, **params):
    """GET admin/timeseries/data/{idno}/value-counts-summary."""
    return get_json(_data_path(idno, "value-counts-summary"), params)


def sync_counts(idno):
    """POST admin/timeseries/data/{idno}/sync-counts."""
    return post_json(_data_path(idno, "sync-counts"))


def replace(idno, csv_path=None, upload_id=None, dsd_idno=None, delimiter=",",
            mapping=None, ensure_unique_index=None):
    """Clear observations for a study, then import a CSV."""
    cleared = clear(idno)
    imported = import_csv(
        idno,
        csv_path=csv_path,
        upload_id=upload_id,
        dsd_idno=dsd_idno,
        delimiter=delimiter,
        mapping=mapping,
        ensure_unique_index=ensure_unique_index,
    )
    return {"cleared": cleared, "imported": imported}
