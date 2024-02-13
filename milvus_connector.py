import logging

from bytewax.outputs import DynamicSink, StatelessSinkPartition

from itertools import chain

from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class _MilvusSink(StatelessSinkPartition):
    def __init__(self, collection, collection_name):
        self.collection = collection
        self._collection_name = collection_name

    def write_batch(self, documents):
        logger.info(f"Start inserting")
        self.collection.insert(list(chain.from_iterable(documents)))
        self.collection.flush()
        logger.info(f"Number of entities in Milvus: {self.collection.num_entities}")
        index = {
           "index_type": "IVF_FLAT",
           "metric_type": "L2",
           "params": {"nlist": 128},
        }
        logger.info("Start Creating index IVF_FLAT")
        self.collection.create_index("doc_embedding", index)

    def close(self) -> None:
        self.collection.release()
        self.collection.drop_index()
        self.collection.drop()
        return super().close()


            
class MilvusOutput(DynamicSink):
    def __init__(self, collection_name, schema, host="localhost", port="19530"):
        self.collection_name = collection_name
        connections.connect("default", host=host, port=port)
        logger.info(f"List connections: {connections.list_connections()}")

        if utility.has_collection(collection_name):
            collection = Collection(collection_name)
            collection.drop()
            logger.info(f"Drop collection: {collection_name}")

        self.collection = Collection(collection_name, schema)

    def build(self, worker_index, worker_count):
        return _MilvusSink(self.collection, self.collection_name)