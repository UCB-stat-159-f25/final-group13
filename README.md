[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

## S&P 500 Market Analysis 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group13/main?urlpath=lab/tree/index.md)

### Project Overview

This final group project studies whether both historical financial and macro-level signals can be used to predict movements in the S&P 500 index. We examine the widespread use and frequent overconfidence in market prediction models through an exploratory, modeling-driven analysis to assess the predictive structure, limitations, and uncertainty in big financial time-series data.

Additionally, we focus our analysis on emphasizing reproducibility and transparent scientific workflows following best practices in STAT 159/259 at UC Berkeley. The whole pipeline from data collection to modeling evaluation of models and reporting in terms of visualization, automated, and documented.

To view the complete narrative and results, open the "MainNarrative.ipynb" notebook, which is computation-free and supported by analysis notebooks and a MyST-generated website https://ucb-stat-159-f25.github.io/final-group13/.

### Repository Structure

```text
.
├── data
│   ├── final_metrics.csv        # Final analysis comparing models 
│   └── sp500.csv                # Raw data soruce of the S&P 500 data
├── images                   # Images embedded in narrative and script notebooks
│   ├── ARMINA.png  
│   ├── ...
│   └── sp500.csv            
├── notebooks
│   ├── data_prep_1.ipynb        # Notebook to get financial data we need from the yfinance APIs 
│   ├── EDA_2.ipynb              # Visualize different parts of the S&P 500 data for questions asking
│   └── Model_3.ipynb            # Implement and compare five different forecasting models
├── pdf_builds               # PDFs of all jupyter notebooks for reference
│   ├── data-prep-1.pdf  
│   ├── ...
│   └── model-3.pdf    
├── scripts
│   ├── __init__.py              # Package initialization
│   ├── data_modeling.py         # Functions to assist in modeling of forecasts
│   ├── data_process.py          # Functions to assist in data preprocessing from API
│   └── tests.py                 # Unit tests to determine functionality of the scripts
├── ai_documentation.txt     # Documentation of LLMs used for the assistance of this project
├── environment.yml          # Conda environment for reproducibility of our cleaning and analysis
├── index.md                 # Project landing page for MyST site
├── LICENSE                  # LICENCE information for our project 
├── MainNarrative.ipynb      # Main results & discussion of the project (no computation needed)
├── Makefile                 # Automation for env creation and execution
├── myst.yml                 # MyST website configuration
├── references.bib           # Bibliography
└── README.md
```

###  Requirements

- Python 3.10
- numpy
- pandas
- matplotlib
- scikit-learn
- statsmodels
- jupyter
- jupyter-book
- pytest
- yfinance
- tensorflow


### Analysis Summary

Our analysis can be completed in four stages:
1.	**Data Processing**
    Implement the data_prep_1.ipynb with data collection, cleaning, transformation, and feature construction. We note that the raw and processed datasets are stored in the data/ directory.

2.	**Exploratory Analysis**
    Visualization and descriptive analysis were conducted in EDA_2.ipynb notebook to understand trends, volatility and structure of the data.


3.	**Modeling and Evaluation**
    Created a Model_3.ipynb notebook that includes statistical and machine-learning models for performance evaluation and comparison.


4.	**Narrative**
    All results were summarized and interpreted in the MainNarrative.ipynb, which has no heavy computation and serves as the paper of our project.

### Installation: Create the Conda environment

```bash
conda env create -f environment.yml
conda activate final-group13
```

### Run the Analysis
To execute the whole pipeline of our project:

```bash
make all
```
### Testing

Reusable data-processing and modeling functions packages that are tested using pytest:

```bash
pytest tests.py
```

### Reproducibility & Automation Notes

- Were needed fixed random seeds where applicable for machine learning
- Developed modular as well as tested Python scripts
- Automated execution via Makefiles
- Fully executable via Binder for ease of access 
- PDF outputs were created
- Website configuration are defined in myst.yml


### Website

The project is deployed as a MyST-generated website hosted on GitHub Pages at https://ucb-stat-159-f25.github.io/final-group13/.

### Authors

Group 13
- Arhaan Aggarwal (arhaan@berkeley.edu)
- Brian Hwang (brianhwang5@berkeley.edu)
- David Robertson (davidrobertson@berkeley.edu)
- Jose Aguilar, M.A. (j.aguilar@berkeley.edu)

Statistics 159/259 — Fall 2025
University of California, Berkeley

### License

See LICENSE for details on how to use code, text, and figures, which are licensed to support reuse and reproducible research with attribution.
