# Etsydress API

Etsydress is an api for testing addresses formatted
as would be provided to a seller through Etsy. This
can include or exclude various filters such as
apartment addresses, international address, etc. It
composites several names and numbers to fake an
address. There are routes for finer granularity of
things it does in a more complete picture.

## Prerequisits

```pip install uvicorn```
```pip install fastapi```

## Running
```python3 -m uvicorn main:app --reload``` will start
the service with the default 127.0.0.1:8000 and set
it to hot swap with changes as they are saved
