"""Admin codelist calls. Use ``nada.indicators.codelists``."""

from ..http import delete_json, drop_none, get_json, load_document, post_json, put_json, seg


class _ItemTranslations(object):
    def list(self, item_id):
        """GET admin/codelists/items/{item_id}/translations."""
        return get_json("admin/codelists/items/{}/translations".format(seg(item_id)))

    def add(self, item_id, lang, title):
        """POST a language label for one codelist item."""
        return post_json(
            "admin/codelists/items/{}/translations".format(seg(item_id)),
            {"lang": lang, "title": title},
        )

    def delete(self, item_id, lang):
        """DELETE admin/codelists/items/{item_id}/translations/{lang}."""
        return delete_json(
            "admin/codelists/items/{}/translations/{}".format(seg(item_id), seg(lang))
        )


class _Items(object):
    def __init__(self):
        self.translations = _ItemTranslations()

    def list(self, codelist_id, **params):
        """GET items for one codelist."""
        return get_json("admin/codelists/item/{}/items".format(seg(codelist_id)), params)

    def get(self, item_id):
        """GET admin/codelists/items/{item_id}."""
        return get_json("admin/codelists/items/{}".format(seg(item_id)))

    def add(self, codelist_id, code, title=None, parent_id=None, sort_order=None, **fields):
        """POST a code onto a codelist."""
        body = drop_none({
            "code": code,
            "title": title,
            "parent_id": parent_id,
            "sort_order": sort_order,
        })
        body.update(fields)
        return post_json("admin/codelists/item/{}/items".format(seg(codelist_id)), body)

    def update(self, item_id, **fields):
        """PUT admin/codelists/items/{item_id}."""
        return put_json("admin/codelists/items/{}".format(seg(item_id)), fields)

    def delete(self, item_id):
        """DELETE admin/codelists/items/{item_id}."""
        return delete_json("admin/codelists/items/{}".format(seg(item_id)))


class _GroupTranslations(object):
    def list(self, group_id):
        return get_json("admin/codelists/groups/{}/translations".format(seg(group_id)))

    def add(self, group_id, lang, title):
        return post_json(
            "admin/codelists/groups/{}/translations".format(seg(group_id)),
            {"lang": lang, "title": title},
        )

    def delete(self, group_id, lang):
        return delete_json(
            "admin/codelists/groups/{}/translations/{}".format(seg(group_id), seg(lang))
        )


class _Groups(object):
    def __init__(self):
        self.translations = _GroupTranslations()

    def list(self, codelist_id):
        return get_json("admin/codelists/item/{}/groups".format(seg(codelist_id)))

    def get(self, group_id):
        return get_json("admin/codelists/groups/{}".format(seg(group_id)))

    def add(self, codelist_id, name, sort_order=None, **fields):
        body = drop_none({"name": name, "sort_order": sort_order})
        body.update(fields)
        return post_json("admin/codelists/item/{}/groups".format(seg(codelist_id)), body)

    def update(self, group_id, **fields):
        return put_json("admin/codelists/groups/{}".format(seg(group_id)), fields)

    def delete(self, group_id):
        return delete_json("admin/codelists/groups/{}".format(seg(group_id)))

    def add_items(self, group_id, codelist_item_id, sort_order=None):
        """Add one codelist item to a group."""
        body = {"codelist_item_id": codelist_item_id}
        if sort_order is not None:
            body["sort_order"] = sort_order
        return post_json("admin/codelists/groups/{}/items".format(seg(group_id)), body)

    def remove_item(self, group_id, item_id):
        return delete_json(
            "admin/codelists/groups/{}/items/{}".format(seg(group_id), seg(item_id))
        )


class _Codelists(object):
    def __init__(self):
        self.items = _Items()
        self.groups = _Groups()

    def list(self, page=None, per_page=None, search=None, status=None, flat=None, with_counts=None, **params):
        """GET admin/codelists."""
        query = drop_none({
            "page": page,
            "per_page": per_page,
            "search": search,
            "status": status,
            "flat": flat,
            "with_counts": with_counts,
        })
        query.update(drop_none(params))
        return get_json("admin/codelists", query)

    def get(self, codelist_id):
        """GET admin/codelists/item/{id}."""
        return get_json("admin/codelists/item/{}".format(seg(codelist_id)))

    def get_by_idno(self, idno):
        """GET admin/codelists/by_idno/{idno}."""
        return get_json("admin/codelists/by_idno/{}".format(seg(idno)))

    def get_by_name(self, name, agency=None, version=None):
        """GET admin/codelists/by_name/{name}."""
        return get_json(
            "admin/codelists/by_name/{}".format(seg(name)),
            drop_none({"agency": agency, "version": version}),
        )

    def versions(self, name, agency=None):
        """GET admin/codelists/versions/{name}."""
        return get_json(
            "admin/codelists/versions/{}".format(seg(name)),
            drop_none({"agency": agency}),
        )

    def create(self, name, description=None, **fields):
        """POST admin/codelists."""
        body = drop_none({"name": name, "description": description})
        body.update(fields)
        return post_json("admin/codelists", body)

    def update(self, codelist_id, **fields):
        """PUT admin/codelists/item/{id}."""
        return put_json("admin/codelists/item/{}".format(seg(codelist_id)), fields)

    def delete(self, codelist_id):
        """DELETE admin/codelists/item/{id}."""
        return delete_json("admin/codelists/item/{}".format(seg(codelist_id)))

    def restore(self, codelist_id):
        """POST admin/codelists/item/{id}/restore."""
        return post_json("admin/codelists/item/{}/restore".format(seg(codelist_id)))

    def delete_many(self, ids):
        """POST admin/codelists/batch_delete."""
        return post_json("admin/codelists/batch_delete", {"ids": [*ids]})

    def import_json(self, codelist, overwrite=False, dry_run=False):
        """POST admin/codelists/import_json.

        codelist is a dict or a path to a JSON file. A document that already
        wraps the codelist under a ``codelist`` key is sent as-is.
        """
        document = load_document(codelist)
        if "codelist" in document and isinstance(document["codelist"], dict):
            body = dict(document)
        else:
            body = {"codelist": document}
        body["overwrite"] = bool(overwrite)
        body["dry_run"] = bool(dry_run)
        return post_json("admin/codelists/import_json", body)


_api = _Codelists()
list = _api.list
get = _api.get
get_by_idno = _api.get_by_idno
get_by_name = _api.get_by_name
versions = _api.versions
create = _api.create
update = _api.update
delete = _api.delete
restore = _api.restore
delete_many = _api.delete_many
import_json = _api.import_json
items = _api.items
groups = _api.groups
