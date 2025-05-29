📈 Stock Price Prediction - NVIDIA (NVDA)<br>
A machine learning project to forecast the closing stock prices of NVIDIA Corporation (NVDA) using historical stock data and multiple regression models.<br>

📌 Project Overview<br>
Stock market forecasting is a challenging task due to the volatile and nonlinear nature of financial data. In this project, we aim to predict the next-day closing stock price of NVDA using historical stock data obtained from Yahoo Finance.<br>

Key Features:<br>
-Real-time data collection using Yahoo Finance<br>
-Data preprocessing, feature engineering, and visualization<br>
-Multiple ML regression models for evaluation<br>
-Performance evaluation using R² score<br>

🧠 Algorithms Used<br>
The following regression models were trained and evaluated:<br>
🔹 Linear Regression — R² ≈ 0.85<br>
🔹 Ridge Regression — R² ≈ 0.85<br>
🔹 Lasso Regression — R² ≈ 0.85<br>
🔹 ElasticNet Regression — R² ≈ 0.85<br>
🔹 Random Forest Regressor — R² ≈ 0.79<br>
🔹 Support Vector Regressor (SVR) — R² ≈ 0.44<br>

📂 Dataset<br>

Source: Yahoo Finance<br>
Stock: NVIDIA (Ticker: NVDA)<br>
Features: Date, Open, High, Low, Close, Adj Close, Volume<br>
Additional Features: Average Price, Day, Month, Year<br>

🛠️ Tech Stack<br>
Language: Python<br>
Libraries:<br>
  pandas — data manipulation<br>
  numpy — numerical operations<br>
  matplotlib & seaborn — visualization<br>
  scikit-learn — machine learning models and evaluation<br>

📊 Exploratory Data Analysis<br>
Performed EDA to:<br>
-Understand distribution of features like volume, open, close prices<br>
-Visualize trends over time<br>
-Check correlation between attributes<br>
-Detect outliers and skewness in data<br>

🔍 Methodology<br>
1.Data Collection: From Yahoo Finance (CSV format)<br>
2.Data Preprocessing: Cleaned date and volume, added engineered features<br>
3.Train-Test Split: Data divided into training and test sets<br>
4.Model Training: Applied and compared various regression models<br>
5.Model Evaluation: Used R² score for performance<br>
6.Prediction: Predicted next-day closing stock price based on the best model<br>

📈 Results<br>
Model             |	  R² Score<br>
Linear Regression	|   0.85<br>
Ridge Regression	|   0.85<br>
Lasso Regression	|   0.85<br>
ElasticNet	      |   0.85<br>
Random Forest     |	  0.79<br>
SVR	0.44

🎯 Objective<br>
-Build a robust ML system to forecast NVDA closing price<br>
-Enable future extensions with real-time data<br>
-Provide users with a simple and interpretable prediction framework<br>

🚀 Future Scope<br>
-Integration of live stock feed APIs<br>
-Use of LSTM/GRU (Deep Learning) models for better performance<br>
-Web-based UI to allow users to input stock symbols and view predictions<br>

📁 Directory Structure<br>
├── data/<br>
│   └── NVDA_stock.csv<br>
├── notebooks/<br>
│   └── EDA_and_Modeling.ipynb<br>
├── models/<br>
│   └── saved_models/<br>
├── README.md<br>
└── requirements.txt<br>

📜 References<br>
i)Yahoo Finance<br>
ii)scikit-learn documentation<br>
iii)Research papers on ML for stock prediction<br>

🙋‍♀️ Author<br>
Preeti<br>
B.Tech CSE | Machine Learning & Web Development Enthusiast<br>

📌 How to Run<br>
# Clone the repo<br>
git clone https://github.com/Preetisheoran08/Stock-Price-Prediction<br>

# Navigate to project<br>
cd stock-price-prediction<br>

# Install dependencies<br>
pip install -r requirements.txt<br>

# Run the notebook<br>
jupyter notebook notebooks/pred.ipynb<br>
