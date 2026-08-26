# SC01: Climate Energy Controller

**Difficulty:** ⭐⭐⭐⭐  
**Core techniques:** Fuzzy Logic + Genetic Algorithm  
**Team:** 3–4 students

## What

Build an uncertain-condition campus climate controller that improves comfort while lowering energy use.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **temperature, humidity, occupancy, and tariff** into **cooling level, fan speed, and energy recommendation**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

Mamdani FIS → controller output; GA tunes membership/rule parameters; compare with fixed thresholds.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → Fuzzy Logic + Genetic Algorithm pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Generate at least 10,000 realistic scenarios using cited weather/occupancy/tariff ranges. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

working fuzzy controller, baseline, 10K scenarios, two plots and interactive MVP. Documentation-only work does not satisfy M1.

### M1 acceptance criteria

M1: document weather/occupancy/tariff sources; generate 10,000 scenarios; implement and plot all fuzzy membership functions and at least 12 rules; build a fixed-threshold baseline; demonstrate cooling and fan recommendations from live inputs.

## Milestone 2: Advanced Product V2

GA-optimised controller, sensitivity analysis, comparison and polished dashboard.

### M2 acceptance criteria

M2: encode controller parameters for GA; compare fixed, fuzzy, and GA-tuned fuzzy control across all scenarios; report comfort error and energy reduction; test empty rooms, heat waves, and high tariffs; publish a dashboard with sensitivity plots.

## Baseline and evaluation

**Baseline:** fixed threshold controller.  
Report **comfort error, energy use, rule/parameter sensitivity**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

multi-zone controller, live sensor feed, demand response.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
