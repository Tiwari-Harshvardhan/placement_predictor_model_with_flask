# Placement Predictor Web App

A simple web application for predicting placement based on CGPA and IQ using a Logistic Regression model.

## Features

- Flask web interface for user input
- FastAPI backend for model prediction
- Model trained on placement data

## Local Setup

1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the service: `uvicorn api:app --reload --host 0.0.0.0 --port 8000`
6. Open http://localhost:8000

## Deployment

For live hosting, since GitHub Pages only supports static sites, you need to deploy to a platform that supports Python.

### Option 1: Railway (Recommended for simplicity)

1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repo
3. Deploy
4. Railway will auto-detect Python and install requirements

### Option 2: Heroku

1. Create a Heroku app
2. Push this code to a GitHub repo
3. Connect Heroku to the GitHub repo
4. Add buildpacks: `heroku/python`
5. Deploy

### Option 3: Vercel

1. Use Vercel for FastAPI deployment
2. Deploy Flask separately or combine into one app

Note: For production, you may need to adjust the API URL in app.py to the deployed FastAPI URL.

## Usage

- Enter CGPA and IQ values
- Click Predict
- See if the student will be placed or not