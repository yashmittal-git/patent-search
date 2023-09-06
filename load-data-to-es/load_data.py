import json
import time
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


time.sleep(60)
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

index_name = "patents" 

def load_data_from_directory(directory):
    actions = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                document = json.load(file)
                action = {
                    "_op_type": "index",
                    "_index": index_name,
                    "_id": document["patent_number"],
                    "_source": document
                }
                actions.append(action)

    success, failed = bulk(es, actions)
    print(f"Successfully loaded {success} documents.")
    if failed:
        print(f"Failed to load {failed} documents.")

if __name__ == "__main__":
    json_directory = "patent_jsons"
    load_data_from_directory(json_directory)
