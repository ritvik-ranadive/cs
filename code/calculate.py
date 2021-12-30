import numpy as np
from import_dataset import import_data
import cc3d

# Import the data
nitrate_dataset, oxygen_dataset, phosphate_dataset, salinity_dataset, temperature_dataset = import_data()

# Define the data ranges
nitrate_range = [0, 100]
oxygen_range = [0, 100]
phosphate_range = [0, 100]
salinity_range = [0, 100]
temperature_range = [20, 50]
depth_limit = 500

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
nitrate_map[nitrate_map < nitrate_range[0]] = 0
nitrate_map[nitrate_map > nitrate_range[1]] = 0
nitrate_map[nitrate_map != 0] = 1
print("Nitrate map shape: {0}    Nitrate Map Unique Values: {1}".format(np.shape(nitrate_map), np.unique(nitrate_map)))

# Filtering the nitrate values
oxygen_map = np.copy(oxygen_mean_values)
oxygen_map[oxygen_map < oxygen_range[0]] = 0
oxygen_map[oxygen_map > oxygen_range[1]] = 0
oxygen_map[oxygen_map != 0] = 1
print("Oxygen map shape: {0}    Oxygen Map Unique Values: {1}".format(np.shape(oxygen_map), np.unique(oxygen_map)))

# Filtering the nitrate values
phosphate_map = np.copy(phosphate_mean_values)
phosphate_map[phosphate_map < phosphate_range[0]] = 0
phosphate_map[phosphate_map > phosphate_range[1]] = 0
phosphate_map[phosphate_map != 0] = 1
print("Phosphate map shape: {0}    Phosphate Map Unique Values: {1}".format(np.shape(phosphate_map), np.unique(phosphate_map)))

# Filtering the nitrate values
salinity_map = np.copy(salinity_mean_values)
salinity_map[salinity_map < salinity_range[0]] = 0
salinity_map[salinity_map > salinity_range[1]] = 0
salinity_map[salinity_map != 0] = 1
print("Salinity map shape: {0}    Salinity Map Unique Values: {1}".format(np.shape(salinity_map), np.unique(salinity_map)))

# Filtering the nitrate values
temperature_map = np.copy(temperature_mean_values)
temperature_map[temperature_map < temperature_range[0]] = 0
temperature_map[temperature_map > temperature_range[1]] = 0
temperature_map[temperature_map != 0] = 1
print("Temperature map shape: {0}    Temperature Map Unique Values: {1}".format(np.shape(temperature_map), np.unique(temperature_map)))

# Generate the intersection of all filtered maps
overall_map = nitrate_map * oxygen_map * phosphate_map * salinity_map * temperature_map
print("Overall map shape: {0}    Overall Map Unique Values: {1}".format(np.shape(overall_map), np.unique(overall_map)))

# Find 3D connected regions in the map
map_with_regions = cc3d.connected_components(overall_map)
print("Region map shape: {0}    Region Map Unique Values: {1}".format(np.shape(map_with_regions), np.unique(map_with_regions)))