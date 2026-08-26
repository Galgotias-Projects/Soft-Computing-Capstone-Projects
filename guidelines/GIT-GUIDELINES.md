# Git & Team Repository Guidelines

After allocation, each team must create a **separate development repository** under the **Galgotias-Projects** organization. This central repository remains the official project catalogue.

## Required repository structure

```text
project-id-project-name/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── notebooks/
├── src/
├── app/
├── results/
├── report/
└── docs/                         # optional: diagrams, video link, slides
```

Do not upload raw datasets when their licence, size, or source terms prohibit it. In that case, provide a download script or clear instructions in data/README.md.

## Required contents

### Root README.md

The README must state:

- project ID, title, team members, and faculty mentor (if assigned);
- problem statement, objectives, and why Soft Computing is appropriate;
- architecture diagram or pipeline;
- algorithms used and baseline;
- dataset/scenario source, URL, licence, original size, features, and preprocessing;
- setup and run instructions;
- current results, key visualisations, limitations, and video link when available.

### Source and application

- **src/**: reusable preprocessing, algorithm, evaluation, and utility code.
- **app/**: runnable Streamlit/GUI/CLI entry point.
- **notebooks/**: exploratory work and experiments; the final product must not exist only in a notebook.
- **results/**: generated plots, tables, saved predictions/schedules, and a short explanation of each result.
- **report/**: interim and final report source/PDF as instructed by faculty.
- **requirements.txt**: exact Python dependencies and versions where practical.

## Minimum Git evidence

GitHub is assessed as development evidence, not file storage. Each team must:

1. Create the repository early and add the initial structure and README.
2. Commit incrementally throughout both milestones.
3. Use descriptive commit messages, for example:
   - Add cited dataset preprocessing pipeline
   - Implement Mamdani membership functions
   - Add GA crossover and mutation operators
   - Evaluate fixed-threshold baseline
   - Publish M1 interactive MVP
4. Ensure each member contributes visible, meaningful work through commits, pull requests, reviews, documentation, or clearly attributable modules.
5. Use branches and pull requests where practical; direct commits are acceptable for a small team if history remains clear.
6. Tag or otherwise identify the M1 and final/M2 submissions.

Uploading a ZIP, one final code dump, or only a few end-of-semester commits will not receive full Git marks.

## Milestone repository checklist

| Item | M1 | M2 |
|---|:---:|:---:|
| README, team, setup, data citation | Required | Updated |
| 10,000+ records/scenarios documented | Required | Required |
| Core Soft Computing implementation | Working | Complete/enhanced |
| Baseline | Working | Compared quantitatively |
| Runnable product | Product V1 | Polished Product V2 |
| Results and plots | At least 2 | Full experiments and edge cases |
| Continuous commit history | Required | Required |
| Report/video links | Interim report | Final report and video |

## Suggested README status block

```text
Milestone: M1 / M2
Run command: streamlit run app/app.py
Dataset/scenarios: 12,450 records — source and citation below
Baseline: Fixed threshold controller
Current best result: 18% lower energy use than baseline
```
