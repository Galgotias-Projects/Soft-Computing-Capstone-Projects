# SC02: Smart Washing Machine

**Difficulty:** ⭐⭐⭐  
**Core techniques:** Fuzzy Logic + Genetic Algorithm  
**Team:** 3–4 students

## What

Optimise wash decisions while satisfying wash-quality and fabric-care constraints.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **dirt level, load, fabric type, water availability** into **wash time, water, detergent, and spin speed**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

Fuzzy cycle controller; GA searches resource-efficient parameters; compare with a fixed cycle.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → Fuzzy Logic + Genetic Algorithm pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Create 10,000 cited or documented wash scenarios across realistic input ranges. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

fuzzy decision MVP with baseline and input/output visualisation. Documentation-only work does not satisfy M1.

### M1 acceptance criteria

M1: build wash scenarios for dirt, load, fabric, and water availability; implement fuzzy rules; compare with a fixed cycle; demonstrate recommended time, water, detergent, and spin settings.

## Milestone 2: Advanced Product V2

GA-tuned resource optimiser with experiments and app.

### M2 acceptance criteria

M2: tune resource/quality constraints with GA; compare three policies; test delicate fabric, water scarcity, and overloaded machines; show resource-saving and wash-quality plots.

## Baseline and evaluation

**Baseline:** fixed wash cycle.  
Report **water, energy, detergent and wash-quality proxy**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

user preferences, load recognition.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
