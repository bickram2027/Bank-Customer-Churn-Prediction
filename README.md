# Bank Customer Churn Prediction

## Project Overview

This project predicts whether a bank customer is likely to churn based on customer information such as credit score, age, balance, number of products, activity status and other customer details.

The project includes data exploration, exploratory data analysis, statistical feature selection, data preprocessing, model comparison and deployment using Streamlit.

Three classification models were trained and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

After comparing the models, Random Forest was selected as the final model because it achieved the best overall performance.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

## Dataset

The dataset contains **10,000 bank customer records** and the following features:

* `customer_id`
* `credit_score`
* `country`
* `gender`
* `age`
* `tenure`
* `balance`
* `products_number`
* `credit_card`
* `active_member`
* `estimated_salary`
* `churn`

The target variable is:

```text
churn
```

where:

* `0` = Customer did not churn
* `1` = Customer churned

The `customer_id` column was removed because it is an identifier and does not provide useful information for predicting churn.

## Data Exploration

The dataset was explored using:

* `head()` to view the first few records
* `info()` to check data types and missing values
* `describe()` to understand numerical statistics

The dataset was also analysed using different visualisations to understand relationships between features and customer churn.

## Exploratory Data Analysis

The following analyses were performed:

### Correlation Analysis

A correlation matrix and heatmap were created for numerical features to understand relationships between variables.

### Scatter Matrix

Scatter matrix plots were created for:

* Balance
* Estimated Salary
* Age

This helped understand distributions and relationships between numerical variables.

### Balance vs Age

A scatter plot of balance against age was created to examine their relationship.

## Feature Selection

Statistical tests were used to identify features that have a significant relationship with customer churn.

### Chi-Square Test

Chi-square tests were applied to categorical features:

* Country
* Gender
* Credit Card
* Active Member

Features such as `country`, `gender` and `active_member` showed significant relationships with churn.

### T-Test

T-tests were applied to numerical features:

* Credit Score
* Age
* Tenure
* Balance
* Products Number
* Estimated Salary

Features such as `age`, `balance`, `products_number` and `credit_score` showed significant differences between churned and non-churned customers.

## Data Preprocessing

A preprocessing pipeline was created using `ColumnTransformer`.

### Numerical Features

Numerical features were processed using:

* Median imputation for missing values
* StandardScaler for feature scaling

### Categorical Features

Categorical features were processed using:

* One-Hot Encoding
* `handle_unknown="ignore"` to handle unseen categories

The preprocessing steps were fitted on the training data and then applied to the test data.

## Model Training

Three classification algorithms were trained:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Decision Tree Classifier

Used to capture non-linear relationships between customer features and churn.

### 3. Random Forest Classifier

An ensemble model consisting of multiple decision trees. It was selected as the final model because it achieved the best overall performance among the tested models.

## Model Evaluation

The models were evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

The Random Forest Classifier achieved the best overall performance among the three models.

## Model Deployment

After selecting Random Forest as the final model, the preprocessing steps and trained model were saved together using Joblib.

The saved model file is:

```text
customer_churn_model.pkl
```

The file contains the trained model and the preprocessing pipeline required to make predictions on new customer data.

## Streamlit Application

A Streamlit application was created to allow users to enter customer details and predict the probability of customer churn.

The application takes inputs such as:

* Credit Score
* Country
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card
* Active Member
* Estimated Salary

The trained Random Forest model then predicts whether the customer is likely to churn.

## Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── bank.py
├── Bank Customer Churn Prediction.csv
├── customer_churn_model.pkl
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Bank-Customer-Churn-Prediction.git
```

### 2. Open the project folder

```bash
cd Bank-Customer-Churn-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run bank.py
```

The application will open in your browser.

## Final Model

The final model used in the application is:

**Random Forest Classifier**

The trained model and preprocessing pipeline are stored in:

```text
customer_churn_model.pkl
```

It can be loaded using:

```python
import joblib

model = joblib.load("customer_churn_model.pkl")
```

## Author

**Bickram Chowdhury**

B.Tech – Computer Science and Engineering
