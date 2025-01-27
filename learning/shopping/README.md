# Shopping Behavior Prediction

This repository contains a Python program that predicts customer purchasing behavior based on shopping data. It uses machine learning techniques to train a K-Nearest Neighbors (KNN) classifier to analyze the data and generate predictions.

## Features

- **Data Loading**: Reads shopping data from a CSV file and preprocesses it into numerical features and labels.
- **Model Training**: Implements a KNN classifier with `k=1` to train on the processed data.
- **Evaluation Metrics**: Calculates sensitivity (true positive rate) and specificity (true negative rate) to evaluate model performance.
- **Command-Line Interface**: Provides a simple interface to run the program with your dataset.

## Installation

1. Install the required libraries
```bash
pip install -r requirements.txt
```

## Usage
Run the program using the command line:
```bash
python shopping.py data.csv
```

## Dataset Structure

Replace `data.csv` with the path to your shopping dataset. The CSV file should have the following structure:

| Administrative | Administrative_Duration | Informational | Informational_Duration | ProductRelated | ProductRelated_Duration | BounceRates | ExitRates | PageValues | SpecialDay | Month  | OperatingSystems | Browser | Region | TrafficType | VisitorType       | Weekend  | Revenue |
|----------------|--------------------------|---------------|-------------------------|----------------|--------------------------|-------------|-----------|------------|------------|--------|------------------|---------|--------|-------------|-------------------|----------|---------|
| Integer        | Float                   | Integer       | Float                  | Integer        | Float                   | Float       | Float     | Float      | Float      | String | Integer          | Integer | Integer| Integer     | String (e.g., Returning_Visitor) | String (TRUE/FALSE) | String (TRUE/FALSE) |

## Code Explanation

### Main Function

The `main()` function orchestrates the program:
1. Validates the command-line arguments.
2. Loads the dataset and splits it into training and testing sets.
3. Trains a KNN model.
4. Evaluates the model and prints results.

### Functions

- **`load_data(filename)`**: Reads and preprocesses the CSV file into numerical evidence and labels.
- **`train_model(evidence, labels)`**: Trains a KNN classifier with `k=1`.
- **`evaluate(labels, predictions)`**: Calculates sensitivity and specificity for the model.

### Model

The program uses a **K-Nearest Neighbors classifier (k=1)** to predict customer behavior.

## Output

The program outputs the following metrics:

- **Correct**: Number of correct predictions.
- **Incorrect**: Number of incorrect predictions.
- **True Positive Rate**: Percentage of actual positive cases correctly identified.
- **True Negative Rate**: Percentage of actual negative cases correctly identified.

