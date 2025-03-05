from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

@app.route('/')
def dashboard():
    """
    Dashboard route that renders the HTML page and passes chart data.
    """
    
    # Sample data for the Pie Chart
    pie_data = {
        'labels': ['Category A', 'Category B', 'Category C'], # Labels for each section
        'values': [40, 30, 30] # Corresponding values for each category
    }
    
    # Sample data for the Bar Chart
    bar_data = {
        'labels': ['January', 'February', 'March', 'April'], # Labels for each month
        'values': [50, 70, 40, 90] # Values representing data points
    }
    
    # Pass data to the HTML template
    return render_template('dashboard.html', pie_data=pie_data, bar_data=bar_data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Starts the server in debug mode for easy troubleshooting
