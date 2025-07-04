# CAR-T-Cell_Problem_V1

This repository contains code and notebooks for modeling CAR-T cell therapy dynamics using **SINDy**. It includes symbolic equation discovery, rational reformulation, simulation, and sensitivity analysis.

---

## Folder Structure

- `Plots_1/`, `Plots_2/`, `Plots_3/`, `Plots_4/` — Saved figures for each Example run  
- `Combined_SINDy_*.ipynb` — Jupyter notebooks for different modeling scenarios (ET, ETN, ETIN, etc.)  
- `model_1.csv`, `model_2.csv`, `model_3.csv` — Time-series datasets (obtained from 3 models)  
- `combined_df.csv` — Combined dataset (E, T, I, N)  
- `combined_library.py` — SINDy library definitions for each case  
- `plot_utils.py` — Custom plotting functions  
- `sindy_utils.py` — SINDy hyperparameter tuning and model fitting  
- `symbolic_parser.py` — Symbolic equation generation 
- `steady_states.py` — Calculating steady states  
- `network_utils.py` — Interaction graph and Jacobian structure visualization  
- `environment.yml` — Conda environment specification  
- `README.md` — This file  

---

## 🧪 Environment Setup

To reproduce the results or run the notebooks:

Make sure [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) is installed.

Open Git CMD or Anaconda Prompt, navigate to the project folder, and run:

```bash
conda env create -f environment.yml
conda activate implicit_sindy



##  Environment Setup
To reproduce the results or run the notebooks:

Make sure Miniconda or Anaconda is installed.

Open Git CMD or Anaconda Prompt, navigate to the project folder, and run:

```bash
conda env create -f environment.yml
conda activate implicit_sindy

This will create and activate the environment with all required packages.

##  Running the Code
After activating the environment, launch Jupyter:

```bash
jupyter notebook

Open and run any of the Jupyter notebooks (e.g., Combined_SINDy_ETIN.ipynb) to reproduce the model fitting, equation extraction, and plotting.

## Dependencies
This project uses Python 3.10 with the following key packages:

pysindy
sympy
scikit-learn, scipy, numpy, pandas
matplotlib, seaborn, plotly
graphviz

All dependencies are listed in environment.yml.

## Contact
For questions or suggestions, please open an issue on the GitHub repository:
https://github.com/Alka-CBhub/CAR-T-Cell_Problem_V1

