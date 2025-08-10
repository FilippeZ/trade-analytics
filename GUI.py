import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# Load the data
df = pd.read_csv('covid_trade_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')


# Define the functions to create each plot
def plot_monthly_turnover():
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    monthly_turnover = df.groupby(pd.Grouper(key='Date', freq='M'))['Value'].sum()
    plt.plot(monthly_turnover.index, monthly_turnover.values)
    plt.title('Total Turnover per Month')
    plt.xlabel('Month')
    plt.ylabel('Turnover')
    plt.show()

def plot_country_turnover():
    country_turnover = df.groupby('Country')['Value'].sum()
    plt.figure(figsize=(12,5))
    plt.bar(country_turnover.index, country_turnover.values)
    plt.title('Total Turnover per Country')
    plt.xlabel('Country')
    plt.ylabel('Turnover')
    plt.xticks(rotation=30) 
    plt.show()

def plot_transport_turnover():
    transport_turnover = df.groupby('Transport_Mode')['Value'].sum()
    plt.bar(transport_turnover.index, transport_turnover.values)
    plt.title('Overall Turnover per Means of Transport')
    plt.xlabel('Transport Mode')
    plt.ylabel('Turnover')
    plt.show()

def plot_weekday_turnover():
    weekday_turnover = df.groupby('Weekday')['Value'].sum()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_turnover = weekday_turnover.reindex(weekday_order)
    plt.bar(weekday_turnover.index, weekday_turnover.values)
    plt.title('Total Turnover per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Turnover')
    plt.xticks(rotation=30) 
    plt.show()

def plot_commodity_turnover_category_of_good():
    commodity_turnover = df.groupby('Commodity')['Value'].sum()
    plt.barh(commodity_turnover.index, commodity_turnover.values)
    plt.title('Total Turnover per Category of Goods')
    plt.ylabel('Category of Goods')
    plt.xlabel('Turnover')
    plt.show()

def plot_monthly_top_5_turnover():
    monthly_turnover = df.groupby(pd.Grouper(key='Date', freq='M'))['Value'].sum()
    top_months = monthly_turnover.sort_values(ascending=False)[:5]
    plt.bar(top_months.index.strftime('%B %Y'), top_months.values)
    plt.title('5 Months with the Highest Turnover')
    plt.xlabel('Month')
    plt.ylabel('Turnover')
    plt.xticks(rotation=30) 
    plt.show()


def plot_top_5_country_commodity_turnover():
    country_commodity_turnover = df.groupby(['Country', 'Commodity'])['Value'].sum()
    # Loop over the unique countries in the data
    for country in df['Country'].unique():
        # Get the top 5 commodities for the current country
        top_commodities = country_commodity_turnover.loc[country].nlargest(5)
        
        # Plot the results for the current country
        plt.figure(figsize=(9,4))
        plt.bar(top_commodities.index, top_commodities.values)
        plt.title(f'Top 5 Commodities with the Largest Turnover in {country}')
        plt.xlabel('Commodity')
        plt.ylabel('Turnover')
        plt.xticks(rotation=30) 
        plt.show()


df = df[df['Commodity'] != 'All']
groups = df.groupby('Commodity')
def highest_turnover_for_each_category_of_merchandise():
    results = pd.DataFrame(columns=['Commodity', 'Day', 'Turnover'])
    for name, group in groups:
        by_date = group.groupby('Date')['Value'].sum()
        sorted_by_date = by_date.sort_values(ascending=False)
        highest_day = sorted_by_date.iloc[0]
        total_turnover = group['Value'].sum()
        new_row = pd.DataFrame({'Commodity': [name], 'Day': [sorted_by_date.index[0]], 'Turnover': [total_turnover]})
        results = pd.concat([results, new_row], ignore_index=True)

    plt.figure(figsize=(12,4))
    plt.bar(results['Commodity'], results['Turnover'])
    plt.xticks(rotation=90)
    plt.ylabel('Total Turnover')
    plt.title('Presentation of the day with the highest turnover for each category of merchandise')
    plt.show()


    
# Define the GUI layout
layout = [
    [sg.Text('Select a plot:', size=(20, 1))],
    [sg.Button('Monthly Turnover', size=(20, 1))],
    [sg.Button('Country Turnover', size=(20, 1))],
    [sg.Button('Transport Turnover', size=(20, 1))],
    [sg.Button('Weekday Turnover', size=(20, 1))],
    [sg.Button('Total Turnover per Category of Goods', size=(20, 1))],
    [sg.Button('5 Months with the Highest Turnover', size=(20, 1))],
    [sg.Button('Top 5 Commodities by Country', size=(20, 1))],
    [sg.Button('Presentation of the day with the highest turnover for each category of merchandise', size=(20, 1))]
]

# Create the GUI window
window = sg.Window('Data Visualizations', layout)

# Loop through events in the GUI window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Monthly Turnover':
        plot_monthly_turnover()
        break
    elif event == 'Country Turnover':
        plot_country_turnover()
        break
    elif event == 'Transport Turnover':
        plot_transport_turnover()
        break
    elif event == 'Weekday Turnover':
        plot_weekday_turnover()
        break
    elif event == 'Total Turnover per Category of Goods':
        plot_commodity_turnover_category_of_good()
        break
    elif event == '5 Months with the Highest Turnover':
        plot_monthly_top_5_turnover()
        break
    elif event == 'Top 5 Commodities by Country':
        plot_top_5_country_commodity_turnover()
        break
    elif event == 'Presentation of the day with the highest turnover for each category of merchandise':
        highest_turnover_for_each_category_of_merchandise()
        break

# Close the GUI window
window.close()