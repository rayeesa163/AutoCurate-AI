import pandas as pd
from prophet import Prophet

def get_forecast():
    df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv")
    df.columns = ["ds", "y"]
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]
