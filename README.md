📈 Stock Price Prediction - NVIDIA (NVDA)
A machine learning project to forecast the closing stock prices of NVIDIA Corporation (NVDA) using historical stock data and multiple regression models.

📌 Project Overview
Stock market forecasting is a challenging task due to the volatile and nonlinear nature of financial data. In this project, we aim to predict the next-day closing stock price of NVDA using historical stock data obtained from Yahoo Finance.

Key Features:
-Real-time data collection using Yahoo Finance
-Data preprocessing, feature engineering, and visualization
-Multiple ML regression models for evaluation
-Performance evaluation using R² score

🧠 Algorithms Used
The following regression models were trained and evaluated:

🔹 Linear Regression — R² ≈ 0.85
🔹 Ridge Regression — R² ≈ 0.85
🔹 Lasso Regression — R² ≈ 0.85
🔹 ElasticNet Regression — R² ≈ 0.85
🔹 Random Forest Regressor — R² ≈ 0.79
🔹 Support Vector Regressor (SVR) — R² ≈ 0.44

📂 Dataset

Source: Yahoo Finance
Stock: NVIDIA (Ticker: NVDA)
Features: Date, Open, High, Low, Close, Adj Close, Volume
Additional Features: Average Price, Day, Month, Year

🛠️ Tech Stack
Language: Python
Libraries:
  pandas — data manipulation
  numpy — numerical operations
  matplotlib & seaborn — visualization
  scikit-learn — machine learning models and evaluation

📊 Exploratory Data Analysis
Performed EDA to:
-Understand distribution of features like volume, open, close prices
-Visualize trends over time
-Check correlation between attributes
-Detect outliers and skewness in data

🔍 Methodology
1.Data Collection: From Yahoo Finance (CSV format)
2.Data Preprocessing: Cleaned date and volume, added engineered features
3.Train-Test Split: Data divided into training and test sets
4.Model Training: Applied and compared various regression models
5.Model Evaluation: Used R² score for performance
6.Prediction: Predicted next-day closing stock price based on the best model

📈 Results
Model             |	  R² Score
Linear Regression	|   0.85
Ridge Regression	|   0.85
Lasso Regression	|   0.85
ElasticNet	      |   0.85
Random Forest     |	  0.79
SVR	0.44

🎯 Objective
-Build a robust ML system to forecast NVDA closing price
-Enable future extensions with real-time data
-Provide users with a simple and interpretable prediction framework

🚀 Future Scope
-Integration of live stock feed APIs
-Use of LSTM/GRU (Deep Learning) models for better performance
-Web-based UI to allow users to input stock symbols and view predictions

📁 Directory Structure
├── data/
│   └── NVDA_stock.csv
├── notebooks/
│   └── EDA_and_Modeling.ipynb
├── models/
│   └── saved_models/
├── README.md
└── requirements.txt

📜 References
i)Yahoo Finance
ii)scikit-learn documentation
iii)Research papers on ML for stock prediction

🙋‍♀️ Author
Preeti
B.Tech CSE | Machine Learning & Web Development Enthusiast

📌 How to Run
# Clone the repo
git clone https://github.com/Preetisheoran08/Stock-Price-Prediction

# Navigate to project
cd stock-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/pred.ipynb
