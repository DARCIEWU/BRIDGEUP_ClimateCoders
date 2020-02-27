#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2013.nc')

	#
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	print(lon.shape) #720
	print(lat.shape) #330
	print(time.shape) #12
	print(depth.shape) #50
	print(temp.shape) #12, 50, 330, 720
	print(salt.shape) #12, 2, 330, 720

	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]
	print(temp_sliced.shape)

	
	temp_mean = temp_sliced.mean()
	

	temp_anom = temp[:,condition_depth,:,:] - temp_mean
	print(temp_anom.shape)
	temp_anom_yr = temp_anom.mean(axis = 0)
	print(temp_anom_yr.shape)
	temp_anom_ = temp_anom_yr.mean(axis = 0)
	print(temp_anom_.shape)


	print(temp_anom_yr.mean)
	print(temp_anom_yr.shape)

#Execute main script
if __name__ == '__main__':
	main()

