# SC04: Adaptive Traffic Control

**Difficulty:** ⭐⭐⭐⭐  
**Core techniques:** Fuzzy Logic + Genetic Algorithm  
**Team:** 3–4 students

## What

Reduce delay under changing and uncertain traffic conditions.

## Why

This problem contains uncertainty, competing objectives, and/or non-linear relationships; Soft Computing should be justified against a crisp or fixed-rule alternative.

## Problem statement

Design, implement, and evaluate a decision-support product that converts **queue length, density, waiting time and emergency priority** into **green duration and phase priority**.

## Product to build

A runnable Streamlit, notebook-based interactive interface, GUI, or command-line application that accepts inputs, runs the model, and displays the result with at least one explanation or visualisation.

## How it works

Fuzzy real-time signal controller; GA tunes rules/membership parameters against a traffic simulation.

## System architecture

Data/scenario generation → preprocessing/validation → baseline → Fuzzy Logic + Genetic Algorithm pipeline → decision/optimised output → metrics, plots and user interface.

## Dataset strategy

Create 10,000+ documented traffic states from cited ranges/simulation. Record the source URL, licence, original size, features, target, preprocessing, and how any synthetic scenarios were produced.

## Tech stack

Python; NumPy/Pandas; Matplotlib/Plotly; Streamlit (recommended). Students may use scikit-learn for comparison, but must expose the core algorithmic logic in their own implementation.

## Milestone 1: Working Product V1

fuzzy controller, simulation, baseline and fitness/delay plots. Documentation-only work does not satisfy M1.

### M1 acceptance criteria

M1: simulate 10,000 traffic states; implement a fuzzy green-time controller and fixed-time baseline; demonstrate queue, wait, and emergency input-to-output decisions.

## Milestone 2: Advanced Product V2

GA-optimised controller, extreme-case testing and dashboard.

### M2 acceptance criteria

M2: use GA to tune fuzzy parameters; compare fixed, fuzzy, and GA-fuzzy policies; evaluate extreme queues/emergencies; report delay, throughput, and queue plots in an interactive simulator.

## Baseline and evaluation

**Baseline:** fixed-time signal.  
Report **mean delay, queue length, throughput, emergency response**, with at least three meaningful configurations/approaches where applicable. Include failure cases such as noisy, extreme, contradictory, or unseen inputs.

## Advanced possibilities

multi-junction coordination, live feeds.

## Minimum requirements

- Team of 3–4 students; Python implementation and a runnable demo.
- At least 10,000 cited dataset records or documented, realistic test scenarios.
- Implement the stated Soft Computing components meaningfully; library calls alone are insufficient.
- Include a simple baseline, parameter experiments, quantitative evaluation, visualisations, edge cases, and limitations.
- Maintain continuous, meaningful Git commits. Submit a report, ~5-minute video, presentation, and individual viva.

## Expected deliverables

Source code, dataset/scenario documentation, setup instructions, results/plots, report, video link, and presentation. Evaluation is Git 10 + Report 10 + Video 10 + Viva/Presentation 20 = **50 marks**.
