# SC08: Predictive Maintenance

**Difficulty:** ⭐⭐⭐  
**Core techniques:** ANN + Fuzzy Logic  
**Team:** 3–4 students

## What

Predict equipment faults and transform uncertainty into a practical maintenance action.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **vibration, temperature, RPM, load and operating severity** into **fault likelihood and maintenance priority**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

ANN estimates failure risk; fuzzy inference combines risk and severity to assign priority.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → ANN + Fuzzy Logic pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Use a cited 10,000+ sensor dataset or documented augmentation. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

ANN/fuzzy MVP, baseline, error curve and priority demo. Documentation-only work does not satisfy M1.

## Milestone 2: Advanced Product V2

hybrid system, experiments, noise/edge analysis and dashboard.

## Baseline and evaluation

**Baseline:** crisp sensor thresholds.  
Report **F1/ROC-AUC, error, priority consistency**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

remaining useful life, streaming signals.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
