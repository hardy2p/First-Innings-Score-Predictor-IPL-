# Importing essential libraries
from flask import Flask, render_template, request
from markupsafe import escape  # Explicitly import escape from markupsafe
import pickle
import numpy as np

# Load the Random Forest Regressor model
filename = 'first-innings-score-lr-model.pkl'
with open(filename, 'rb') as file:
    regressor = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        # Handle Batting Team
        batting_team = escape(request.form['batting-team'])
        if batting_team == 'Chennai Super Kings':
            temp_array.extend([1, 0, 0, 0, 0, 0, 0, 0])
        elif batting_team == 'Delhi Daredevils':
            temp_array.extend([0, 1, 0, 0, 0, 0, 0, 0])
        elif batting_team == 'Kings XI Punjab':
            temp_array.extend([0, 0, 1, 0, 0, 0, 0, 0])
        elif batting_team == 'Kolkata Knight Riders':
            temp_array.extend([0, 0, 0, 1, 0, 0, 0, 0])
        elif batting_team == 'Mumbai Indians':
            temp_array.extend([0, 0, 0, 0, 1, 0, 0, 0])
        elif batting_team == 'Rajasthan Royals':
            temp_array.extend([0, 0, 0, 0, 0, 1, 0, 0])
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array.extend([0, 0, 0, 0, 0, 0, 1, 0])
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array.extend([0, 0, 0, 0, 0, 0, 0, 1])
            
        # Handle Bowling Team
        bowling_team = escape(request.form['bowling-team'])
        if bowling_team == 'Chennai Super Kings':
            temp_array.extend([1, 0, 0, 0, 0, 0, 0, 0])
        elif bowling_team == 'Delhi Daredevils':
            temp_array.extend([0, 1, 0, 0, 0, 0, 0, 0])
        elif bowling_team == 'Kings XI Punjab':
            temp_array.extend([0, 0, 1, 0, 0, 0, 0, 0])
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array.extend([0, 0, 0, 1, 0, 0, 0, 0])
        elif bowling_team == 'Mumbai Indians':
            temp_array.extend([0, 0, 0, 0, 1, 0, 0, 0])
        elif bowling_team == 'Rajasthan Royals':
            temp_array.extend([0, 0, 0, 0, 0, 1, 0, 0])
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array.extend([0, 0, 0, 0, 0, 0, 1, 0])
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array.extend([0, 0, 0, 0, 0, 0, 0, 1])
            
        # Match details
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        # Add these details to the temp_array
        temp_array.extend([overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5])
        
        # Convert to numpy array for prediction
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit=my_prediction - 10, upper_limit=my_prediction + 5)

if __name__ == '__main__':
    app.run(debug=True)