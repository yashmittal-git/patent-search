from fastapi import FastAPI, HTTPException, Query
from elasticsearch import Elasticsearch

app = FastAPI()

# Initialize Elasticsearch client
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/search')
async def search_documents(keyword: str = "keyword"):
    results = es.search(index='patents', body={
        'query': {
            'query_string': {
                'query': keyword
            }
        },
        'sort': [
            {
                "_score": "desc"
            }
        ]
    })

    return results