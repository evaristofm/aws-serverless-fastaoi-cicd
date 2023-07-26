from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from mangum import Mangum

from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


app.include_router(api_router, prefix="/api/v1")
# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)
