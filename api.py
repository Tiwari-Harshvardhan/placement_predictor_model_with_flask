from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    raise FileNotFoundError('model.pkl and/or scaler.pkl not found in project root')

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

class PredictionRequest(BaseModel):
    cgpa: float
    iq: int

@app.post('/predict')
def predict(request: PredictionRequest):
    try:
        input_data = np.array([[request.cgpa, request.iq]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        return {'placement': int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/')
def read_index():
    index_file = os.path.join(os.path.dirname(__file__), 'index.html')
    if not os.path.exists(index_file):
        raise HTTPException(status_code=404, detail='index.html not found')
    return FileResponse(index_file)
