# patent-search

# Patent Search Application

This is a keyword-based search application that retrieves documents by performing a keyword search on the text content within the documents. The documents are returned in the order of relevance. The system is containerized and can be deployed using Docker Compose.

## Services

### 1. Backend
The backend service provides a FastAPI-based REST API endpoint for searching documents based on keywords. It serves as the interface between the user and the Elasticsearch database.

### 2. Load Data
The load_data service is responsible for populating the Elasticsearch database with JSON documents. It reads JSON files from a specified directory and indexes them in Elasticsearch.
We can make it more efficient by using multithreading if we suspect a large number of JSON documents.

### 3. Elasticsearch
The Elasticsearch service provides a high-performance, distributed search and analytics engine for storing and retrieving documents.


## Getting Started

Follow the steps below to get the application up and running:

### Prerequisites

- Docker and Docker Compose must be installed on your system.

### Clone the Repository

```bash
git clone https://github.com/yashmittal-git/patent-search
cd patent-search
```

### Starting the Application

Start all the services
```bash
docker-compose up
```
(Optional) If you want to use Kibana for data visualization, uncomment the Kibana service in the docker-compose.yml file

### Accessing the Application

- FastAPI is running at http://localhost:8000
- Elasticsearch is running at http://localhost:9200
- (Optional) Kibana is running at http://localhost:5601

### Using the search tool

- Open a web browser or an API Client(like Postman) or use FastAPI Swagger available at http://localhost:8000/docs#/
- Send a GET request to http://localhost:8000/search with the keyword query parameter, like this:
```bash
http://localhost:8000/search?keyword=your_keyword
```

## Scaling Strategies

### Horizontal Scaling
To horizontally scale the application, we can add more instances of the FastAPI service behind a load balancer. This can be achieved by duplicating the fastapi service in the docker-compose.yml file and configuring a load balancer like NGINX to distribute traffic among these instances.
Elasticsearch is inherently designed for horizontal scalability. We can create multiple Elasticsearch containers and configure them to form an Elasticsearch cluster for high availability and performance.

### Vertical Scaling
For vertical scaling, we can allocate more resources (CPU, memory) to each container to handle increased load by configuring in the yml file.

