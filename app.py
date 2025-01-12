from flask import Flask, render_template, request

app = Flask(__name__)

def mean_squared_error(y_true, y_pred):
    """
    Calculate the Mean Squared Error (MSE).

    Parameters:
        y_true: List of actual values.
        y_pred: List of predicted values.

    Returns:
        MSE value as a float.
    """
    n = len(y_true)
    squared_errors = [(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)]
    mse = sum(squared_errors) / n
    return mse

@app.route('/')
def index():
    # Render the home page with an explanation of MSE
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Predefined example datasets
    examples = {
        "house_prices": {
            "y_true": [300000, 250000, 400000, 350000],
            "y_pred": [310000, 240000, 405000, 340000]
        },
        "stock_prices": {
            "y_true": [120, 130, 125, 135],
            "y_pred": [118, 132, 124, 138]
        },
        "weather_forecast": {
            "y_true": [25, 28, 30, 22, 24],
            "y_pred": [24, 29, 31, 23, 25]
        }
    }

    # Check if an example dataset is selected
    dataset = request.form.get('dataset')
    if dataset and dataset in examples:
        y_true = examples[dataset]["y_true"]
        y_pred = examples[dataset]["y_pred"]
    else:
        # Retrieve user inputs from the form
        actual = request.form.get('actual_values')
        predicted = request.form.get('predicted_values')
        try:
            y_true = list(map(float, actual.split(',')))
            y_pred = list(map(float, predicted.split(',')))
        except ValueError:
            return render_template('result.html', error="Please enter valid numbers separated by commas.")

    # Ensure the lengths match
    if len(y_true) != len(y_pred):
        return render_template('result.html', error="The number of actual and predicted values must match.")
    
    # Calculate MSE
    mse = mean_squared_error(y_true, y_pred)
    return render_template('result.html', mse=mse, y_true=y_true, y_pred=y_pred)



if __name__ == '__main__':
    app.run(debug=True)
