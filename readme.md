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
6. [Test Cases](#test-cases)

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
│   └── test_results.html  # Page displaying unit test results
├── static/                # Static assets (CSS)
│   ├── index_style/       # Styles for index.html
│   └── result_style/      # Styles for result.html
├── tests.py               # Unit tests for MSE and the Flask app
└── README.md              # Project documentation
```

---

## Test Cases

### Example Test Cases

```python
import unittest
from app import mean_squared_error

class TestMeanSquaredError(unittest.TestCase):
    def test_correct_mse(self):
        y_true = [1, 2, 3]
        y_pred = [1.1, 2.1, 3.1]
        self.assertAlmostEqual(mean_squared_error(y_true, y_pred), 0.01, places=2)

    def test_empty_lists(self):
        y_true = []
        y_pred = []
        with self.assertRaises(ZeroDivisionError):
            mean_squared_error(y_true, y_pred)

    def test_length_mismatch(self):
        y_true = [1, 2, 3]
        y_pred = [1, 2]
        with self.assertRaises(ValueError):
            mean_squared_error(y_true, y_pred)
```

### Running the Tests
1. Save the test cases in `tests.py`.
2. Run the tests:
   ```bash
   python tests.py
   ```
3. Alternatively, run the tests through the web app by clicking **"Run Test Cases"**.

---

Enjoy using the **MSE Calculator Project**! If you have any suggestions or encounter issues, feel free to reach out.

#   M e a n - S q u a r e d - E r r o r - M S E - I m p l e m e n t a t i o n  
 