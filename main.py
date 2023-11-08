from fastapi import FastAPI
import json

import db

app = FastAPI()

@app.get(f"/")
def root():
    return json.dumps(
            db.generate_product(),
            indent=4
            ) 



