import matplotlib.pyplot as plt
import statsmodels.graphics.gofplots as sm
from statsmodels.formula.api import ols
import datetime
import yfinance as yf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
import statsmodels.stats.api as sms
import scipy.stats as stats

def get_model(y,k):
    factors = pd.read_excel(path+"Fama and French Factors.xlsx")
    df = pd.DataFrame({'Port_ret': y - factors['Rf'], 'Market_ret': factors['Mkt-Rf'], 'SMB': factors['SMB']
                          , 'HML': factors['HML'], 'RMW': factors['RMW'], 'CMA': factors['CMA']})
    if k==3:
        modell = ols('Port_ret~Market_ret + SMB + HML', data=df).fit()
    else:
        modell = ols('Port_ret~Market_ret + SMB + HML +RMW + CMA', data=df).fit()
    print(modell.summary())



    test_for_residual_normality(modell.resid)
    test_for_residual_autocorrelation(modell.resid)
    test_for_heteroscedasticity(modell,df)
    test_for_multicollinearity(df[['Market_ret', 'SMB', 'HML', 'RMW', 'CMA']])
    print('Breusch-Pagan',sms.het_breuschpagan(modell.resid,modell.model.exog))
    print('Jarque-Bara',stats.jarque_bera(modell.resid))


def get_returns(stock):
    end_date = datetime.datetime(2024, 9, 30)
    start_date = datetime.datetime(2019, 9, 30)
    data = yf.download(stock, start=start_date, end=end_date)
    data = pd.DataFrame(data)
    data = data['Adj Close']
    monthly_data = data.resample('M').last()
    monthly_data.columns = ['Adj Close']
    monthly_data['returns'] = (monthly_data['Adj Close'] - monthly_data['Adj Close'].shift(1)) / monthly_data['Adj Close'].shift(1)
    monthly_data['returns'] = round(monthly_data['returns'],4)
    monthly_data=monthly_data.dropna()
    monthly_data.index = range(0, len(monthly_data))
    return(pd.Series(monthly_data['returns']*100))

def test_for_residual_normality(x):
    fig, ax=plt.subplots(1,2,figsize=(12,7))
    sns.histplot(x,kde=True,color='blue',ax=ax[0])
    sm.ProbPlot(x).qqplot(line='s',ax=ax[1])
    plt.savefig(path + 'Normality.png')
    print('Residual Expected Value: ', x.mean())

def test_for_heteroscedasticity(model,df):
    pred = model.predict(df)
    fig = plt.figure(figsize=(10, 5))
    plt.style.use('ggplot')
    plt.scatter(pred, model.resid)
    plt.axhline(y=0,color='b',linestyle='--')
    plt.title('Residuals vs Fitted Values')
    plt.savefig(path + 'Residuals vs Fitted Values.png')

def test_for_residual_autocorrelation(x):
    fig = plt.figure(figsize=(10, 5))
    plot_pacf(x)
    plt.title('Partial Autocorrelation Plot')
    plt.savefig(path + 'Partial Autocorrelation Plot.png')

def test_for_multicollinearity(x):
    print(x.corr())
    vif_df = pd.DataFrame()
    vif_df['Factor'] = x.columns
    vif_df['VIF'] = [variance_inflation_factor(x.values, i)
                     for i in range(len(x.columns))]
    print(vif_df)

def save_data(data,name):
    writer = pd.ExcelWriter(path + name + '.xlsx', engine='xlsxwriter')
    data.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
    writer.close()

stock=''
path=""
k=5

returns=get_returns(stock)
port_returns=pd.DataFrame({'Portfolio Returns':returns})


get_model(port_returns['Portfolio Returns'],k)
save_data(returns,'Portfolio Returns')