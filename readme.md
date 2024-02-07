# Neo4j PoC
## Running Locally

1. [Install Neo4J Desktop GUI ](https://neo4j.com/product/developer-tools/)
    * Allows you to connect to our locally running docker container
    * Has really nice tutorials for how to interact with the graph, and provides thorough examples
    * ![Neo4j GUI Screenshot](./assets/gui.png)

2. Download neo4j image
    ```bash
    docker pull neo4j
    ```

3. Run db container
    ```bash
    docker run \
        --env NEO4J_AUTH=neo4j/newPassword \
        --publish=7687:7687 \
        --volume=$HOME/neo4j/data:/data \
        neo4j
    ```

4. Initialize virtual environment
    ```bash
    python -m venv .venv
    . .venv/bin/activate
    ```

5. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

6. Run hello world example
    ```bash
    python hello_world.py
    ```
    * ![hello world output](./assets/console-output.png)

7. Seed db
    ```bash
    python models_example.py
    ```
    * ![seed output](./assets/graph-output.png)

## Notes
### Object Graph Mapper (It's OGM rather than ORM)
[Neomodel](https://neo4j.com/labs/neomodel/) is an OGM for Python and Neo4j. It allows you to define your graph database model in a Pythonic way and then access and edit your data **without needing to write Cypher queries**.

You can inspect an existing Neo4j database to generate a neomodel definition file using the inspect command:
```bash
neomodel_inspect_database -db bolt://neo4j:neo4j@localhost:7687 --write-to yourapp/models.py
```

### Django considerations
There is a Django specific Neomodel OGM plugin https://pypi.org/project/django-neomodel/
* This is in beta
    * It should be noted that AWS' Neptune doesn't have anything similar though

Model form example pulled from [docs](https://pypi.org/project/django-neomodel/):
![Model form example](./assets/django-docs.png)
