# SC10: Energy Scheduler

**Difficulty:** ⭐⭐⭐  
**Core techniques:** ANN + Genetic Algorithm  
**Team:** 3–4 students

## What

Lower energy cost and peak demand while honouring user appliance constraints.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **historical load, weather, tariff, appliance constraints and preferences** into **demand forecast and appliance schedule**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

ANN forecasts near-term demand; GA schedules appliances using tariff, peak and preference penalties.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → ANN + Genetic Algorithm pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Use a cited 10,000+ load dataset plus documented appliance scenarios. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

forecast MVP, baseline, error/fitness plots and schedule demo. Documentation-only work does not satisfy M1.

## Milestone 2: Advanced Product V2

integrated GA schedule, parameter study and dashboard.

## Baseline and evaluation

**Baseline:** non-optimised schedule.  
Report **MAE/RMSE, cost, peak reduction, fitness**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

battery/solar integration, demand response.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
