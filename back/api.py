from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your tax form."}

forms = [{
        "name": "deloitte",
        "revenue": "10",
        "costs": "5"
    }]


@app.get("/form", tags=["forms"])
async def get_forms() -> dict:
    return {"data": forms}


@app.post("/form", tags=["forms"])
async def add_form(form: dict) -> dict:
    forms.append(form)
    return {
        "data": {"Form added."}
    }


@app.put("/form}", tags=["forms"])
async def update_form(name, form: dict) -> dict:
    """
    for form in forms:
        if form["name"] == name:
            form["item"] = body["item"]
            return {
                "data": f"Form with name {name} has been updated."
            }

    return {
        "data": f"Form with id {name} not found."
    }
    """
    return {
        "data": f"Form with name {name} not found."
    }


@app.delete("/form}", tags=["forms"])
async def delete_form(name, form: dict) -> dict:
    """
    for form in forms:
        if int(form["name"]) == name:
            todos.remove(form)
            return {
                "data": f"Form with name {name} has been removed."
            }
    """
    return {
        "data": f"Form with name {name} not found."
    }

