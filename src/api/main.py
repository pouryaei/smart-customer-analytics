from typing import Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic import Field
from src.services.predict import predict_customer
from src.utils.logger import logger


app = FastAPI(title="Axiomeet Customer Analytics API", version="1.1")


class CustomerInput(BaseModel):
    tenure: Annotated[
        int,
        Field(
            ge=0,
            le=72
        )
    ]

    MonthlyCharges: Annotated[
        float,
        Field(
            ge=0
        )
    ]

    TotalCharges: Annotated[
        float,
        Field(
            ge=0
        )
    ]

    InternetService_Fiber_optic: Annotated[
        int,
        Field(
            ge=0,
            le=1
        )
    ] = 0

    Contract_Two_year: Annotated[
        int,
        Field(
            ge=0,
            le=1
        )
    ] = 0


class PredictionResponse(BaseModel):

    prediction: int

    probability: float

    explanation: list


@app.get("/api/v1")
def home():

    return {"status": "healthy"}


@app.get("/api/v1/health")
def health():

    return {
        "api": "ok",
        "model": "loaded"
    }


@app.post(
    "/api/v1/predict",
    response_model=PredictionResponse
)
def predict(
    customer: CustomerInput
):

    try:

        payload = (
            customer
            .model_dump()
        )

        payload[
            "InternetService_Fiber optic"
        ] = payload.pop(
            "InternetService_Fiber_optic"
        )

        payload[
            "Contract_Two year"
        ] = payload.pop(
            "Contract_Two_year"
        )

        result = (
            predict_customer(
                payload
            )
        )

        logger.info(
            f"prediction={result['prediction']}"
        )

        return result

    except Exception as e:

        logger.error(
            str(e)
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Prediction failed"
            )
        )