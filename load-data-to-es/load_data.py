import json
import time
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk



def get_elasticsearch():
    es = None
    tries = 0
    while tries != 100:
        es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
        try:
            if es.ping() == True:
                print("ES Running")
                return es
        except Exception as e:
            tries += 1
            print(f"Connection to ES failed for {tries} time. Retrying in 10 seconds")
            time.sleep(10)

    return es


def load_data_from_directory(directory):

    es = get_elasticsearch()
    index_name = "patents"
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
