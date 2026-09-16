# Beginner Project Start Guide

This guide tells every team exactly how to start. Do not jump directly to ANN, fuzzy logic, genetic algorithms, or the final user interface. First make the problem small, define the inputs and outputs, prepare a test fixture, and prove that every team member can run the same repository.

## Deadlines and milestone meaning

- **Milestone 1 (M1):** Working Product V1, completed one week before the mid-semester examination.
- **Milestone 2 (M2):** Enhanced and deployed Product V2, completed one week before the end-semester examination.
- M1 is not a proposal, literature review, dataset, or slide deck. It must demonstrate **input -> processing -> output**.
- M2 must improve M1 with the advanced or hybrid technique, experiments, difficult cases, deployment, and final evidence.

## The eight-step path for every project

| Step | Milestone | What the team does | Evidence required |
|---|---|---|---|
| 1. Freeze the project contract | M1 | Fix the exact problem boundary, inputs, outputs, units, baseline, data source, test cases, repository, and team responsibilities. | Repository, `docs/STEP-1.md`, data dictionary, 20-row sample, five test cases, first commits. |
| 2. Build the data pipeline | M1 | Collect or generate 10,000+ cited records/scenarios; clean, validate, transform, and split them reproducibly. | `data/README.md`, preparation script/notebook, data-quality summary, processed-data instructions. |
| 3. Implement the baseline | M1 | Build the simple non-soft-computing method that the final product must beat. | Runnable baseline, saved predictions/decisions, first comparison table. |
| 4. Implement the core M1 technique | M1 | Make one complete fuzzy, ANN, or GA method work and expose its important internal steps. | Source code, algorithm explanation, training/inference/fitness evidence, plots. |
| 5. Assemble Product V1 | M1 | Connect input, validation, baseline, core method, output, and two visuals in a runnable interface. | Local Product V1, run instructions, screenshots, interim report, M1 demo. |
| 6. Add the advanced M2 technique | M2 | Add the planned optimisation, hybrid model, extra algorithms, priorities, or multi-objective constraints. | Advanced pipeline, configuration files, meaningful commits, reproducible runs. |
| 7. Experiment and stress-test | M2 | Compare baseline, M1, and M2; vary parameters; test noise, extremes, unseen cases, and constraints. | Metric tables, plots, edge-case results, limitations, selected configuration. |
| 8. Finish Product V2 | M2 | Polish and deploy the product; finish the report, video, presentation, README, and viva preparation. | Public deployment, final repository, report, approximately five-minute video, presentation. |

## Step 1: common instructions for all teams

Complete Step 1 before writing the main algorithm. A sensible target is the first three to five working days.

### 1. Create the team repository

Use a clear name such as `SC01-Climate-Controller-Team-Name`. Add every team member as a collaborator.

Create this structure:

