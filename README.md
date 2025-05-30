# LVEF Class Predictor API

## Overview
This FastAPI application predicts Left Ventricular Ejection Fraction (LVEF) class from claims-based variables in Medicare data. The model mimics logistic regression developed in "Development and Preliminary Validation of a Medicare Claims–Based Model to Predict Left Ventricular Ejection Fraction Class in Patients With Heart Failure" (Desai et al., 2018).

## Use Cases
- Identify LVEF class in heart failure patients where echocardiographic EF is unavailable.
- Support health services research and retrospective cohort stratification.
- Aid in observational study adjustment when EF is a key confounder.

## Inputs
- Age, sex, ICD-based indicators (systolic/diastolic/unspecified HF)
- HF hospitalizations
- Device history (ICD, CRT)
- Medications (ACEi, ARB, beta-blockers, loop diuretics)
- Comorbidities (MI, valve disorders)

## Outputs
- LVEF Class: Reduced EF (<45%) or Preserved EF (≥45%)
- Probability score of classification

## Limitations
- Based on simplified logistic coefficients from the paper, not the full LASSO-derived model.
- Does not distinguish moderately reduced EF.
- Assumes accurate ICD coding and claims completeness.

## Evidence
Desai RJ, Lin KJ, Patorno E, et al. Circ Cardiovasc Qual Outcomes. 2018;11:e004700. doi:10.1161/CIRCOUTCOMES.118.004700

## Owner's Insight
This tool helps bridge the critical gap in administrative claims analysis where echocardiographic data is unavailable, enabling more granular population segmentation in heart failure research and real-world evidence.

## Running Locally
```bash
uvicorn main:app --reload
```

## Health Universe Compatibility
- Deploy in a `python:3.10-slim-bookworm` container
- API-formatted, CORS-enabled, and input-safe for Navigator integration
