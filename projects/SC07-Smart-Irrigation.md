# SC07: Smart Irrigation

**Difficulty:** ⭐⭐⭐⭐  
**Core techniques:** Fuzzy Logic + ANN  
**Team:** 3–4 students

## What

Deliver crop-sensitive irrigation recommendations under uncertain weather and soil conditions.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **soil moisture, humidity, temperature, rainfall and crop stage** into **water requirement and irrigation duration**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

ANN predicts water requirement/soil condition; fuzzy system produces explainable irrigation decision; compare ANN-only and fuzzy-only.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → Fuzzy Logic + ANN pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Use a cited 10,000+ agricultural/weather dataset or documented simulation. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

one core ANN or fuzzy MVP, baseline and result plots. Documentation-only work does not satisfy M1.

### M1 acceptance criteria

M1: prepare 10,000+ crop/weather records; implement ANN or fuzzy MVP plus fixed moisture baseline; demonstrate water recommendation and prediction/decision plots.

## Milestone 2: Advanced Product V2

integrated hybrid model, tuning, comparison and dashboard.

### M2 acceptance criteria

M2: integrate ANN prediction with fuzzy irrigation decision; compare threshold, ANN-only, fuzzy-only, and hybrid behaviour; test rain/noise/dry-soil cases; report water saved and prediction error.

## Baseline and evaluation

**Baseline:** fixed moisture threshold.  
Report **MAE/RMSE, water saved, decision quality**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

forecast API, zone control.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
