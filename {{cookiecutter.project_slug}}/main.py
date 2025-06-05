from typing import Union

from fastapi import FastAPI

app = FastAPI()


{% if cookiecutter.app_type == "async" %}
@app.get("/")
async def root():
    return {"message": "Hello from async"}

{% else %}
@app.get("/")
def root():
    return {"message": "Hello from sync"}
{% endif %}