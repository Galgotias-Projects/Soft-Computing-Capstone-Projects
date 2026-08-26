# Milestone 1 — Working Product V1

## What does M1 mean?

M1 is a working first product, not only a dataset, literature review, slides, or a plan. By M1, your team must show: input -> Soft Computing processing -> meaningful output.

Example for the Climate Controller: give temperature 32 C, humidity 78%, and occupancy 42; the fuzzy controller applies its membership functions and rules; it returns cooling level 76% and fan speed High.

## Complete these steps

### Step 1: Prepare the repository

Create the repository early. Add a README with the team, objective, data citation, setup instructions, and the algorithm being developed. Follow the Git guide for folders and commit examples.

### Step 2: Prepare and document 10,000+ data records or scenarios

ANN/data projects should use a cited public dataset where possible. Fuzzy and optimisation projects may generate realistic scenarios, but must explain the source of ranges and generation method. Example: temperature and humidity ranges came from cited weather data; 12,000 occupancy and tariff combinations were generated within those documented ranges.

### Step 3: Make one core technique work

ANN teams should show training/prediction and loss or error. Fuzzy teams should show variables, membership functions, rules, inference, and defuzzification. GA teams should show chromosome, population, fitness, selection, crossover, mutation, and generations.

### Step 4: Build a simple baseline

The baseline shows what improved. Examples: fixed-time traffic signal, fixed irrigation threshold, nearest-neighbour route, random timetable, or crisp credit-score threshold.

### Step 5: Build Product V1

A simple Streamlit app, interactive notebook, GUI, or command-line program is enough. A user must be able to give an input and see an output. It does not need to look polished yet.

### Step 6: Save evidence

Add at least two useful visuals to results, such as a fuzzy membership plot, loss curve, GA fitness curve, route map, predicted-vs-actual chart, or baseline comparison table.

## M1 checklist

- [ ] Regular GitHub commits from team members
- [ ] README, cited 10,000+ records/scenarios, and run steps
- [ ] One working core Soft Computing method
- [ ] One working baseline
- [ ] Runnable Product V1
- [ ] At least two saved result visuals
- [ ] Interim report with problem, data, architecture, MVP, and initial results

If you cannot demonstrate input -> processing -> output, M1 is incomplete.