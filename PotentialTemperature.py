import numpy as np
from netCDF4 import Dataset
from PIL import Image
from matplotlib import pyplot as plt

def generate_potentialTemperature(year,month,date,monthConversion):
	potentialTemperature_rate = Dataset("datasets/ptrate.atms.gauss." + str(year) + ".nc","r",format="NETCDF4")
	ptrate = np.array(potentialTemperature_rate.variables['ptrate'])
	# Month conversion to 365-day scale + leap year correction
	if len(ptrate) == 366:
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
	ptrate = ptrate[newDate-3:newDate+4]
	np.save("outData/ptrate_7day_atms_7x2.5x2.5",ptrate)
	return 0.

def plot_potentialTemperatureRate(err):
	ptrateData = np.load("outData/ptrate_7day_atms_7x2.5x2.5.npy")
	x = np.linspace(0,90,num=4,endpoint=True)
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))]
	y = np.linspace(0,93,num=7,endpoint=True)
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))]
	im = Image.open("globalMap.png")
	dayLabel = 1
	for dailyProfile in ptrateData:
		fig = plt.figure()
		ax = plt.axes()
		plt.imshow(im,extent=[0,90,0,93])
		plt.xlabel("Latitude")
		plt.ylabel("Pressure")
		plt.xticks(x,xLabels)
		plt.yticks(y,yLabels)
		cs =  ax.contourf(dailyProfile,alpha=0.6)
		plt.colorbar(cs, ax=ax, label="Potential Temperature Rate (%)", orientation='horizontal')
		plt.savefig("finalOutput_plots/potentialTemperatureRate/potentialTemperatureRate_day" + str(dayLabel) + ".png")
		dayLabel += 1
		plt.cla()
		plt.clf()
		plt.close()


