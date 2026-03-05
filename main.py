from typing import Annotated, Literal

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class InputWithList(BaseModel):
    type: Literal["list"] = "list"
    list: list[str]


class InputWithoutList(BaseModel):
    type: Literal["no-list"] = "no-list"
    single: str


@app.post("/test-union")
def test_form_list_with_union(
    request: Annotated[InputWithList | InputWithoutList, Form(discriminator="type")],
):
    return request


@app.post("/test-no-union")
def test_form_list_without_union(
    request: Annotated[InputWithList, Form(discriminator="type")],
):
    return request
