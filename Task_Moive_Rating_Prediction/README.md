 Movie Rating Prediction

 About the Project

This project was completed as part of the CodSoft Data Science Internship. The goal of this project is to predict
the rating of a movie using Machine Learning techniques. The model learns from historical movie data and uses features such as genre, director, actors, year of release, duration, and votes to estimate a movie's rating.
 Dataset

The dataset used for this project was taken from Kaggle:

https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies

The dataset contains information about Indian movies, including:

* Movie Name
* Year of Release
* Duration
* Genre
* Rating
* Votes
* Director
* Actor 1
* Actor 2
* Actor 3

## Objective

The main objective of this project is to build a machine learning model that can predict movie ratings based on various movie-related features. This helps in understanding how different factors influence a movie's overall rating.

## Tools and Libraries Used

* Python
* Pandas
* NumPy
* Scikit-Learn

## Steps Performed

### 1. Data Loading

The dataset was loaded into Python using Pandas.

### 2. Data Cleaning

Missing values were removed, and columns such as Year, Duration, and Votes were cleaned and converted into numerical format.

### 3. Data Preprocessing

Categorical columns like Genre, Director, and Actor names were converted into numerical values using Label Encoding.

### 4. Feature Selection

The following features were used for prediction:

* Year
* Duration
* Votes
* Genre
* Director
* Actor 1
* Actor 2
* Actor 3

Target Variable:

* Rating

### 5. Model Training

The dataset was divided into training and testing sets. A Random Forest Regressor model was then trained using the 
training data.

### 6. Prediction and Evaluation

The trained model was used to predict movie ratings. The performance of the model was evaluated using Mean Absolute Error (MAE) and R² Score.

## Output

Example output obtained from the model:

* MAE: 1.02
* R² Score: 0.075
* Predicted Rating: 6.13

The results show that the model is capable of predicting movie ratings, although the accuracy can be improved further by using additional features and advanced machine learning techniques.

## Project Structure

Movie_Rating_Prediction/

├── movie_rating_prediction.py

├── README.md

├── requirements.txt

└── screenshots/

    ├── code.png

    └── output.png

## Future Improvements

* Use more movie-related features for training.
* Perform feature engineering.
* Experiment with different machine learning algorithms.
* Improve model accuracy through parameter tuning.

## Conclusion

This project provided hands-on experience with data preprocessing, feature encoding, model training, and evaluation. 
It demonstrates how machine learning can be used to analyze movie data and predict ratings based on various factors.

## Author

CodSoft Data Science Internship Project

