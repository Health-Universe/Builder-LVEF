from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="LVEF Class Predictor API",
    description="Predicts Left Ventricular Ejection Fraction (LVEF) class from Medicare claims-based variables.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LVEFPredictionOutput(BaseModel):
    lvef_class: str
    probability: float

@app.post("/predict", response_model=LVEFPredictionOutput)
def predict_lvef_class(
    age: Annotated[int, Form(...)],
    sex: Annotated[int, Form(...)],
    icd_systolic: Annotated[int, Form(...)],
    icd_diastolic: Annotated[int, Form(...)],
    icd_unspecified: Annotated[int, Form(...)],
    hf_hospitalizations: Annotated[int, Form(...)],
    device_icd: Annotated[int, Form(...)],
    crt: Annotated[int, Form(...)],
    acei: Annotated[int, Form(...)],
    arb: Annotated[int, Form(...)],
    beta_blocker: Annotated[int, Form(...)],
    loop_diuretic: Annotated[int, Form(...)],
    comorbid_mi: Annotated[int, Form(...)],
    comorbid_valve: Annotated[int, Form(...)],
):
    # Example logistic model coefficients (placeholders)
    import math
    coeffs = {
        "intercept": -1.2,
        "age": 0.02,
        "sex": -0.3,
        "icd_systolic": 1.5,
        "icd_diastolic": -1.2,
        "icd_unspecified": -0.6,
        "hf_hospitalizations": 0.4,
        "device_icd": 0.8,
        "crt": 0.6,
        "acei": 0.5,
        "arb": 0.3,
        "beta_blocker": 0.7,
        "loop_diuretic": 0.4,
        "comorbid_mi": 0.9,
        "comorbid_valve": 0.6
    }
    
    logit = coeffs["intercept"] + age * coeffs["age"] + sex * coeffs["sex"] + \
            icd_systolic * coeffs["icd_systolic"] + icd_diastolic * coeffs["icd_diastolic"] + \
            icd_unspecified * coeffs["icd_unspecified"] + hf_hospitalizations * coeffs["hf_hospitalizations"] + \
            device_icd * coeffs["device_icd"] + crt * coeffs["crt"] + acei * coeffs["acei"] + \
            arb * coeffs["arb"] + beta_blocker * coeffs["beta_blocker"] + \
            loop_diuretic * coeffs["loop_diuretic"] + comorbid_mi * coeffs["comorbid_mi"] + \
            comorbid_valve * coeffs["comorbid_valve"]

    prob = 1 / (1 + math.exp(-logit))
    lvef_class = "Reduced EF (<45%)" if prob > 0.5 else "Preserved EF (>=45%)"

    return LVEFPredictionOutput(lvef_class=lvef_class, probability=round(prob, 2))
