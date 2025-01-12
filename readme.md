# Mean Squared Error (MSE) Calculator Project

This project implements a web-based application to calculate the **Mean Squared Error (MSE)**, a common metric for evaluating the accuracy of regression models. It provides an intuitive interface to input actual and predicted values or select predefined datasets to see MSE in action.

## Features

- **Interactive Web App**: Input actual and predicted values to calculate MSE dynamically.
- **Predefined Scenarios**: Demonstrate MSE usage with example datasets (e.g., house prices, stock prices, weather forecasts).
- **Error Handling**: Handles invalid or mismatched inputs gracefully.
- **Comprehensive Results**: Displays MSE along with the actual and predicted values.
- **Test Integration**: Run predefined unit tests directly from the app.

---

## Table of Contents
1. [Introduction to MSE](#introduction-to-mse)
2. [Significance of MSE in Model Evaluation](#significance-of-mse-in-model-evaluation)
3. [How to Run the Project](#how-to-run-the-project)
4. [Application Scenarios](#application-scenarios)
5. [Project Structure](#project-structure)

---

## Introduction to MSE

The **Mean Squared Error (MSE)** is a metric that quantifies the average squared difference between actual and predicted values in regression tasks. It is calculated as:

\[
MSE = \frac{1}{n} \sum_{i=1}^n (y_{true} - y_{pred})^2
\]

Where:
- \( y_{true} \): Actual values
- \( y_{pred} \): Predicted values
- \( n \): Number of data points

---

## Significance of MSE in Model Evaluation

1. **Performance Metric**:
   - MSE evaluates how well a regression model predicts outcomes.
   - Lower MSE values indicate better model performance.

2. **Outlier Sensitivity**:
   - Since MSE squares the differences, it gives more weight to larger errors, making it sensitive to outliers.

3. **Widely Used**:
   - Commonly used in regression tasks to compare the accuracy of different models or algorithms.

4. **Real-World Applications**:
   - Predicting house prices.
   - Forecasting stock prices.
   - Analyzing weather data.

---

## How to Run the Project

### Prerequisites
- Python 3.7+
- Flask

### Setup
1. Clone the repository or download the source code.
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Navigate to the project directory and run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Application Scenarios

### Example Scenarios

1. **House Price Prediction**:
   - **Actual Values**: [300000, 250000, 400000, 350000]
   - **Predicted Values**: [310000, 240000, 405000, 340000]
   - **MSE**: 25000000.0

2. **Stock Price Forecasting**:
   - **Actual Values**: [120, 130, 125, 135]
   - **Predicted Values**: [118, 132, 124, 138]
   - **MSE**: 4.5

3. **Weather Forecast**:
   - **Actual Values**: [25, 28, 30, 22, 24]
   - **Predicted Values**: [24, 29, 31, 23, 25]
   - **MSE**: 1.0

### How to Use:
- Select a predefined dataset to see how MSE is calculated for different scenarios.
- Input your own actual and predicted values to evaluate your data.

---

## Project Structure

```
project_directory/
|
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html         # Home page with input form
│   └── result.html        # Results page
├── static/                # Static assets (CSS)
│   ├── index_style/       # Styles for index.html
│   └── result_style/      # Styles for result.html
└── README.md              # Project documentation
```

Enjoy using the **MSE Calculator Project**! If you have any suggestions or encounter issues, feel free to reach out.

