import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as plt
from PIL import Image

def generate_skinTemperature(year,month,date,monthConversion):
	NC_skinTemperature = Dataset('skt.sfc.gauss.' + str(year) + '.nc', "r", format="NETCDF4")
	skinTemperature = np.array(NC_skinTemperature.variables['skt'])#	shape(366,8,73,144) for 2020.
	# newDate calculation.
	if len(skinTemperature) == 366: # Assuming no. of time entries for surf + pressure datasets are equal.
		leapYear = True
	newDate = 0
	for elem in monthConversion.keys():
		if elem != month:
			newDate += (monthConversion[elem])[1]
		else:
			newDate += date
			break
	if leapYear == True and newDate > 59:
		newDate += 1
	# Extracting profs by alt. (Indexes: 300mbar: -1, 850mbar: 2)
	skinTemperature = skinTemperature[newDate - 3 : newDate + 4]
	np.save("outData/skt_7d_surface_3x7x94x192.npy",full_relHumidity) # Arranged by ascending altitude.
	return 0.

def plot_skinTemperature(err):
	sktData = np.load("outData/skt_7day_surface_7x94x192.npy")
	x = np.linspace(0,191,num=9,endpoint=True) 
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))]
	y = np.linspace(0,93,num=7,endpoint=True)
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))]
	im = Image.open("globalMap.png")
	dayLabel = 1
	for dailyProfile in sktData:
		fig = plt.figure()
		ax = plt.axes()
		plt.imshow(im,extent=[0,191,0,93])
		plt.xlabel("Latitude")
		plt.ylabel("Latitude")
		plt.xticks(x,xLabels)
		plt.yticks(y,yLabels)
		cs =  ax.contourf(dailyProfile,alpha=0.6)
		plt.colorbar(cs, ax=ax, label="Precipitation Rate (Kg/m^2/s)", orientation='horizontal')
		plt.savefig("finalOutput_plots/precipitationRate/precipitationRate_day" + str(dayLabel) + ".png")
		dayLabel += 1
		plt.cla()
		plt.clf()
		plt.close()
