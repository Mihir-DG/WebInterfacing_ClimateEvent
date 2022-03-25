from pullData import *
from gen_windT_Profiles import *
from make_windT_Plots import *
from createGlobalMap import *
from cleanup import *
from makeTemp3dSurface import *
from precipitationRate import *
from relativeHumidity import *
from specificHumidity import *
from cloudCover import *
from skinTemperature import *

from matplotlib import pyplot as plt
import numpy as np
from netCDF4 import Dataset

def main():
	err = 0.
	year, month, date, monthConversion = getDates() #
	a = int(input("Do you want all sample data and all datasets removed from our directories? Enter '0' to clean up!"))
	if a == 0:
		print("Cleaning!")
		clean() # deletes all sample data + datasets.
	chosenData = chooseData(year)
	downloadData(year, chosenData) # Comment out if all datasets downloaded
	createMap()
	# Creating functions list
	chosenData = [i - 1 for i in chosenData] # altering chosenData to deal with list indices.
	functions = [
		[(generate_daily_windT_profs,year,month,date,monthConversion),(make_daily_windT_plots,err)], # 1 --> Wind Vector Plots (Standard Heights) (overlaying air temperature contours)
		[(generate_daily_windT_profs,year,month,date,monthConversion),(diffs_windT_gen,err), (make_delta_windT_plots,err)], # 2 --> Delta Plots for (1)
		[(generate_daily_windT_profs,year,month,date,monthConversion), (make_temp3d_dailyPlots,err)], # 3 --> 3d surface plots -- air temperature
		[(generate_precipitationRate_profs,year,month,date,monthConversion),(plot_precipitationRate,err)], # 4 --> Precipitation Rate Contours
		[(generate_relHumidity_profs,year,month,date,monthConversion),(plot_relHumidity,err)], # 5 --> Relative Humidity Contours
		[(generate_specHumidity_profs,year,month,date,monthConversion),(plot_specHumidity,err)], # 6 --> Specific Humidity Contours.
		[(generate_cloudCover,year,month,date,monthConversion),(plot_cloudCover, err)], # 7 --> Cloud Cover Contours
		[(generate_skinTemperature,year,month,date,monthConversion)),(plot_skinTemperature,err)] # 8 --> Skin Temperature Contours.
	]
	for index in chosenData:
		for fn in functions[index]:
			fn[0](*fn[1:])

if __name__ == "__main__":
	main()
