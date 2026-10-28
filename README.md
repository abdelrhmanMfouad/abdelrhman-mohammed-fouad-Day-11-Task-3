# Diabetes Prediction Using Machine Learning

## Overview

This project uses Machine Learning to predict whether a person is likely to have diabetes based on health-related features. It explores ensemble learning techniques and compares model performance to identify a suitable model for the classification task.

## Problem Statement

Early identification of potential diabetes cases can help support further medical assessment. The goal of this project is to build a predictive model using patient-related data and provide an accessible interface for making predictions.

**Note:** This project is for educational purposes only and is not a substitute for professional medical diagnosis.

## Dataset

- **Source:** [Diabetes Prediction Dataset — Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)
- **Task:** Binary classification
- **Target:** `diabetes`
- **Data size:** Approximately 100,000 records, depending on the downloaded version.

## Models and Techniques

The project explores the following ensemble learning approaches:

- **Bagging Classifier**
- **Random Forest Classifier**
- **AdaBoost Classifier**
- **Gradient Boosting Classifier**

Additional techniques include:

- Data preprocessing
- Pipeline-based model development
- Hyperparameter tuning
- Bootstrap sampling comparison
- Out-of-Bag (OOB) score evaluation where supported
- Model evaluation and selection
- Saving the selected model for deployment

## Evaluation

Models should be evaluated using metrics suitable for imbalanced classification:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Recall and F1-score are particularly important because accuracy alone can hide poor performance on the minority class.

The final model should be selected based on the evaluation results and the project's objectives. No performance score is claimed here without verified experiment results.

## Streamlit Application

The project includes a Streamlit interface for entering patient information and obtaining a model prediction.

The application uses the saved model to generate predictions from user-provided input.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn, if required by the saved pipeline
- Joblib
- Streamlit
- Matplotlib / Seaborn, if used for visualization

## Project Structure

```text
diabetes-prediction/
├── app.py
├── notebook.ipynb
├── requirements.txt
├── best_model.pkl
└── README.md
```

The filenames may differ in your repository. Keep the model filename in `app.py` consistent with the actual saved file.

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd diabetes-prediction
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Model Loading

The application loads a previously trained model. Ensure that the saved model file is available at the path expected by `app.py`, and install compatible versions of the packages used during training.

## Limitations

- Predictions depend on the quality and representativeness of the training dataset.
- Model performance may vary across populations.
- A prediction is not a medical diagnosis.
- The model should be validated on appropriate unseen data before real-world use.

## Author

**Abdelrhman Mohammed**  
Computer Science Student | Machine Learning

