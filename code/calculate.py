import numpy as np
from import_dataset import import_data, generate_land_map
import cc3d
import folium

northern_hemisphere_season = "winter"
# Import the data
nitrate_dataset, oxygen_dataset, phosphate_dataset, salinity_dataset, temperature_dataset = import_data(northern_hemisphere_season)

# Generate the land map
land_map = generate_land_map(nitrate_dataset)

# Define the data ranges
nitrate_range = [0, 30]
oxygen_range = [0, 100]
phosphate_range = [0, 50]
salinity_range = [0, 70]
temperature_range = [25, 50]
depth_limit = 500

# Extract values for latitudes and longitudes
latitudes_all = nitrate_dataset["lat"][:].tolist()
longitudes_all = nitrate_dataset["lon"][:].tolist()

# Calculate
nitrate_mean_values = nitrate_dataset["n_mn"][0]
oxygen_mean_values = oxygen_dataset["o_mn"][0]
phosphate_mean_values = phosphate_dataset["p_mn"][0]
salinity_mean_values = salinity_dataset["s_mn"][0]
temperature_mean_values = temperature_dataset["t_mn"][0]

# Filtering all the mean value matrices by depth
# Find the index of the depth value provided
depth_values = nitrate_dataset["depth"][:].tolist()
depth_index = depth_values.index(depth_limit)
# print(depth_index)
nitrate_mean_values = nitrate_mean_values[0:depth_index]
oxygen_mean_values = oxygen_mean_values[0:depth_index]
phosphate_mean_values = phosphate_mean_values[0:depth_index]
salinity_mean_values = salinity_mean_values[0:depth_index]
temperature_mean_values = temperature_mean_values[0:depth_index]

# print("Nitrate Value Shape: {0}, Oxygen Value Shape: {1}, Phosphate Value Shape: {2}, Salinity Value Shape:{3}, Temperature Value Shape:{4}".format(np.shape(nitrate_mean_values), np.shape(oxygen_mean_values), np.shape(phosphate_mean_values), np.shape(salinity_mean_values), np.shape(temperature_mean_values)))

# Filtering the nitrate values
nitrate_map = np.copy(nitrate_mean_values)
nitrate_map[nitrate_map < nitrate_range[0]] = 0.0
nitrate_map[nitrate_map > nitrate_range[1]] = 0.0
nitrate_map[nitrate_map != 0] = 1.0
nitrate_map = np.sum(nitrate_map, axis=0)
nitrate_map[nitrate_map != 0.0] = 1.0
nitrate_map = nitrate_map * land_map
print("Nitrate map shape: {0}    Nitrate Map Unique Values: {1}".format(np.shape(nitrate_map), np.unique(nitrate_map)))

# Filtering the nitrate values
oxygen_map = np.copy(oxygen_mean_values)
oxygen_map[oxygen_map < oxygen_range[0]] = 0.0
oxygen_map[oxygen_map > oxygen_range[1]] = 0.0
oxygen_map[oxygen_map != 0.0] = 1.0
oxygen_map = np.sum(oxygen_map, axis=0)
oxygen_map[oxygen_map != 0.0] = 1.0
oxygen_map = oxygen_map * land_map
print("Oxygen map shape: {0}    Oxygen Map Unique Values: {1}".format(np.shape(oxygen_map), np.unique(oxygen_map)))

# Filtering the nitrate values
phosphate_map = np.copy(phosphate_mean_values)
phosphate_map[phosphate_map < phosphate_range[0]] = 0.0
phosphate_map[phosphate_map > phosphate_range[1]] = 0.0
phosphate_map[phosphate_map != 0.0] = 1.0
phosphate_map = np.sum(phosphate_map, axis=0)
phosphate_map[phosphate_map != 0.0] = 1.0
phosphate_map = phosphate_map * land_map
print("Phosphate map shape: {0}    Phosphate Map Unique Values: {1}".format(np.shape(phosphate_map), np.unique(phosphate_map)))

# Filtering the nitrate values
salinity_map = np.copy(salinity_mean_values)
salinity_map[salinity_map < salinity_range[0]] = 0.0
salinity_map[salinity_map > salinity_range[1]] = 0.0
salinity_map[salinity_map != 0.0] = 1.0
salinity_map = np.sum(salinity_map, axis=0)
salinity_map[salinity_map != 0.0] = 1.0
salinity_map = salinity_map * land_map
print("Salinity map shape: {0}    Salinity Map Unique Values: {1}".format(np.shape(salinity_map), np.unique(salinity_map)))

