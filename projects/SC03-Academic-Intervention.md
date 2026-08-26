# SC03: Academic Intervention

**Difficulty:** ⭐⭐⭐  
**Core techniques:** Perceptron + ADALINE + Backpropagation  
**Team:** 3–4 students

## What

Identify students needing timely academic support and explain model differences.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **attendance, marks, assignments, engagement and prior performance** into **risk/support category and intervention recommendation**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

Preprocess data; implement and compare Perceptron, ADALINE and BPN; map prediction to interventions.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → Perceptron + ADALINE + Backpropagation pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Use a cited 10,000+ record dataset or documented augmentation strategy. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

one working classifier, baseline, error/convergence plots and risk MVP. Documentation-only work does not satisfy M1.

## Milestone 2: Advanced Product V2

three-model comparison, tuning, calibration and intervention dashboard.

## Baseline and evaluation

**Baseline:** majority class/simple score threshold.  
Report **accuracy/F1, confusion matrix, loss/convergence**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

fairness review, explanation module.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
