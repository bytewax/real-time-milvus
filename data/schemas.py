from pymilvus import FieldSchema, CollectionSchema, DataType

VECTOR_DIMENSIONS = 384

story_fields = [
    FieldSchema(name="key_id", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="by", dtype=DataType.VARCHAR, max_length=255, description="Author"),
    FieldSchema(name="descendants", dtype=DataType.INT64),
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="score", dtype=DataType.INT64),
    FieldSchema(name="time", dtype=DataType.INT64),
    FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=512),
    FieldSchema(name="type", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="url", dtype=DataType.VARCHAR, max_length=2048),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name="doc_embedding", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIMENSIONS)
]

# Create the collection schema
STORY_SCHEMA = CollectionSchema(fields=story_fields, description="Stories", enable_dynamic_field=True)

comment_fields = [
    FieldSchema(name="key_id", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="by", dtype=DataType.VARCHAR, max_length=255, description="Author"),
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="parent", dtype=DataType.INT64, description="Parent ID"),
    FieldSchema(name="time", dtype=DataType.INT64),
    FieldSchema(name="type", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="root_id", dtype=DataType.INT64),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name="doc_embedding", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIMENSIONS)
]

COMMENT_SCHEMA = CollectionSchema(fields=comment_fields, description="Comments", enable_dynamic_field=True)