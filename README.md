# Project Title
## Fama and French Model Estimation with Python <br>
# Contents
[Info](#Info)<br>
[How it Works](#How-it-Works)<br>
[Example](#Example)<br>
[Data](#Data)<br>
[Results](#Results)<br>
[Disclaimer](#Disclaimer)
# Info
## Programming Language: 
Python <br>
## Libraries used:
[Pandas](https://pandas.pydata.org/#:~:text=pandas%20is%20a%20fast,%20powerful,%20flexible)<br>
[Numpy](https://numpy.org/)<br>
[Yfinance](https://pypi.org/project/yfinance/)<br>
[Datetime](https://docs.python.org/3/library/datetime.html)<br>
[Statsmodels](https://www.statsmodels.org/stable/index.html)<br>
[Seaborn](https://seaborn.pydata.org/tutorial.html)<br>
[Sklearn](https://scikit-learn.org/stable/index.html) <br>
# How it Works
The program is used to estimate the Fama and French three-factor or five-factor model, as well as to conduct various statistical tests.
Before executing the program, the following need to be initialized:
The variable stock with the ticker of the stock.
The variable k with a value of 3 for the estimation of the three-factor model, or alternatively with a value of 5 for the estimation of the five-factor model.
Once executed, the program:
1.	Retrieves the monthly prices for the stock via the yfinance library and stores them in a data frame.
2.	Calculates the stock's monthly returns.
3.	Retrieves the data for Fama and French’s five factors. These data have been retrieved from the online library of Kenneth R. French (Kenneth R. French - Data Library) and saved in an .xlsx file.
4.	Estimates the model using the Ordinary Least Squares method via the corresponding function in the statsmodels package.
5.	Presents the results, which include, among others, the coefficient estimates, their corresponding p-values, and the results of the Durbin-Watson, Jarque-Bera, and Breusch-Pagan tests.
6.	Allows the user to check the normality of the residuals, as well as any potential autocorrelation and heteroscedasticity of the residuals by generating corresponding graphs.
7.	Checks for potential multicollinearity using a Variance Inflation Factor (VIF) test.
8.	Displays the correlation coefficients for each pair of factors.
9.	Saves the stock returns in an .xlsx file.
# Example
## Data
Below, the five-factor model will be estimated for the [Vanguard Mega Cap Growth ETF](https://investor.vanguard.com/investment-products/etfs/profile/mgk?msockid=0d7c1b389fd661bf19ad0fb99eca60b6).<br>
To estimate the model monthly returns from October 2019 to September 2024 (60 observations) were used. <br>
The data for the five factors have been retrieved from the online library of Kenneth R. French - Data Library. 


## Results:

![Στιγμιότυπο οθόνης 2025-02-05 194431](https://github.com/user-attachments/assets/2048190e-5b48-4dd8-87eb-4f21c0f17985)


![Στιγμιότυπο οθόνης 2025-02-05 194444](https://github.com/user-attachments/assets/16d7534b-b538-4376-aba7-56aa6fff9ec1)

![Partial Autocorrelation Plot](https://github.com/user-attachments/assets/ca5f9a9e-b2ac-435d-8d03-b74b394c8be3)

![Normality](https://github.com/user-attachments/assets/4628b1f1-cb55-4574-92cb-66ced44117d4)

![Residuals vs Fitted Values](https://github.com/user-attachments/assets/d9720b57-99e3-4b98-8323-4ceb2c7da25b)

# Disclaimer

This project serves educational purposes only. <br>
Under no circumstances should it be used as an actual investing tool.
