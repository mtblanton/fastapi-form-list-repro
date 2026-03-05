# FastAPI Form Request issue repro 
This repo reproduces an issue in FastAPI where having a union as the type for a `Form` parameter can cause validation to be incorrect if there's only a single entry in the list.

## Running 
Run `uv sync` then run `fastapi dev main.py`

## Example requests

* Fails validation with single entry in list
```sh
curl --request POST \
  --url http://localhost:8000/test-union \
  --header 'content-type: multipart/form-data' \
  --form type=list \
  --form list=foo
```


```json
{
  "detail": [
    {
      "type": "list_type",
      "loc": [
        "body",
        "list",
        "list"
      ],
      "msg": "Input should be a valid list",
      "input": "foo"
    }
  ]
}
```

* Passes validation with multiple entries in list
```sh
curl --request POST \
  --url http://localhost:8000/test-union \
  --header 'content-type: multipart/form-data' \
  --form type=list \
  --form list=foo \
  --form list=foo2
```

```json
{
  "type": "list",
  "list": [
    "foo",
    "foo2"
  ]
}
```

* Passes validation when hitting an endpoint that doesn't use a union
```sh
curl --request POST \
  --url http://localhost:8000/test-no-union \
  --header 'content-type: multipart/form-data' \
  --form type=list \
  --form list=foo
```

```json
{
  "type": "list",
  "list": [
    "foo"
  ]
}
```