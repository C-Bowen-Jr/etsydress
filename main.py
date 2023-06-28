import json
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Address(BaseModel):
    name: str
    street: str
    city: str
    state: str
    zipcode: str
    country: str

app = FastAPI()

@app.get("/")
def read_root():
    #products = open("sample.json").read()
    return json.loads(open("sample.json").read())

# Return the entire block of product SKU
@app.get("/first-name/")
async def get_first_name(gender: str = "any"):
    random.seed()
    data = json.loads(open("sample.json").read())

    first_name_pool = [] #data["names"]["male"] + data["names"]["female"]
    if gender == "male" or gender == "any":
        first_name_pool += data["names"]["male"]
    if gender == "female" or gender == "any":
        first_name_pool += data["names"]["female"]
    return random.choice(first_name_pool)

@app.get("/last-name")
async def get_last_name():
    random.seed()
    data = json.loads(open("sample.json").read())

    return random.choice(data["names"]["surname"])

@app.get("/full-name")
async def get_full_name():
    first = await get_first_name()
    last = await get_last_name()
    return first + ' ' + last

@app.get("/full-address")
async def get_address():
    name = await get_full_name()
    data = json.loads(open("sample.json").read())
    street = str(random.randint(1,999)) + ' ' + random.choice(data["street"])
    city = random.choice(data["city"])
    state = random.choice(data["state"])
    zipcode = str(random.randint(10000,99999))
    country = "United States"
    full = "{}\n{}\n{}, {} {}\n{}".format(name, street, city, state, zipcode, country)

    return {"name": name, "street": street, "city": city, "state": state, "zip": zipcode, "country": country, "full": full}

@app.get("/copy", response_class=HTMLResponse)
async def get_html_copy():
    full = await get_address()
    clipboardApproved = full["full"].replace("\n","\\n")
    html_content = """
    <html>
        <header>
            <script>
            </script>
        </header>
        <body>
            <textarea id="copy" rows=5>{0}</textarea>
            <button onClick="navigator.clipboard.writeText('{1}').then(() => alert('Address copied')).catch((error) => alert(error))">Copy to Clipboard</button>
        </body>
    </html>
    """.format(full["full"],clipboardApproved)

    return HTMLResponse(content=html_content, status_code=200)
