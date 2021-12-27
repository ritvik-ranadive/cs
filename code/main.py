import netCDF4 as nc
import numpy as np

# Import the data files
# Nitrate
nitrate_file = "../data/nitrate/woa18_all_n00_5d.nc"
nitrate_dataset = nc.Dataset(nitrate_file)
# Oxygen
oxygen_file = "../data/oxygen/woa18_all_o00_5d.nc"
oxygen_dataset = nc.Dataset(oxygen_file)
# Phosphate
phosphate_file = "../data/phosphate/woa18_all_p00_5d.nc"
phosphate_dataset = nc.Dataset(phosphate_file)
# Salinity
salinity_file = "../data/salinity/woa18_decav_s00_5d.nc"
salinity_dataset = nc.Dataset(salinity_file)
# Temperature
temperature_file = "../data/temperature/woa18_decav_t00_5d.nc"
temperature_dataset = nc.Dataset(temperature_file)


# print("Nitrate Values:")
# for var in nitrate_dataset.variables.values():
#     print(var)
#     print("-"*50)
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

latitude = nitrate_dataset["lat"][:]
longitude = nitrate_dataset["lon"][:]
depth = nitrate_dataset["depth"][:]
timestamp = nitrate_dataset["time"][:]
nitrate_value = nitrate_dataset["n_mn"][:]
# for depth_iterator in range(102):
#     for latitude_iterator in range(36):
#         for longitude_iterator in range(72):
#             print("Depth: {0}, Latitude: {1}, Longitude: {2}, Value: {3}".format(depth[depth_iterator], latitude[latitude_iterator], longitude[longitude_iterator], nitrate_value[0, depth_iterator, latitude_iterator, longitude_iterator]))

nitrate_value = nitrate_value[0]
nitrate_map = np.copy(nitrate_value)
nitrate_map[nitrate_map < 100] = 0
nitrate_map[nitrate_map >= 100] = 1
print(np.shape(nitrate_map))
print(np.unique(nitrate_map))
