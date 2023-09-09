from weather import getWeather
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def preparingPastData(pastData: dict):
    days = pastData['daily']['time']
    temperature = pastData['daily']['temperature_2m_mean']
    return days, temperature


def createPlotWeatherYearAgo(parent, pastData):
    futureData, pastData = getWeather()
    x, y = preparingPastData(dict(pastData))
    fig = Figure(figsize=(5, 3))
    plotPast = fig.add_subplot(111)

    plotPast.plot(list(range(0, len(x))), y,)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=1, columnspan=2)
    plotPast.set_xlabel('X Label')  
    plotPast.set_ylabel('Y Label')  
    plotPast.set_title('Plot Title')
    fig.tight_layout()  

def preparingCurrentData(futureData: dict):
    time = futureData['hourly']['time']
    temperature = futureData['hourly']['temperature_2m']
    precipitationProb=futureData['hourly']['precipitation_probability']
    precipitation=futureData['hourly']['precipitation']
    
    return time, temperature, precipitationProb, precipitation


def createPlotWeatherCurrent(parent, futureData):
    futureData, pastData = getWeather()
    x, y, y1, y2 = preparingCurrentData(dict(futureData))
    xRange = list(range(0, len(x)))
    fig = Figure(figsize=(5, 3))
    
    plotCurrentTemp = fig.add_subplot(111)
    plotCurrentTemp.plot(xRange, y, xRange, y1, xRange, y2)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=1, columnspan=2)
    plotCurrentTemp.set_xlabel('X Label')  
    plotCurrentTemp.set_ylabel('Y Label')  
    plotCurrentTemp.set_title('Plot Title')
    fig.tight_layout()