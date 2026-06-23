# Iris Flower Classification

## About the Project

This project was completed as part of the CodSoft Data Science Internship.

The goal of this project is to build a machine learning model that can identify the species of an Iris flower based on its sepal and petal measurements.
The model classifies flowers into one of the following categories:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

## Dataset

The project uses the famous Iris Flower Dataset, which contains 150 flower samples. Each sample includes:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species

The dataset is commonly used for learning and practicing classification algorithms in machine learning.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

## Project Workflow

1. Loaded and explored the dataset.
2. Checked for missing values.
3. Visualized the data using different plots.
4. Split the dataset into training and testing sets.
5. Trained a Random Forest Classifier model.
6. Evaluated the model using accuracy score and confusion matrix.
7. Tested the model with sample flower measurements.

## Visualizations

The following visualizations were created during the project:

- Species Distribution Plot
- Pair Plot
- Correlation Heatmap

These plots help in understanding the dataset and relationships between different flower measurements.

## Model Performance

The Random Forest Classifier achieved excellent performance on the Iris dataset with an accuracy close to 100%.

## Project Files

- `iris_classification.py` – Main source code
- `Iris.csv` – Dataset used for training and testing
- `species_distribution.png` – Species distribution graph
- `pairplot.png` – Pair plot visualization
- `heatmap.png` – Correlation heatmap
- `README.md` – Project documentation

## How to Run the Project

Install the required libraries:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

Run the program:

```bash
python iris_classification.py
```

## Conclusion

This project demonstrates how machine learning can be used to classify Iris flower species using simple measurements. 
It also helped me understand the basic workflow of a data science project, including data analysis, visualization, model training, and evaluation.
