"""Admin data structure calls. Use ``nada.indicators.data_structures``."""

from pathlib import Path

from ..http import NadaError, download, drop_none, get_json, load_document, post_files, post_json, seg


class _Components(object):
    def list(self, structure_id, **params):
        """GET admin/data_structures/components/{id_or_idno}."""
        return get_json("admin/data_structures/components/{}".format(seg(structure_id)), params)

    def add(self, structure_id, component):
        """POST a component. component is a field dict."""
        return post_json(
            "admin/data_structures/components/{}".format(seg(structure_id)),
            component,
        )

    def update(self, component_id, component):
        """POST admin/data_structures/components_update/{component_id}."""
        return post_json(
            "admin/data_structures/components_update/{}".format(seg(component_id)),
            component,
        )

    def delete(self, component_id):
        """POST admin/data_structures/components_delete/{component_id}."""
        return post_json(
            "admin/data_structures/components_delete/{}".format(seg(component_id))
        )


def _normalize_structure_import(document, overwrite, dry_run):
    """Move a root-level components array under data_structure, matching NADA import_json."""
    document = dict(document)
    if "data_structure" in document and isinstance(document["data_structure"], dict):
        body = document
        structure = dict(body["data_structure"])
    else:
        structure = dict(document)
        body = {"data_structure": structure}
    components = None
    if "components" in body and "components" not in structure:
        components = body.get("components")
    if components is not None:
        structure["components"] = components
    body = {"data_structure": structure}
    if "components" not in structure:
        raise NadaError("Data structure import requires a components array")
    body["overwrite"] = bool(overwrite)
    body["dry_run"] = bool(dry_run)
    return body


class _DataStructures(object):
    def __init__(self):
        self.components = _Components()

    def list(self, page=None, per_page=None, search=None, status=None, flat=None, **params):
        """GET admin/data_structures."""
        query = drop_none({
            "page": page,
            "per_page": per_page,
            "search": search,
            "status": status,
            "flat": flat,
        })
        query.update(drop_none(params))
        return get_json("admin/data_structures", query)

    def get(self, structure_id, with_components=None):
        """GET admin/data_structures/{id_or_idno}."""
        params = None
        if with_components is not None:
            params = {"with_components": "1" if with_components else "0"}
        return get_json("admin/data_structures/{}".format(seg(structure_id)), params)

    def get_by_identity(self, name, agency, version=None, with_components=None):
        """GET admin/data_structures/by_identity."""
        params = drop_none({
            "name": name,
            "agency": agency,
            "version": version,
        })
        if with_components is not None:
            params["with_components"] = "1" if with_components else "0"
        return get_json("admin/data_structures/by_identity", params)

    def versions(self, structure_id, **params):
        """GET admin/data_structures/versions/{id_or_idno}."""
        return get_json("admin/data_structures/versions/{}".format(seg(structure_id)), params)

    def projects(self, structure_id, **params):
        """GET admin/data_structures/projects/{id_or_idno}."""
        return get_json("admin/data_structures/projects/{}".format(seg(structure_id)), params)

    def create(self, data_structure, overwrite=False):
        """POST admin/data_structures/create."""
        body = dict(load_document(data_structure))
        body["overwrite"] = bool(overwrite)
        return post_json("admin/data_structures/create", body)

    def update(self, structure_id, data_structure):
        """POST admin/data_structures/update/{id_or_idno}."""
        return post_json(
            "admin/data_structures/update/{}".format(seg(structure_id)),
            load_document(data_structure),
        )

    def set_status(self, structure_id, status):
        """POST admin/data_structures/status/{id_or_idno}."""
        return post_json(
            "admin/data_structures/status/{}".format(seg(structure_id)),
            {"status": status},
        )

    def delete(self, structure_id):
        """POST admin/data_structures/delete/{id_or_idno}."""
        return post_json("admin/data_structures/delete/{}".format(seg(structure_id)))

    def delete_many(self, ids):
        """POST admin/data_structures/batch_delete."""
        return post_json("admin/data_structures/batch_delete", {"ids": [*ids]})

    def import_json(self, document, overwrite=False, dry_run=False):
        """POST admin/data_structures/import_json.

        document is a dict or a JSON path. Components may sit on the document
        root or inside data_structure.
        """
        body = _normalize_structure_import(load_document(document), overwrite, dry_run)
        return post_json("admin/data_structures/import_json", body)

    def import_sdmx(self, file, overwrite_codelists=False, dsd_id=None):
        """POST admin/data_structures/import with an SDMX XML file."""
        path = Path(file)
        if not path.is_file():
            raise NadaError("SDMX file not found: {}".format(file))
        fields = {}
        if overwrite_codelists:
            fields["overwrite_codelists"] = "1"
        if dsd_id:
            fields["dsd_id"] = dsd_id
        with path.open("rb") as handle:
            return post_files(
                "admin/data_structures/import",
                fields,
                {"file": (path.name, handle, "application/xml")},
            )

    def export(self, structure_id, output_path=None):
        """GET admin/data_structures/export/{id_or_idno}."""
        endpoint = "admin/data_structures/export/{}".format(seg(structure_id))
        if output_path:
            return download(endpoint, output_path=output_path)
        return get_json(endpoint)

    def validate(self, data_structure=None, data_structure_id=None):
        """POST admin/data_structures/validate."""
        if data_structure_id is not None:
            body = {"data_structure_id": data_structure_id}
        else:
            body = load_document(data_structure)
            if "data_structure" not in body:
                body = {"data_structure": body}
        return post_json("admin/data_structures/validate", body)

    def indexes(self, dsd_id, include_unique_key_hash=None):
        """POST admin/timeseries/data-structures/{dsd_id}/indexes."""
        body = None
        if include_unique_key_hash is not None:
            body = {"include_unique_key_hash": bool(include_unique_key_hash)}
        return post_json("admin/timeseries/data-structures/{}/indexes".format(seg(dsd_id)), body)

    def rehash(self, dsd_id, sid=None, limit=None):
        """POST admin/timeseries/data-structures/{dsd_id}/rehash."""
        body = drop_none({"sid": sid, "limit": limit})
        return post_json(
            "admin/timeseries/data-structures/{}/rehash".format(seg(dsd_id)),
            body or None,
        )

    def duplicates(self, dsd_id, **params):
        """GET admin/timeseries/data-structures/{dsd_id}/duplicates."""
        return get_json("admin/timeseries/data-structures/{}/duplicates".format(seg(dsd_id)), params)

    def stats(self, dsd_id):
        """GET admin/timeseries/data-structures/{dsd_id}/stats."""
        return get_json("admin/timeseries/data-structures/{}/stats".format(seg(dsd_id)))


_api = _DataStructures()
list = _api.list
get = _api.get
get_by_identity = _api.get_by_identity
versions = _api.versions
projects = _api.projects
create = _api.create
update = _api.update
set_status = _api.set_status
delete = _api.delete
delete_many = _api.delete_many
import_json = _api.import_json
import_sdmx = _api.import_sdmx
export = _api.export
validate = _api.validate
components = _api.components
indexes = _api.indexes
rehash = _api.rehash
duplicates = _api.duplicates
stats = _api.stats
