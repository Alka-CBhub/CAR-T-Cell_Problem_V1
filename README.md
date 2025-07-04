# CAR-T-Cell_Problem_V1

This repository contains code and notebooks for modeling CAR-T cell therapy dynamics using **SINDy**. 

---

## 📁 Folder Structure

CAR-T-Cell_Problem_V1/
├── Plots 1/, Plots 2/, Plots 3/, Plots 4/ # Saved figures for each Example run
├── Combined_SINDy_*.ipynb # Jupyter notebooks for different modeling scenarios (ET, ETN, etc.)
├── model_1.csv, model_2.csv, model_3.csv # Time-series datasets (from 3 different models)
├── combined_df.csv # Generates individual as well combined dataset (E, T, I, N)
├── combined_library.py # SINDy library definitions for each case
├── plot_utils.py # Custom plotting functions
├── sindy_utils.py # SINDy hyperparameter tuning and model fitting
├── symbolic_parser.py # Symbolic equation generation
├── steady_states.py # Calculating steady-states
├── network_utils.py # Interaction graph near steady state using Jacobian
├── environment.yml # Conda environment specification
└── README.md # This file


---


## 🧪 Environment Setup

To reproduce the results or run the notebooks:

Make sure [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda is installed.

Then open Git CMD or Anaconda Prompt and run:

```bash
conda env create -f environment.yml
conda activate implicit_sindy

This will create and activate the environment with all required packages.


---


🚀 Running the Code
After activating the environment, launch Jupyter:
```bash
jupyter notebook

Then open and run any of the notebooks in the repository.


---

📦 Dependencies
This project uses Python 3.10 with the following key packages:

pysindy

sympy

scikit-learn, scipy, numpy, pandas

matplotlib, seaborn, plotly

graphviz

All dependencies are listed in environment.yml.

---

📬 Contact
For questions or suggestions, please open an issue on the GitHub repository:
👉 https://github.com/Alka-CBhub/CAR-T-Cell_Problem_V1



