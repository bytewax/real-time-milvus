
#  Stream, Process, Embed, Repeat

## Your takeaway
In this tutorial, we will use Bytewax as the basis to create a pipeline that will retrieve new hackernews posts, parallelize the parsing and creation of embeddings to be fed into Milvus, our vector database.

## Dataflow
![dataflow](https://github.com/bytewax/real-time-milvus/blob/main/dataflow.png)

The dataflow has 5 parts:
* Input - stream stories and comments from [HackerNews API](https://github.com/HackerNews/API).
* Preprocess - retrieve updates and filter for stories/comments.
* Retrieve Content - download the html and parse it into useable text. Thanks to awesome [Unstructured.io](https://github.com/Unstructured-IO/unstructured).
* Vectorize - Create an embedding or list of embeddings for text using [Hagging Face Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).
* Output - write the vectors to [Milvus](https://github.com/milvus-io/milvus) and create a new index


## Setting up your environment
Recommended with Python 3.11.

```bash
pip install -r requirements.txt
```

## Run it

```bash
python -m bytewax.run "pipeline:run_hn_flow()"
```

### Milvus Lite
We'll use Milvus Lite in this tutorial. Milvus Lite is a lightweight version of Milvus that can be embedded into your Python application. It is a single binary that can be easily installed and run on your machine. Install with client (pymilvus):

```bash
python -m pip install "milvus[client]"
```

### Milvus CLI
[Milvus Command-Line Interface (CLI)](https://milvus.io/docs/cli_overview.md) is a command-line tool that supports database connection, data operations, and import and export of data. So you can run queries and see if the data goes through the pipeline.
Install with

```bash
pip install milvus-cli
```
