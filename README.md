# condAPI

`condAPI` is a FastAPI-based application designed to manage and validate JSON schemas. It provides endpoints to set, retrieve, and compare JSON schemas.

## Endpoints

### `GET /`
- **Description**: API root. Shows available endpoints and their usage.
- **Response**:
  ```json
  {
    "routes": [
      {
        "path": "/",
        "method": "GET",
        "description": "API root. Shows available endpoints and their usage."
      },
      {
        "path": "/details",
        "method": "GET",
        "description": "Returns the current schema details. No parameters required."
      },
      {
        "path": "/compare",
        "method": "POST",
        "description": "Compares a provided JSON schema with the current schema. Requires JSON body."
      },
      {
        "path": "/set_schema",
        "method": "POST",
        "description": "Sets a new schema from provided JSON. Requires JSON body."
      }
    ]
  }
  ```

### `GET /details`
- **Description**: Returns the current schema details.
- **Response**:
  - If no schema is set:
    ```json
    {
      "message": "No schema has been set yet."
    }
    ```
  - If a schema is set:
    ```json
    {
      "schema": { ...schema details... }
    }
    ```

### `POST /compare`
- **Description**: Compares a provided JSON schema with the current schema.
- **Request Body**: JSON schema to compare.
- **Response**:
  - If no schema is set:
    ```json
    {
      "detail": "No schema has been set yet. Please set a schema first."
    }
    ```
  - If the provided JSON is invalid:
    ```json
    {
      "detail": "Invalid JSON"
    }
    ```
  - If the schema comparison fails:
    ```json
    {
      "detail": "...error details..."
    }
    ```
  - If the schema comparison succeeds:
    ```json
    {
      "message": "Example JSON received and validated successfully"
    }
    ```

### `POST /set_schema`
- **Description**: Sets a new schema from the provided JSON.
- **Request Body**: JSON schema to set.
- **Response**:
  - If the provided JSON is invalid:
    ```json
    {
      "detail": "Invalid JSON"
    }
    ```
  - If the schema validation fails:
    ```json
    {
      "detail": "...error details..."
    }
    ```
  - If the schema is successfully set:
    ```json
    {
      "message": "Example JSON received and validated successfully",
      "generated_schema": { ...schema details... }
    }
    ```

## How to Run

1. Install the package. It will automatically install its required dependencies:
    ```bash
    pip install condAPI
    ```

2. Start the server:
    ```bash
    condapi start
    ```

3. To start the server on a different port (default is 8000), use the `--port` parameter:
    ```bash
    condapi start --port <port_number>
    ```


## License

This project is licensed under the MIT License.
