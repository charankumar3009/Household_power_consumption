import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filepath, sep=';', na_values='?'):
    """
    Loads the energy dataset and returns a DataFrame.
    """
    df = pd.read_csv(filepath, sep=sep, na_values=na_values)
    return df

def clean_and_preprocess(df):
    """
    Cleans dataset by dropping missing values, converting datatypes,
    creating a DateTime index, and casting power to numeric.
    """
    df = df.dropna()
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
    df.set_index('DateTime', inplace=True)
    df['Global_active_power'] = pd.to_numeric(df['Global_active_power'])
    return df

def get_total_and_average_consumption(df):
    """
    Returns total and average energy consumption.
    """
    total = df['Global_active_power'].sum()
    average = df['Global_active_power'].mean()
    return total, average

def get_max_and_min_consumption(df):
    """
    Returns maximum and minimum energy consumption.
    """
    maximum = df['Global_active_power'].max()
    minimum = df['Global_active_power'].min()
    return maximum, minimum

def get_timeframe_consumption(df):
    """
    Returns daily, weekly, and monthly energy consumption (as DataFrames).
    """
    daily = df['Global_active_power'].resample('D').sum()
    weekly = df['Global_active_power'].resample('W').sum()
    monthly = df['Global_active_power'].resample('M').sum()
    return daily, weekly, monthly

def plot_daily_consumption(daily_consumption):
    """
    Plots daily energy consumption.
    """
    daily_consumption.plot(figsize=(15,5), title="Daily Energy Consumption")
    plt.ylabel("kW")
    plt.show()

def plot_hourly_average(df):
    """
    Plots average hourly energy consumption.
    """
    if 'hour' not in df.columns:
        df['hour'] = df.index.hour
    hourly_avg = df.groupby('hour')['Global_active_power'].mean()
    hourly_avg.plot(kind='bar', title="Average Hourly Energy Consumption")
    plt.ylabel("kW")
    plt.show()

def plot_weekday_average(df):
    """
    Plots average consumption by day of week.
    """
    if 'dayofweek' not in df.columns:
        df['dayofweek'] = df.index.dayofweek
    weekday_avg = df.groupby('dayofweek')['Global_active_power'].mean()
    weekday_avg.plot(kind='bar', title="Average Consumption by Day of Week")
    plt.ylabel("kW")
    plt.show()

def calculate_correlation(df):
    """
    Calculates correlation between power consumption and voltage.
    """
    return df['Global_active_power'].corr(df['Voltage'])

def get_high_usage_periods(df, quantile=0.99):
    """
    Returns periods where power consumption is above the specified quantile.
    """
    threshold = df['Global_active_power'].quantile(quantile)
    return df[df['Global_active_power'] > threshold]

def add_weekend_feature(df):
    """
    Adds 'is_weekend' column to the DataFrame.
    """
    if 'dayofweek' not in df.columns:
        df['dayofweek'] = df.index.dayofweek
    df['is_weekend'] = df['dayofweek'] >= 5
    return df

def save_cleaned_data(df, filename='cleaned_energy_consumption.csv'):
    """
    Saves the cleaned DataFrame to a CSV file.
    """
    df.to_csv(filename)