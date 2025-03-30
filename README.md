# Social Media Emotion Predictor

This project is a **Social Media Emotion Prediction** web application that allows users to input comments and get the predicted emotion (e.g., happy, sad, angry, etc.) using a trained machine learning model. The app is built using **Flask**, with a **RandomForestClassifier** for the emotion prediction and a **TF-IDF Vectorizer** for text preprocessing. The application also features an attractive, user-friendly, and animated web interface.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Requirements](#requirements)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Emotion Prediction**: Takes user comments as input and predicts the emotion using a trained machine learning model.
- **Interactive Web Interface**: The web interface is designed using HTML/CSS with animations and interactive features.
- **Model Training**: Allows users to retrain the model with new data for better predictions.
- **Flask Backend**: The backend of the web app is powered by Flask.
- **Preprocessing with TF-IDF**: Uses TF-IDF for converting text data into numerical format before feeding it into the machine learning model.

## Project Structure

```
├── app.py                        # Main Flask application
├── templates/
│   └── index.html                # HTML template for the web interface
├── static/
│   └── css/
│       └── style.css             # Custom CSS for styling
├── model/
│   ├── model.pkl                 # Trained machine learning model
│   └── tfidf_vectorizer.pkl      # Trained TF-IDF vectorizer
├── dataset/
│   └── social_media_listening_emotions_dataset.csv  # Dataset for training the model
├── train_model.py                # Python script for training the model
├── requirements.txt              # Python package dependencies
├── README.md                     # Project documentation
└── .gitignore                    # Files to ignore in Git
```

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/social-media-emotion-predictor.git
   cd social-media-emotion-predictor
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # or
   source myenv/bin/activate  # On macOS/Linux
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download or prepare the dataset**:
   Ensure that the `social_media_listening_emotions_dataset.csv` file is placed in the `dataset/` directory.

5. **Run the Flask app**:
   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/` in your browser.

## Running the App

Once the app is running, you can access the interface via the browser. Type in a comment in the text box and click "Predict Emotion" to get the emotion prediction.

## Usage

- Open the web app in your browser.
- Input any text comment (e.g., "I am feeling amazing today!").
- Click on the "Predict Emotion" button.
- The predicted emotion (e.g., "happy") will be displayed on the screen.

## Training the Model

If you wish to train the model on a new dataset or retrain it, follow these steps:

1. Prepare your dataset in CSV format, similar to the `social_media_listening_emotions_dataset.csv` file.
2. Update the dataset path in `train_model.py` and run the following command:
   ```bash
   python train_model.py
   ```
3. This will generate new `model.pkl` and `tfidf_vectorizer.pkl` files, which you can use in the Flask app.

## Requirements

The following Python packages are required for this project:

- Flask
- scikit-learn
- pandas
- numpy
- matplotlib (optional, for visualization)

You can install these packages using `pip` via the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Screenshots

Here are some screenshots of the application:

### Homepage:
![Homepage Screenshot](static/screenshots/homepage.png)

### Emotion Prediction:
![Emotion Prediction Screenshot](static/screenshots/emotion_prediction.png)

## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

Feel free to open issues if you encounter any problems or have suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This `README.md` provides a complete overview of the project, installation instructions, usage, and contribution guidelines. It will help users and contributors understand your project better and encourage collaboration.
