from fastapi import APIRouter,Request, HTTPException
from .schema import SchemaGenerator
from fastapi.responses import JSONResponse

router = APIRouter()
schema = SchemaGenerator()


@router.get("/")
async def read_root():
    return {
        "routes": [
            {
                "path": "/",
                "method": "GET",
                "description": "API root. Shows available endpoints and their usage.",
            },
            {
                "path": "/details",
                "method": "GET",
                "description": "Returns the current schema details. No parameters required.",
            },
            {
                "path": "/compare",
                "method": "POST",
                "description": "Compares a provided JSON schema with the current schema. Requires JSON body.",
            },
            {
                "path": "/set_schema",
                "method": "POST",
                "description": "Sets a new schema from provided JSON. Requires JSON body.",
            },
        ]
    }


@router.get("/details")
async def read_details():
    schema_data = schema.get_schema()
    if not schema_data:
        return {"message": "No schema has been set yet."}
    return {"schema": schema_data}


@router.post("/compare")
async def compare_schema(request: Request):
    current_schema = schema.get_schema()
    if not current_schema:
        return JSONResponse(
            status_code=400,
            content={"detail": "No schema has been set yet. Please set a schema first."}
        )

    try:
        data = await request.json()
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"detail": "Invalid JSON"}
        )

    ok, error = schema.compare_schema(data)
    if not ok:
        return JSONResponse(
            status_code=422,
            content={"detail": error}
        )

    return {"message": "Example JSON received and validated successfully"}


@router.post("/set_schema")
async def read_input(request: Request):
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    try:
        schema.set_schema(data)
        schema_data = schema.get_schema()
        if not schema_data:
            raise ValueError("The generated schema is empty")
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

    return {
        "message": "Example JSON received and validated successfully",
        "generated_schema": schema,
    }
