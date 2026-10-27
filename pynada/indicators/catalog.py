"""Published catalog reads. Use ``nada.indicators.catalog``."""

from ..http import download, drop_none, get_json, seg
from .filters import observation_params


def _data_path(idno, suffix=None):
    path = "timeseries/data/{}".format(seg(idno))
    if suffix:
        path = path + "/" + suffix
    return path


def query(idno, time_from=None, time_to=None, limit=None, offset=None, sort=None,
          sort_by=None, dimensions=None, components=None, params=None):
    """GET timeseries/data/{idno}."""
    return get_json(_data_path(idno), observation_params(
        time_from, time_to, limit, offset, sort, sort_by, dimensions, components, params
    ))


def count(idno, time_from=None, time_to=None, dimensions=None, components=None, params=None):
    """GET timeseries/data/{idno}/count."""
    return get_json(_data_path(idno, "count"), observation_params(
        time_from, time_to, dimensions=dimensions, components=components, params=params
    ))


def chart(idno, time_from=None, time_to=None, limit=None, dimensions=None, components=None, params=None):
    """GET timeseries/data/{idno}/chart."""
    return get_json(_data_path(idno, "chart"), observation_params(
        time_from, time_to, limit=limit, dimensions=dimensions, components=components, params=params
    ))


def filter_options(idno, **params):
    """GET timeseries/data/{idno}/filter-options."""
    return get_json(_data_path(idno, "filter-options"), params)


def schema(idno):
    """GET timeseries/data/{idno}/schema."""
    return get_json(_data_path(idno, "schema"))


def notes(idno, **params):
    """GET timeseries/data/{idno}/notes."""
    return get_json(_data_path(idno, "notes"), params)


def export(idno, output_path=None, time_from=None, time_to=None, limit=None, offset=None,
           sort=None, sort_by=None, dimensions=None, components=None, params=None):
    """GET timeseries/data/{idno}/export."""
    return download(_data_path(idno, "export"), observation_params(
        time_from, time_to, limit, offset, sort, sort_by, dimensions, components, params
    ), output_path)


def export_xml(idno, output_path=None, **params):
    """GET timeseries/data/{idno}/export-xml."""
    return download(_data_path(idno, "export-xml"), params, output_path)


def export_table(idno, output_path=None, **params):
    """GET timeseries/data/{idno}/table-export."""
    return download(_data_path(idno, "table-export"), params, output_path)


class _CatalogStructures(object):
    def get(self, structure_id, with_components=None):
        """GET timeseries/data-structures/item/{id}."""
        params = None
        if with_components is not None:
            params = {"with_components": "1" if with_components else "0"}
        return get_json("timeseries/data-structures/item/{}".format(seg(structure_id)), params)

    def get_by_idno(self, idno, with_components=None):
        """GET timeseries/data-structures/by_idno/{idno}."""
        params = None
        if with_components is not None:
            params = {"with_components": "1" if with_components else "0"}
        return get_json("timeseries/data-structures/by_idno/{}".format(seg(idno)), params)

    def get_by_identity(self, name, agency=None, version=None, with_components=None):
        """GET timeseries/data-structures/by_identity/{name}."""
        params = drop_none({"agency": agency, "version": version})
        if with_components is not None:
            params["with_components"] = "1" if with_components else "0"
        return get_json("timeseries/data-structures/by_identity/{}".format(seg(name)), params)

    def versions(self, name, agency=None):
        """GET timeseries/data-structures/versions/{name}."""
        return get_json(
            "timeseries/data-structures/versions/{}".format(seg(name)),
            drop_none({"agency": agency}),
        )


class _CatalogCodelists(object):
    def get(self, codelist_id):
        """GET timeseries/codelists/item/{id}."""
        return get_json("timeseries/codelists/item/{}".format(seg(codelist_id)))

    def get_by_idno(self, idno):
        """GET timeseries/codelists/by_idno/{idno}."""
        return get_json("timeseries/codelists/by_idno/{}".format(seg(idno)))

    def get_by_name(self, name, agency=None, version=None):
        """GET timeseries/codelists/by_name/{name}."""
        return get_json(
            "timeseries/codelists/by_name/{}".format(seg(name)),
            drop_none({"agency": agency, "version": version}),
        )

    def items(self, codelist_id, **params):
        """GET timeseries/codelists/item/{id}/items."""
        return get_json("timeseries/codelists/item/{}/items".format(seg(codelist_id)), params)


data_structures = _CatalogStructures()
codelists = _CatalogCodelists()
