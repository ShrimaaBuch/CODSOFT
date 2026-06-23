# Sales Prediction Using Python

## Project Overview

This project uses Machine Learning to predict product sales based on advertising budgets spent on TV, Radio, and
Newspaper advertisements.

The objective is to understand how different advertising channels influence sales and to build a model that can estimate
future sales from advertising expenditure.

This project was completed as part of the CODSOFT Data Science Internship.

---

## Dataset Information

The dataset contains the following columns:

- TV – Advertising budget spent on TV
- Radio – Advertising budget spent on Radio
- Newspaper – Advertising budget spent on Newspaper
- Sales – Sales generated

The Sales column is the target variable that the model predicts.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

## Machine Learning Model

For this project, I used **Linear Regression**, a supervised machine learning algorithm that helps predict continuous 
numerical values.

The model learns the relationship between advertising budgets and sales, then uses that relationship to make predictions.

---

## Project Workflow

1. Loaded and explored the dataset
2. Checked for missing values
3. Performed basic data analysis
4. Visualized relationships between variables
5. Split the dataset into training and testing sets
6. Trained a Linear Regression model
7. Predicted sales on unseen data
8. Evaluated model performance using different metrics
9. Allowed users to enter advertising budgets and get predicted sales

---

## Performance Metrics

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model achieved an R² score of approximately 0.90, indicating strong predictive performance.

---

## Sample Prediction

Users can enter values such as:

TV Budget: 200
Radio Budget: 40
Newspaper Budget: 30

The model then predicts the expected sales based on these inputs.

---

## Key Learnings

Through this project, I learned:

- How to work with datasets using Pandas
- Data visualization using Matplotlib and Seaborn
- The basics of Machine Learning
- How Linear Regression works
- Model evaluation techniques
- Making predictions using trained models

---

## Conclusion

This project demonstrates how Machine Learning can be used to analyze advertising data and predict future sales. 
Such predictions can help businesses make better marketing decisions and allocate advertising budgets more effectively.

---

### Author

Completed as part of the CODSOFT Data Science Internship.
