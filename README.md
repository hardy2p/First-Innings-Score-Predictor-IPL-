# IPL First Innings Score Predictor

## Overview
The **IPL First Innings Score Predictor** is a machine learning-based web application developed using Flask. It predicts the score of the first innings in an IPL cricket match based on user inputs such as batting team, bowling team, overs played, and current runs scored.

## Features
- **User-Friendly Interface:** A simple and intuitive web interface to input match details.
- **Real-Time Predictions:** Predicts the score of the first innings in real-time.
- **Machine Learning Model:** Built using Python's machine learning libraries.

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Machine Learning:** scikit-learn, pandas, numpy
- **Deployment:** Flask Server (can be deployed on platforms like Heroku, AWS, etc.)

## Requirements
- Python 3.7 or above
- Libraries:
  - Flask
  - scikit-learn
  - pandas
  - numpy
  - jinja2

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IPL-First-Innings-Score-Prediction.git
   cd IPL-First-Innings-Score-Prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter the match details:
   - Batting team
   - Bowling team
   - Overs played
   - Current runs scored
2. Click on the **Predict Score** button.
3. View the predicted score for the first innings.

## Model Details
The machine learning model was trained using historical IPL data. It uses regression techniques to predict the score based on features such as:
- Batting team
- Bowling team
- Overs played
- Current runs scored

### Dataset
The dataset used for training includes IPL match data from previous seasons.

## Folder Structure
```
IPL-First-Innings-Score-Prediction/
├── app.py                  # Flask application file
├── templates/              # HTML templates
├── static/                 # CSS and JS files
├── model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## Deployment
To deploy this application:
1. Use platforms like Heroku, AWS, or Google Cloud.
2. Ensure the required dependencies are installed on the server.
3. Configure the `Procfile` and `runtime.txt` if deploying on Heroku.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, feel free to contact:
- **Name:** Pushpendra
- **Email:** work.pushpendra16@gmail.com
