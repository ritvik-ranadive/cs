import numpy as np
from import_dataset import import_data

nitrate_dataset, oxygen_dataset, phosphate_dataset, salinity_dataset, temperature_dataset = import_data()

########################################################################################################################
# Verify if the matrices that contain the actual values of the means have the same dimensions
nitrate_mean_values = nitrate_dataset["n_mn"]
oxygen_mean_values = oxygen_dataset["o_mn"]
phosphate_mean_values = phosphate_dataset["p_mn"]
salinity_mean_values = salinity_dataset["s_mn"]
temperature_mean_values = temperature_dataset["t_mn"]
print("Nitrate Value Shape: {0}, Oxygen Value Shape: {1}, Phosphate Value Shape: {2}, Salinity Value Shape:{3}, Temperature Value Shape:{4}".format(np.shape(nitrate_mean_values), np.shape(oxygen_mean_values), np.shape(phosphate_mean_values), np.shape(salinity_mean_values), np.shape(temperature_mean_values)))
########################################################################################################################
########################################################################################################################
# Check if the values of the values of latitudes are the same
# latitude_nitrate = nitrate_dataset["lat"][:]
# latitude_oxygen = oxygen_dataset["lat"][:]
# latitude_phosphate = phosphate_dataset["lat"][:]
# latitude_salinity = salinity_dataset["lat"][:]
# latitude_temperature = temperature_dataset["lat"][:]
# for i in range(np.shape(latitude_nitrate)[0]):
#     if latitude_nitrate[i] == latitude_oxygen[i] == latitude_phosphate[i] == latitude_salinity[i] == latitude_temperature[i]:
#         print("Good: ", i, latitude_nitrate[i], latitude_oxygen[i], latitude_phosphate[i], latitude_salinity[i], latitude_temperature[i])
#     else:
#         print("Bad: ", i, latitude_nitrate[i], latitude_oxygen[i], latitude_phosphate[i], latitude_salinity[i], latitude_temperature[i])
########################################################################################################################
########################################################################################################################
# Check whether the values of the longitudes are the same
# longitude_nitrate = nitrate_dataset["lon"][:]
# longitude_oxygen = oxygen_dataset["lon"][:]
# longitude_phosphate = phosphate_dataset["lon"][:]
# longitude_salinity = salinity_dataset["lon"][:]
# longitude_temperature = temperature_dataset["lon"][:]
# for i in range(np.shape(longitude_nitrate)[0]):
#     if longitude_nitrate[i] == longitude_oxygen[i] == longitude_phosphate[i] == longitude_salinity[i] == longitude_temperature[i]:
#         print("Good: ", i, longitude_nitrate[i], longitude_oxygen[i], longitude_phosphate[i], longitude_salinity[i], longitude_temperature[i])
#     else:
#         print("Bad: ", i, longitude_nitrate[i], longitude_oxygen[i], longitude_phosphate[i], longitude_salinity[i], longitude_temperature[i])
########################################################################################################################
########################################################################################################################
# Check whether the values of the depths are the same
# depth_nitrate = nitrate_dataset["depth"][:]
# depth_oxygen = oxygen_dataset["depth"][:]
# depth_phosphate = phosphate_dataset["depth"][:]
# depth_salinity = salinity_dataset["depth"][:]
# depth_temperature = temperature_dataset["depth"][:]
# for i in range(np.shape(depth_nitrate)[0]):
#     if depth_nitrate[i] == depth_oxygen[i] == depth_phosphate[i] == depth_salinity[i] == depth_temperature[i]:
#         print("Good: ", i, depth_nitrate[i], depth_oxygen[i], depth_phosphate[i], depth_salinity[i], depth_temperature[i])
#     else:
#         print("Bad: ", i, depth_nitrate[i], depth_oxygen[i], depth_phosphate[i], depth_salinity[i], depth_temperature[i])
########################################################################################################################

print("Nitrate Values:")
for var in nitrate_dataset.variables.values():
    print(var)
    print("-"*50)
# <class 'netCDF4._netCDF4.Variable'>
# float32 n_mn(time, depth, lat, lon)
#     standard_name: moles_concentration_of_nitrate_in_sea_water
#     long_name: Average of all unflagged interpolated values at each standard depth level for moles_concentration_of_nitrate_in_sea_water in each grid-square which contain at least one measurement.
#     coordinates: time lat lon depth
#     cell_methods: area: mean depth: mean time: mean within years time: mean over years
#     grid_mapping: crs
#     units: micromoles_per_kilogram
#     _FillValue: 9.96921e+36
# unlimited dimensions:
# current shape = (1, 102, 36, 72)
# filling on
# for depth_iterator in range(102):
#     for latitude_iterator in range(36):
#         for longitude_iterator in range(72):
#             print("Depth: {0}, Latitude: {1}, Longitude: {2}, Value: {3}".format(depth[depth_iterator], latitude[latitude_iterator], longitude[longitude_iterator], nitrate_value[0, depth_iterator, latitude_iterator, longitude_iterator]))



# (27, -106), (22, -100)
# latitude -> 111 to 117
# longitude -> 73 to 80
# print(temperature_mean_values[0,0:10,111:117,73:80])

print("Max and Min Values:")
print("Nitrate: ", np.max(nitrate_mean_values), np.min(nitrate_mean_values))
print("Oxygen: ", np.max(oxygen_mean_values), np.min(oxygen_mean_values))
print("Phosphate: ", np.max(phosphate_mean_values), np.min(phosphate_mean_values))
print("Salinity: ", np.max(salinity_mean_values), np.min(salinity_mean_values))
print("Temperature: ", np.max(temperature_mean_values), np.min(temperature_mean_values))
