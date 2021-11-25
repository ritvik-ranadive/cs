import netCDF4 as nc

phosphate_file = "data/phosphate/woa18_all_p00_01.nc"
phosphate_dataset = nc.Dataset(phosphate_file)

nitrate_file = "data/nitrate/woa18_all_n00_01.nc"
nitrate_dataset = nc.Dataset(nitrate_file)

# print("Phosphate Dimensions:")
# for dim in phosphate_dataset.dimensions.values():
#     print(dim)

# print("Nitrate Dimensions:")
# for dim in nitrate_dataset.dimensions.values():
#     print(dim)

# print("Phosphate Values:")
# for var in phosphate_dataset.variables.values():
#     print(var)
#     print("-"*50)

print("Nitrate Values:")
for var in nitrate_dataset.variables.values():
    print(var)
    print("-"*50)

# latitude = phosphate_dataset["lat"][:]
# longitude = phosphate_dataset["lon"][:]
# depth = phosphate_dataset["depth"][:]
# timestamp = phosphate_dataset["time"][:]

# <class 'netCDF4._netCDF4.Variable'>
# float32 p_an(time, depth, lat, lon)
#     standard_name: moles_concentration_of_phosphate_in_sea_water
#     long_name: Objectively analyzed mean fields for moles_concentration_of_phosphate_in_sea_water at standard depth levels.
#     coordinates: time lat lon depth
#     cell_methods: area: mean depth: mean time: mean within years time: mean over years
#     grid_mapping: crs
#     units: micromoles_per_kilogram
#     _FillValue: 9.96921e+36
# unlimited dimensions:
# current shape = (1, 102, 180, 360)
# filling on
# phosphate_value = phosphate_dataset["p_an"][:]

# print("Latitude: {0}  Longitude: {1}  Depth: {2}  Timestamp: {3}".format(len(latitude), len(longitude), len(depth), len(timestamp)))
# print(latitude)
# print(longitude)
# print(depth)
# print(timestamp)
# print(phosphate_value[:, 100, 100, 99])

# for dep in range(102):
#     for lat in range(180):
#         for longt in range(360):
#             print("Depth: {0}, Latitude: {1}, Longitude: {2}, Value: {3}".format(depth[dep], latitude[lat], longitude[longt], phosphate_value[0, dep, lat, longt]))

# indices = [[dep, lat, longt] for dep in range(102) for lat in range(180) for longt in range(360) if phosphate_value[0, dep, lat, longt] > 2.5]
# print(indices)


latitude = nitrate_dataset["lat"][:]
longitude = nitrate_dataset["lon"][:]
depth = nitrate_dataset["depth"][:]
timestamp = nitrate_dataset["time"][:]

# <class 'netCDF4._netCDF4.Variable'>
# float32 n_an(time, depth, lat, lon)
#     standard_name: moles_concentration_of_nitrate_in_sea_water
#     long_name: Objectively analyzed mean fields for moles_concentration_of_nitrate_in_sea_water at standard depth levels.
#     coordinates: time lat lon depth
#     cell_methods: area: mean depth: mean time: mean within years time: mean over years
#     grid_mapping: crs
#     units: micromoles_per_kilogram
#     _FillValue: 9.96921e+36
# unlimited dimensions:
# current shape = (1, 102, 180, 360)
# filling on
nitrate_value = nitrate_dataset["n_an"][:]

for dep in range(102):
    for lat in range(180):
        for longt in range(360):
            print("Depth: {0}, Latitude: {1}, Longitude: {2}, Value: {3}".format(depth[dep], latitude[lat], longitude[longt], nitrate_value[0, dep, lat, longt]))
