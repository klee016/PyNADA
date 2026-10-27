"""Query-string builders for indicator observation reads."""


def observation_params(
        time_from=None,
        time_to=None,
        limit=None,
        offset=None,
        sort=None,
        sort_by=None,
        dimensions=None,
        components=None,
        params=None,
):
    """Build the query string NADA expects for indicator observations.

    time_from and time_to map to the ``from`` and ``to`` query parameters.
    dimensions become ``d[role]`` and components become ``c[COLUMN]``.
    Values may be a string or a sequence of codes.
    """
    query = {}
    if time_from is not None:
        query["from"] = time_from
    if time_to is not None:
        query["to"] = time_to
    if limit is not None:
        query["limit"] = limit
    if offset is not None:
        query["offset"] = offset
    if sort is not None:
        query["sort"] = sort
    if sort_by is not None:
        query["sort_by"] = sort_by
    _encode_filters(query, "d", dimensions)
    _encode_filters(query, "c", components)
    if params:
        for key, value in params.items():
            if value is not None:
                query[key] = value
    return query


def _encode_filters(query, prefix, filters):
    if not filters:
        return
    for key, value in filters.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            value = ",".join(str(item) for item in value)
        query["{}[{}]".format(prefix, key)] = value