# Filtering the nitrate values
temperature_map = np.copy(temperature_mean_values)
temperature_map[temperature_map < temperature_range[0]] = 0.0
temperature_map[temperature_map > temperature_range[1]] = 0.0
temperature_map[temperature_map != 0.0] = 1.0
temperature_map = np.sum(temperature_map, axis=0)
temperature_map[temperature_map != 0.0] = 1.0
temperature_map = temperature_map * land_map
print("Temperature map shape: {0}    Temperature Map Unique Values: {1}".format(np.shape(temperature_map), np.unique(temperature_map)))

# Generate the intersection of all filtered maps
# overall_map = nitrate_map * oxygen_map * phosphate_map * salinity_map * temperature_map
overall_map = temperature_map
print("Overall map shape: {0}    Overall Map Unique Values: {1}".format(np.shape(overall_map), np.unique(overall_map)))

# Find 3D connected regions in the map
# map_with_regions = cc3d.connected_components(overall_map, connectivity=26)
# print("Region map shape: {0}    Region Map Unique Values: {1}".format(np.shape(map_with_regions), np.unique(map_with_regions)))

# Create a list to store the coordinates
# coordinate_list = []
# for i in range(1, len(np.unique(map_with_regions).tolist())):
#     # print("Depth Indices: ", np.where(map_with_regions == i)[0].tolist())
#     # print("Latitude Indices: ", np.where(map_with_regions == i)[1].tolist())
#     # print("Longitude Indices: ", np.where(map_with_regions == i)[2].tolist())

#     latitude_list = np.where(map_with_regions == i)[1].tolist()
#     start_latitude_index = min(latitude_list)
#     end_latitude_index = max(latitude_list)
#     if start_latitude_index == end_latitude_index and end_latitude_index != (len(latitudes_all)-1):
#         end_latitude_index = start_latitude_index + 1
#     start_latitude = latitudes_all[start_latitude_index]
#     end_latitude = latitudes_all[end_latitude_index]

#     longitude_list = np.where(map_with_regions == i)[2].tolist()
#     start_longitude_index = min(longitude_list)
#     end_longitude_index = max(longitude_list)
#     if start_longitude_index == end_longitude_index and end_longitude_index != (len(longitudes_all)-1):
#         end_longitude_index = start_longitude_index + 1
#     start_longitude = longitudes_all[start_longitude_index]
#     end_longitude = longitudes_all[end_longitude_index]


#     # Check if the region is already marked
#     is_marked = False
#     for coordinates in coordinate_list:
#         if coordinates[0][0] <= start_latitude and coordinates[0][1] <= start_longitude and coordinates[1][0] >= end_latitude and coordinates[1][1] >= end_longitude:
#             is_marked = True
#             break
#     # If the region is not already marked, then mark it
#     if not is_marked:
#         if end_latitude > start_latitude and end_longitude > start_longitude:
#             coordinate_list.append([(start_latitude, start_longitude), (end_latitude, end_longitude)])

# Create a map
# nutrient_map = folium.Map(location=[0.0, 0.0], zoom_start=3)
# for coordinates in coordinate_list:
#     folium.Rectangle(bounds=[(coordinates[0][0], coordinates[0][1]), (coordinates[1][0], coordinates[1][1])], color='#ffff00', fill=True, fill_color='#ffff00', fill_opacity=0.2).add_to(nutrient_map)
# nutrient_map.save("map.html")

nutrient_map = folium.Map(location=[0.0, 0.0], zoom_start=3)
for latitude_index in range(np.shape(overall_map)[0]):
    for longitude_index in range(np.shape(overall_map)[1]):
        if overall_map[latitude_index, longitude_index] == 1.0:
            start_latitude = latitudes_all[latitude_index]
            start_longitude = longitudes_all[longitude_index]
            if latitude_index < len(latitudes_all)-1 and longitude_index < len(longitudes_all)-1:
                end_latitude = latitudes_all[latitude_index + 1]
                end_longitude = longitudes_all[longitude_index + 1]
                folium.Rectangle(bounds=[(start_latitude, start_longitude), (end_latitude, end_longitude)], color='#9AFF33', fill=True, fill_color='#9AFF33', fill_opacity=1).add_to(nutrient_map)
nutrient_map.save("map.html")

