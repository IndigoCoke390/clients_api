from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()


class UpdateClientsPayload(BaseModel):
    password_entr: str
    new_value: int



# Open the config.json file
with open("config.json", "r") as f:
    # Load the JSON data from the file
    data = json.load(f)



def read_clients_from_file():
    with open("clients.txt", "r") as f:
        return int(f.read())

def write_clients_to_file(clients):
    with open("clients.txt", "w") as f:
        f.write(str(clients))

password = data["password"]

@app.post("/clients/update")
def update_clients(payload: UpdateClientsPayload):
    if payload.password_entr != password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    write_clients_to_file(payload.new_value)
    return {"status": "success, the value of your clients has been updated", "new_value": payload.new_value}

    


@app.get("/clients/view")
def view_clients():
    clients = read_clients_from_file()
    return {"clients": clients}