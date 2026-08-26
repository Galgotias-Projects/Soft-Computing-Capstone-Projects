# Git & Team Repository Guidelines

This guide is for beginners. Think of GitHub as your team's shared project folder with a history: it records what changed, when it changed, and who did the work.

## Five simple words

| Word | Meaning | Example |
|---|---|---|
| Repository (repo) | The online folder for your whole project | SC01-Climate-Controller-Team-A |
| File | One item inside that folder | app.py or README.md |
| Commit | A saved checkpoint with a message | Add fuzzy controller rules |
| Push | Send those checkpoints to GitHub | Make this week's work visible online |
| README | The front page of your project | Explains the project and how to run it |

You do not need to learn every Git command. Each week, add the work you completed, write a clear commit message, and push it to GitHub.

## Required structure

    project-id-project-name/
    ├── README.md              project introduction and run steps
    ├── requirements.txt       Python packages
    ├── data/README.md         data citation and download notes
    ├── notebooks/             exploration and experiments
    ├── src/                   main algorithm code
    ├── app/                   runnable Streamlit, GUI, or CLI product
    ├── results/               labelled plots and tables
    └── report/                interim and final report

Example: an irrigation team might have src/ann_model.py, src/fuzzy_controller.py, app/app.py, and results/predicted_vs_actual.png.

## What must the root README say?

1. Project ID, title, and all team members.
2. Problem, objectives, and why Soft Computing is appropriate.
3. Dataset/scenario source, URL, licence, size, features, and preprocessing.
4. Algorithms used and the simple baseline.
5. Exact setup and run instructions.
6. Current results, key visuals, limitations, and final video link.

Example status information: Milestone M1; Run command: streamlit run app/app.py; Dataset: 12,450 documented climate scenarios; Baseline: fixed-threshold controller; Current result: 18% lower energy use.

## How to work each week

1. Create the folder structure and README early.
2. Complete one small meaningful task.
3. Commit with a sentence explaining that task.
4. Push the same day or week.
5. Ensure every member has visible, meaningful contributions.

Good messages: Add dataset preprocessing pipeline; Implement Mamdani membership functions; Add GA crossover and mutation; Evaluate fixed-threshold baseline; Publish M1 interactive MVP.

Avoid messages such as update, final, changes, or one giant final upload. GitHub is assessment evidence, not storage for a final ZIP.

## M1 and M2 checks

At M1 the repository must contain cited 10,000+ data/scenarios, a working core algorithm, baseline, Product V1, and at least two plots. At M2 it must show the completed/enhanced method, experiments, edge cases, final results, report/video links, and continuous history.