```text
project-repository/
|-- README.md
|-- requirements.txt
|-- docs/
|   `-- STEP-1.md
|-- data/
|   |-- README.md
|   `-- sample_input.csv
|-- notebooks/
|-- src/
|-- app/
|-- results/
`-- report/
```

### 2. Assign visible responsibilities

| Responsibility | First responsibility |
|---|---|
| Repository and integration | Create folders, protect the main branch if possible, review pull requests, keep run instructions current. |
| Data and scenarios | Find sources, define columns/units, create the 20-row sample, document validation and the 10,000-record plan. |
| Baseline and algorithm | Write baseline pseudocode and the first algorithm flowchart; identify the fuzzy/ANN/GA elements required later. |
| Interface, testing, and evidence | Draw the input/output screen, write five test cases, maintain screenshots and results. |

For a three-person team, combine repository/integration with interface/testing. Responsibilities are not permanent silos: every member must understand and commit code.

### 3. Write `docs/STEP-1.md`

Use these exact headings:

```markdown
# Step 1 Project Contract
## Team and responsibilities
## One-sentence problem
## User of the product
## Inputs and units
## Outputs and units
## Baseline method
## Soft Computing method for M1
## Advanced method for M2
## Dataset/scenario sources
## Five mandatory test cases
## Product V1 screen sketch
## Risks and assumptions
## Step 1 completion evidence
```

### 4. Create the input/output dictionary

For every field, record:

- column/field name;
- plain-language meaning;
- number or category;
- unit;
- temporary starter range/categories;
- missing-value rule;
- source used to justify the final range;
- whether it is a user input, model input, target, or output.

The starter ranges below are only for the first 20-row fixture. Teams must replace or justify them using cited sources before generating 10,000 scenarios.

### 5. Create 20 sample rows and five mandatory cases

Do not start with 10,000 rows. First create a clean 20-row `data/sample_input.csv`. It must contain ordinary, boundary, and difficult cases. Write a small notebook or script that:

1. loads the file;
2. prints its shape and column names;
3. checks missing values;
4. checks ranges/categories;
5. prints the five mandatory cases without error.

### 6. Define the baseline before the Soft Computing model

Write the baseline as numbered rules or pseudocode. It must be simple enough to implement during Step 3 and meaningful enough to compare against M1/M2.

### 7. Draw one screen sketch

On paper, slides, Figma, or in `docs/STEP-1.md`, show:

- where the user enters values;
- the Run/Recommend/Optimise button;
- baseline output;
- Soft Computing output;
- one explanation or chart;
- validation/error message area.

### 8. Make attributable commits

Minimum Step 1 evidence:

- one repository-structure/README commit;
- one data dictionary/sample-data commit;
- one baseline/test-case commit;
- one interface sketch or validation-script commit;
- at least one meaningful commit from every member.

Examples: `Define climate input schema`, `Add 20 validated wash scenarios`, `Document fixed-time traffic baseline`, `Add timetable constraint fixture`.

## SC01 - Intelligent Campus Climate and Energy Controller

### Eight project steps

1. **M1:** Define one room/zone, climate inputs, controller outputs, fixed-threshold baseline, and sample scenarios.
2. **M1:** Generate and document 10,000+ temperature, humidity, occupancy, and tariff scenarios.
3. **M1:** Implement the fixed-threshold HVAC controller.
4. **M1:** Implement Mamdani membership functions, at least 12 rules, inference, and defuzzification.
5. **M1:** Build Product V1 showing live cooling/fan recommendations, baseline comparison, and two plots.
6. **M2:** Encode membership/rule parameters and optimise them with a genetic algorithm.
7. **M2:** Compare fixed, fuzzy, and GA-fuzzy control under normal, empty-room, heat-wave, and high-tariff cases.
8. **M2:** Deploy the dashboard and finish sensitivity analysis, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Choose **one room or zone**. Record its maximum occupancy and whether the controller operates cooling, fan, or both.
2. Create `data/sample_input.csv` with: `scenario_id`, `temperature_c`, `humidity_pct`, `occupancy_count`, `tariff_level`.
3. For the sample only, use temperatures 18-45 C, humidity 20-100%, occupancy 0 to the chosen room capacity, and tariff `low/medium/high`.
4. Define outputs: `cooling_pct` (0-100), `fan_level` (`off/low/medium/high`), and `energy_action` (`normal/save/avoid_peak`).
5. Draft the fixed baseline, for example: temperature bands control cooling, humidity bands adjust the fan, and an empty room forces minimum operation. Mark these as provisional rules.
6. Include these five cases: comfortable occupied room; hot-humid occupied room; empty room; heat wave with high tariff; cool room with high humidity.
7. Draw a screen with four inputs, baseline recommendation, fuzzy recommendation, rule/explanation text, and membership plot area.
8. Step 1 is complete when the validation script loads 20 rows, rejects an out-of-range row, prints all five cases, and every member has committed evidence.

## SC02 - Smart Washing Machine Decision and Resource Optimizer

### Eight project steps

1. **M1:** Fix the machine capacity, fabric categories, inputs/outputs, fixed-cycle baseline, and sample wash cases.
2. **M1:** Generate and document 10,000+ realistic wash scenarios.
3. **M1:** Implement fixed wash-cycle policies for comparison.
4. **M1:** Implement fuzzy variables, membership functions, rules, and defuzzified wash decisions.
5. **M1:** Build Product V1 returning time, water, detergent, and spin settings with baseline comparison.
6. **M2:** Use GA to tune resource/quality trade-offs and controller parameters.
7. **M2:** Compare policies for delicate fabric, scarce water, light soil, and overloaded machines.
8. **M2:** Deploy the app and finish savings/quality plots, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Choose a machine capacity, such as 7 kg or 8 kg, and state it in `docs/STEP-1.md`.
2. Create `data/sample_input.csv` with: `scenario_id`, `dirt_score`, `load_kg`, `fabric_type`, `water_availability_pct`.
3. For the sample, use dirt score 0-10; load 0.5 kg to machine capacity; fabric `delicate/cotton/synthetic/heavy`; water availability 0-100%.
4. Define outputs: `wash_time_min`, `water_litre`, `detergent_ml`, and `spin_rpm`.
5. Create a fixed-cycle baseline table with one preset per fabric type. The same preset should be used regardless of fuzzy conditions.
6. Include five cases: lightly soiled half-load; heavily soiled full cotton load; delicate fabric; low-water situation; overloaded input that must show validation.
7. Draw a screen with input controls, fixed-cycle output, future fuzzy output, and estimated water/detergent use.
8. Step 1 is complete when the 20-row file loads, fabric categories and machine capacity are validated, the five cases are printed, and every member has committed.

## SC03 - Student Performance and Academic Intervention System

### Eight project steps

1. **M1:** Define the anonymous student features, risk label, interventions, score-threshold baseline, and sample records.
2. **M1:** Prepare a cited 10,000+ record dataset or document the augmentation process and train/test split.
3. **M1:** Implement the majority-class or score-threshold baseline.
4. **M1:** Implement one transparent classifier with preprocessing, learning, prediction, and convergence/error evidence.
5. **M1:** Build Product V1 showing a risk category and actionable intervention.
6. **M2:** Implement and compare Perceptron, ADALINE, and Backpropagation Network.
7. **M2:** Tune learning settings and analyse F1, recall, confusion matrices, imbalance, noise, and fairness.
8. **M2:** Deploy the intervention dashboard and finish the report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Define the prediction unit as **one anonymous student record at one review point**. Do not collect names, phone numbers, or private student records.
2. Create `data/sample_input.csv` with: `record_id`, `attendance_pct`, `assessment_pct`, `assignment_pct`, `engagement_score`, `prior_performance_pct`, `risk_label`.
3. Use 0-100 for percentages, 0-10 for engagement, and labels `low/medium/high` for the 20-row fixture.
4. Define one intervention per band: monitoring for low risk, mentoring/study plan for medium risk, and faculty/counsellor follow-up for high risk. State that the product supports human decisions; it does not punish students automatically.
5. Draft a transparent weighted-score threshold baseline. Record the weights as provisional and explain why they must be tested.
6. Include five cases: consistently strong; low attendance only; weak marks and assignments; high engagement but weak prior performance; contradictory/boundary record.
7. Identify at least one public, anonymised dataset candidate and record its URL, licence, size, features, and target in `data/README.md`.
8. Step 1 is complete when the schema contains no personally identifying data, 20 rows validate, all risk labels are documented, and every member has committed.

## SC04 - Adaptive Traffic Signal Optimization System

### Eight project steps

1. **M1:** Freeze a simple junction model, traffic-state inputs, signal outputs, fixed-time baseline, and sample states.
2. **M1:** Generate and document 10,000+ traffic states through a reproducible simulator/scenario generator.
3. **M1:** Implement the fixed-time signal and queue update logic.
4. **M1:** Implement fuzzy traffic variables, rules, phase priority, and green-duration output.
5. **M1:** Build Product V1 with queue/wait visualisation and fixed-vs-fuzzy comparison.
6. **M2:** Use GA to tune controller parameters or phase timing.
7. **M2:** Compare three controllers under extreme queues, incidents, imbalance, and emergency vehicles.
8. **M2:** Deploy the simulator/dashboard and finish results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Model one two-phase intersection: north-south versus east-west. Do not begin with an entire city network.
2. Create `data/sample_input.csv` with: `state_id`, `queue_ns`, `queue_ew`, `density_ns_pct`, `density_ew_pct`, `max_wait_ns_sec`, `max_wait_ew_sec`, `emergency_direction`.
3. Use non-negative queues, density 0-100%, wait time 0-300 seconds, and emergency direction `none/NS/EW` for the fixture.
4. Define outputs: `next_phase` (`NS/EW`) and `green_duration_sec`, with a documented safe minimum and maximum.
5. Define the fixed baseline, such as alternating 30-second green phases, and state how queues change when vehicles arrive/depart.
6. Include five cases: balanced low traffic; heavy NS queue; heavy EW queue; long-wait but shorter queue; emergency vehicle overriding normal priority.
7. Draw a screen with junction state, Start/Next Step control, chosen phase, green duration, queue chart, and average-wait indicator.
8. Step 1 is complete when 20 states validate, impossible negative values are rejected, the baseline timing is documented, and every member has committed.

## SC05 - University Timetable Optimization Engine

### Eight project steps

1. **M1:** Define the timetable entities, hard/soft constraints, output format, random/greedy baseline, and tiny fixture.
2. **M1:** Build a reproducible generator for 10,000+ documented timetable variations.
3. **M1:** Implement the random or greedy scheduler and conflict counter.
4. **M1:** Implement chromosome encoding, population, fitness, selection, crossover, mutation, repair, and stopping.
5. **M1:** Build Product V1 with a timetable viewer, violations summary, and fitness curve.
6. **M2:** Add multi-objective constraints and stronger repair/penalty strategies.
7. **M2:** Compare GA settings and heuristic quality at small, medium, and large scales.
8. **M2:** Deploy the engine/viewer and finish results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Start with a tiny fixture: 5 courses, 3 rooms, 3 faculty members, 2 cohorts, and 10 timeslots.
2. Create `data/courses.csv` (`course_id`, `cohort_id`, `faculty_id`, `weekly_sessions`, `duration_slots`, `required_room_type`).
3. Create `data/rooms.csv` (`room_id`, `capacity`, `room_type`) and `data/timeslots.csv` (`slot_id`, `day`, `start_time`, `end_time`).
4. Write `data/constraints.md`. Hard constraints must include no faculty/room/cohort clash and suitable room. Soft constraints can include preferred time, compact schedule, and reduced gaps.
5. Define the output table: `course_id`, `room_id`, `slot_id`, `faculty_id`, `cohort_id`.
6. Define the baseline as random placement with retry or a simple greedy first-available placement.
7. Create five required fixtures: feasible timetable; room shortage; faculty clash; cohort clash; preference conflict with no hard violation.
8. Step 1 is complete when a validator reads the three files, reports entity counts, detects deliberate clashes, and every member has committed.

## SC06 - Multi-Stop Campus Shuttle or Delivery Route Optimizer

### Eight project steps

1. **M1:** Choose a small stop network, route representation, distance/traffic inputs, nearest-neighbour baseline, and sample cases.
2. **M1:** Cite the map/distance source and generate 10,000+ route/traffic scenarios.
3. **M1:** Implement nearest-neighbour route construction and cost calculation.
4. **M1:** Implement permutation GA, fitness, selection, crossover, mutation, elitism, and stopping.
5. **M1:** Build Product V1 with route display, cost comparison, and convergence plot.
6. **M2:** Add stop priorities, traffic, time windows, and penalties.
7. **M2:** Compare random, nearest-neighbour, and GA routes under congestion and constraints.
8. **M2:** Deploy the route app and finish results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Choose one depot and 6-10 campus stops. Give every stop a short ID and readable name.
2. Create `data/stops.csv` with: `stop_id`, `stop_name`, `x_coordinate`, `y_coordinate`, `priority`, `earliest_time`, `latest_time`.
3. Create `data/distance_matrix.csv`, or write a script that calculates distances from coordinates. The matrix must be symmetric unless one-way travel is explicitly modelled.
4. Define a route as an ordered list that starts and ends at the depot. Define outputs: visit order, total distance, estimated time, and penalty/cost.
5. Define the baseline as nearest unvisited stop.
6. Include five cases: ordinary six-stop route; two equally close stops; high-priority distant stop; congested connection; impossible/very narrow time window.
7. Draw a screen with stop selection, route map, visit order, baseline distance, future GA distance, and fitness curve area.
8. Step 1 is complete when the distance matrix passes diagonal/symmetry checks, route cost can be calculated for one manual route, and every member has committed.

## SC07 - Smart Irrigation and Crop Water Management System

### Eight project steps

1. **M1:** Choose a crop/context, sensor inputs, irrigation output, moisture-threshold baseline, and sample cases.
2. **M1:** Prepare 10,000+ cited agricultural/weather records or documented scenarios.
3. **M1:** Implement the fixed moisture-threshold irrigation baseline.
4. **M1:** Implement either ANN water prediction or a complete fuzzy irrigation controller.
5. **M1:** Build Product V1 with recommendation, baseline comparison, and water/error plots.
6. **M2:** Integrate ANN prediction with fuzzy decision-making.
7. **M2:** Compare threshold, ANN-only, fuzzy-only, and hybrid modes under difficult weather/sensor cases.
8. **M2:** Deploy the app and finish savings/results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Choose one crop and state whether the product models a pot, plot, greenhouse bed, or field zone.
2. Create `data/sample_input.csv` with: `scenario_id`, `soil_moisture_pct`, `humidity_pct`, `temperature_c`, `rainfall_mm`, `crop_stage`.
3. For the fixture, use moisture/humidity 0-100%, documented local temperature range, non-negative rainfall, and crop stage `initial/development/mid/late`.
4. Define outputs: `water_requirement_litre` (or mm), `irrigation_duration_min`, and `decision` (`off/low/medium/high`). State the assumed area/flow rate.
5. Define the baseline as irrigation below a fixed soil-moisture threshold, with rain override.
6. Include five cases: dry-hot; adequate moisture; recent heavy rain; dry soil with high humidity; impossible/noisy sensor reading.
7. Identify the weather/agriculture source candidates and document units, frequency, missing values, crop assumptions, and how 10,000 records will be obtained.
8. Step 1 is complete when 20 scenarios validate, unit assumptions are explicit, the threshold baseline is written, and every member has committed.

## SC08 - Machine Predictive Maintenance and Fault Priority System

### Eight project steps

1. **M1:** Define the machine observation, sensor schema, fault target, priority output, crisp-threshold baseline, and sample readings.
2. **M1:** Prepare a cited 10,000+ sensor dataset or documented augmentation pipeline.
3. **M1:** Implement crisp sensor thresholds and a baseline fault decision.
4. **M1:** Implement an ANN fault-risk model or fuzzy priority controller with error evidence.
5. **M1:** Build Product V1 with sensor input, risk/priority result, baseline, and plots.
6. **M2:** Combine ANN fault likelihood with fuzzy severity/maintenance priority.
7. **M2:** Tune and compare methods under noise, extreme readings, imbalance, and unseen conditions.
8. **M2:** Deploy the dashboard and finish results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Define one row as one machine observation/time window. Choose binary fault/no-fault or a small documented fault-category set.
2. Create `data/sample_input.csv` with: `reading_id`, `vibration`, `temperature_c`, `rpm`, `load_pct`, `severity`, `fault_label`.
3. Record the units for vibration and RPM from the chosen dataset; do not mix units from different sources.
4. Define outputs: `fault_probability`, `risk_band` (`low/medium/high`), and `maintenance_priority` (`routine/soon/immediate`).
5. Draft crisp baseline thresholds from cited documentation or dataset distributions. Mark every temporary threshold clearly.
6. Include five cases: normal operation; high vibration only; overheating under high load; multiple severe signals; missing/noisy sensor value.
7. Document the candidate dataset, class balance, sampling frequency, machine type, target definition, and planned train/validation/test split.
8. Step 1 is complete when 20 readings validate, units/labels are unambiguous, no real machine identity is exposed, and every member has committed.

## SC09 - Intelligent Loan or Credit Risk Decision Support System

### Eight project steps

1. **M1:** Define the anonymised applicant features, risk target, recommendation, crisp-score baseline, and sample cases.
2. **M1:** Prepare a cited 10,000+ public credit dataset with documented cleaning, encoding, and splits.
3. **M1:** Implement a transparent crisp score/threshold baseline.
4. **M1:** Implement the ANN classifier with training, prediction, and confusion/error evidence.
5. **M1:** Build Product V1 showing risk, confidence, recommended action, and baseline comparison.
6. **M2:** Add fuzzy handling of borderline or uncertain applicants.
7. **M2:** Compare crisp, ANN, and hybrid decisions with calibration, fairness, and difficult cases.
8. **M2:** Deploy the decision-support app and finish the report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Use only a public, anonymised dataset. Do not collect real financial information from classmates or relatives.
2. Create `data/sample_input.csv` with: `record_id`, `income`, `loan_amount`, `debt_to_income_pct`, `repayment_history`, `employment_length`, `credit_target`.
3. Define currencies/units, category meanings, missing-value handling, and target interpretation. Do not mix default probability with approval decision.
4. Define outputs: `risk_band`, `confidence`, and `recommended_action` (`review/approve/reject`), with a clear statement that this is an educational decision-support prototype.
5. Draft a crisp points/threshold baseline using a few documented features. Keep the provisional score visible and explainable.
6. Include five cases: low debt/stable history; high debt; borderline score; conflicting strong income and poor repayment; missing/unknown category.
7. Document dataset URL/licence, record count, target distribution, protected/sensitive attributes, planned encoding, and fairness checks.
8. Step 1 is complete when 20 anonymous records validate, target/action are separated, ethical limitations are recorded, and every member has committed.

## SC10 - Smart Energy Demand and Appliance Scheduling System

### Eight project steps

1. **M1:** Define a 24-hour home/building case, load/tariff/appliance inputs, output schedule, non-optimised baseline, and sample day.
2. **M1:** Prepare 10,000+ cited load records plus documented appliance/tariff scenarios.
3. **M1:** Implement persistence/simple-average forecasting or the original non-optimised schedule baseline.
4. **M1:** Implement either the ANN demand forecast or a GA scheduler MVP.
5. **M1:** Build Product V1 with forecast/schedule, daily cost, peak load, baseline, and plots.
6. **M2:** Integrate ANN demand forecasting with GA appliance scheduling.
7. **M2:** Compare plans under tariff changes, user preferences, weather, and peak constraints.
8. **M2:** Deploy the scheduling app and finish results, report, video, presentation, and viva evidence.

### Exact Step 1 work

1. Choose one home, lab, or small building and use 24 one-hour slots for the first fixture.
2. Create `data/hourly_load.csv` with: `date`, `hour`, `historical_load_kw`, `temperature_c`, `tariff_per_kwh`.
3. Create `data/appliances.csv` with: `appliance_id`, `power_kw`, `duration_slots`, `earliest_start`, `latest_finish`, `interruptible`, `priority`.
4. Define outputs: `forecast_load_kw`, appliance start slots, `daily_cost`, and `peak_load_kw`.
5. Define the baseline as the original/user-entered schedule without optimisation; use persistence or a simple moving average if a forecast baseline is required.
6. Include five cases: normal tariff; expensive evening peak; narrow appliance window; two high-power appliances competing; impossible schedule that must be flagged.
7. Draw a screen with hourly tariff/load chart, appliance table, Run Schedule button, baseline vs optimised cost, peak reduction, and schedule timeline.
8. Step 1 is complete when the 24-hour and appliance files validate, energy/cost can be calculated for the baseline schedule, impossible constraints are detected, and every member has committed.

## Step 1 submission checklist for faculty review

Every team should submit or demonstrate:

- [ ] Repository URL with all members added.
- [ ] Required folder structure and `requirements.txt`.
- [ ] Complete `docs/STEP-1.md`.
- [ ] Input/output data dictionary with units and validation rules.
- [ ] `data/README.md` containing real source URLs and licences.
- [ ] A valid 20-row sample fixture.
- [ ] Five named test cases, including a boundary/error case.
- [ ] Baseline pseudocode or rule table.
- [ ] Product V1 screen sketch.
- [ ] A script/notebook that loads and validates the sample.
- [ ] Meaningful commits from every member.
- [ ] A three-minute demonstration: clone/open repository -> install -> run validation -> show sample/test cases.

Step 1 is **not complete** if the team has only copied the problem statement, created slides, downloaded a dataset without documenting it, or uploaded all work in one commit.

