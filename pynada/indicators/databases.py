"""Source database entries linked from indicator metadata."""

from ..create_and_import import timeseries_database_payload
from ..http import post_json, seg


def create(published=None, overwrite=None, database_description=None, additional=None,
           metadata_information=None, provenance=None, embeddings=None, lda_topics=None, tags=None):
    """POST datasets/create/timeseriesdb. Returns the JSON response."""
    return post_json("datasets/create/timeseriesdb", timeseries_database_payload(
        published=published,
        overwrite=overwrite,
        database_description=database_description,
        additional=additional,
        metadata_information=metadata_information,
        provenance=provenance,
        embeddings=embeddings,
        lda_topics=lda_topics,
        tags=tags,
    ))


def update(dataset_id, published=None, database_description=None, additional=None,
           metadata_information=None, provenance=None, embeddings=None, lda_topics=None, tags=None):
    """POST datasets/update/timeseriesdb/{idno}. Only the sections you pass are merged."""
    return post_json(
        "datasets/update/timeseriesdb/" + seg(dataset_id),
        timeseries_database_payload(
            published=published,
            database_description=database_description,
            additional=additional,
            metadata_information=metadata_information,
            provenance=provenance,
            embeddings=embeddings,
            lda_topics=lda_topics,
            tags=tags,
        ),
    )

