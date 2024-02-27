# -*- coding: utf-8 -*-
"""Japan_GDP_Forecast

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vcDmH_KvwMc2hu7dIh3HqSp1UiC79VfN
"""

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# Read data from excel file
data = pd.read_excel("/content/sample_data/Japan.xlsx")

# Selecting the data for ARIMA model
japan_gdp = data[['Year', 'GDP']]
japan_gdp.set_index('Year', inplace=True)

# Fit the ARIMA model
model = ARIMA(japan_gdp, order=(5,1,0))
model_fit = model.fit()

# Forecasting for the next 5 years
forecast = model_fit.forecast(steps=5)

# Plotting the forecast
plt.figure(figsize=(10, 6))
plt.plot(japan_gdp.index, japan_gdp['GDP'], label='Historical GDP')
plt.plot(range(2023, 2028), forecast, color='red', linestyle='--', label='Forecasted GDP')
plt.title('Japan GDP Forecast 2023-2027')
plt.xlabel('Year')
plt.ylabel('GDP in Billion USD')
plt.legend()
plt.show()

# Output the forecast values
print('Forecasted GDP values for 2023 to 2027 in Billion USD :\n',forecast)