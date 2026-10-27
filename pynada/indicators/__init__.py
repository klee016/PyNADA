"""Indicator studies, structures, codelists, and observations.

``nada.indicators.create`` writes the catalog entry.
``nada.indicators.codelists``, ``nada.indicators.data_structures``, and
``nada.indicators.data`` manage the shared vocabulary, the data structure,
and the observations. ``nada.indicators.catalog`` reads a published series.
"""

from ..create_and_import import timeseries_study_payload
from ..http import NadaError, delete_json, get_json, post_json, seg
from . import catalog
from . import codelists as _codelists
from . import data
from . import data_structures
from . import databases

codelists = _codelists


def _study_payload(dataset_id, series_description=None, require_series=False, **fields):
    if require_series or series_description is not None:
        assert series_description is not None and dataset_id == series_description["idno"]
    return timeseries_study_payload(
        dataset_id=dataset_id,
        series_description=series_description,
        **fields
    )


def create(dataset_id, series_description, repository_id=None, access_policy=None,
           data_remote_url=None, published=None, overwrite=None, metadata_creation=None,
           metadata_information=None, data_structure_reference=None, data_notes=None,
           tags=None, provenance=None, embeddings=None, lda_topics=None, additional=None):
    """POST datasets/create/timeseries/{idno}. Returns the JSON response."""
    body = _study_payload(
        dataset_id,
        series_description,
        require_series=True,
        repository_id=repository_id,
        access_policy=access_policy,
        data_remote_url=data_remote_url,
        published=published,
        overwrite=overwrite,
        metadata_creation=metadata_creation,
        metadata_information=metadata_information,
        data_structure_reference=data_structure_reference,
        data_notes=data_notes,
        tags=tags,
        provenance=provenance,
        embeddings=embeddings,
        lda_topics=lda_topics,
        additional=additional,
    )
    return post_json("datasets/create/timeseries/" + seg(dataset_id), body)


def update(dataset_id, series_description=None, repository_id=None, access_policy=None,
           data_remote_url=None, published=None, overwrite=None, metadata_creation=None,
           metadata_information=None, data_structure_reference=None, data_notes=None,
           tags=None, provenance=None, embeddings=None, lda_topics=None, additional=None,
           merge_options=None):
    """POST datasets/update/timeseries/{idno}.

    Sections you omit stay as they are. Pass merge_options="replace" to replace
    the stored metadata with this payload.
    """
    body = _study_payload(
        dataset_id,
        series_description,
        repository_id=repository_id,
        access_policy=access_policy,
        data_remote_url=data_remote_url,
        published=published,
        overwrite=overwrite,
        metadata_creation=metadata_creation,
        metadata_information=metadata_information,
        data_structure_reference=data_structure_reference,
        data_notes=data_notes,
        tags=tags,
        provenance=provenance,
        embeddings=embeddings,
        lda_topics=lda_topics,
        additional=additional,
        merge_options=merge_options,
    )
    return post_json("datasets/update/timeseries/" + seg(dataset_id), body)


def get(dataset_id):
    """GET datasets/{idno}."""
    return get_json("datasets/" + seg(dataset_id))


def delete(dataset_id):
    """DELETE datasets/{idno}."""
    return delete_json("datasets/" + seg(dataset_id))


def _structure_idno(document):
    if document is None:
        return None
    if isinstance(document, str):
        return document
    block = document.get("data_structure")
    if not isinstance(block, dict):
        block = document
    return block.get("idno")


def _reference_idno(reference):
    if isinstance(reference, dict):
        return reference.get("idno")
    return reference


def _study_exists(dataset_id):
    try:
        get(dataset_id)
        return True
    except NadaError as exc:
        text = exc.body or str(exc)
        if exc.status_code == 404 or "IDNO-NOT-FOUND" in text or "DATASET_NOT_FOUND" in text:
            return False
        raise


def publish(dataset_id, series_description, data_structure=None, csv_path=None, codelists=None,
            repository_id=None, access_policy=None, data_remote_url=None, published=None,
            overwrite="yes", metadata_creation=None, metadata_information=None,
            data_structure_reference=None, data_notes=None, tags=None, provenance=None,
            embeddings=None, lda_topics=None, additional=None, dsd_overwrite=False,
            codelist_overwrite=False, delimiter=",", mapping=None, ensure_unique_index=None):
    """Import codelists and a data structure, write the study, attach the structure, and load a CSV.

    codelists is a list of codelist documents (dicts or JSON paths).
    data_structure is the data structure document (dict or JSON path).
    An existing study is updated. A new study is created.
    """
    results = {}
    if codelists:
        imported = []
        for document in codelists:
            imported.append(_codelists.import_json(document, overwrite=codelist_overwrite))
        results["codelists"] = imported
    if data_structure is not None:
        results["data_structure"] = data_structures.import_json(
            data_structure,
            overwrite=dsd_overwrite,
        )
    study_fields = dict(
        repository_id=repository_id,
        access_policy=access_policy,
        data_remote_url=data_remote_url,
        published=published,
        overwrite=overwrite,
        metadata_creation=metadata_creation,
        metadata_information=metadata_information,
        data_structure_reference=data_structure_reference,
        data_notes=data_notes,
        tags=tags,
        provenance=provenance,
        embeddings=embeddings,
        lda_topics=lda_topics,
        additional=additional,
    )
    if _study_exists(dataset_id):
        results["study"] = update(dataset_id, series_description, **study_fields)
    else:
        results["study"] = create(dataset_id, series_description, **study_fields)
    attach_idno = _reference_idno(data_structure_reference) or _structure_idno(data_structure)
    if attach_idno:
        results["attach"] = data.attach_structure(
            dataset_id,
            data_structure_reference=attach_idno,
        )
    if csv_path:
        results["data"] = data.import_csv(
            dataset_id,
            csv_path=csv_path,
            dsd_idno=attach_idno,
            delimiter=delimiter,
            mapping=mapping,
            ensure_unique_index=ensure_unique_index,
        )
    return results
