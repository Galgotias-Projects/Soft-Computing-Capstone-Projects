# Milestone 2 — Enhanced Final Product V2

## What does M2 mean?

M2 improves the working M1 prototype into a complete and evaluated capstone. It is not simply finishing leftover M1 work at the deadline.

Example progression: M1 has a fuzzy climate controller. M2 uses GA to tune controller parameters, compares fixed thresholds vs fuzzy control vs GA-optimised fuzzy control across 10,000+ scenarios, and presents the result in a polished app.

## Complete these steps

### Step 1: Finish the planned advanced pipeline

Add the intended hybrid or optimisation component. Examples: ANN prediction -> fuzzy decision; GA -> tuned fuzzy controller; ANN demand forecast -> GA appliance schedule.

### Step 2: Experiment with parameters

Do not show only your best run. Change and compare settings. ANN: learning rate, epochs, hidden neurons. GA: population size, mutation rate, crossover rate, generations. Fuzzy: membership ranges/shapes, rules, defuzzification method. Explain what changed and what you learned.

### Step 3: Compare approaches quantitatively

Compare the baseline, your M1 approach, and advanced M2 approach where applicable. Use appropriate numbers such as accuracy/F1, MAE/RMSE, cost, delay, energy saved, constraint violations, or GA fitness. Include tables or plots, not only claims.

### Step 4: Test difficult cases

Deliberately test noisy readings, extreme traffic, missing or unseen data, contradictory fuzzy inputs, or strict constraints. State limitations honestly; this strengthens the viva.

### Step 5: Polish the final product

A user should be able to select inputs, run the system, see the decision/schedule, and view an explanation or visualisation. A classmate should be able to follow the README and run it.

## M2 checklist

- [ ] M1 MVP remains runnable
- [ ] Complete hybrid/optimised method is implemented
- [ ] Parameter experiments are documented
- [ ] Baseline and advanced methods are compared quantitatively
- [ ] Edge cases and limitations are included
- [ ] Product V2 is clear and runnable
- [ ] Final plots/tables, report, video link, and presentation are included or linked
- [ ] Git history shows continuous contributions from every member
- [ ] Every member can explain their own code and results for the viva

Final check: can a classmate clone the repository, follow the README, run the product, and understand what improved over the baseline?