import netCDF4 as nc
from global_land_mask import globe
import numpy as np

# Import the data files
def import_data():
    # Nitrate
    nitrate_file = "../data/nitrate/woa18_all_n00_01.nc"
    nitrate_dataset = nc.Dataset(nitrate_file)
    # Oxygen
    oxygen_file = "../data/oxygen/woa18_all_o00_01.nc"
    oxygen_dataset = nc.Dataset(oxygen_file)
    # Phosphate
    phosphate_file = "../data/phosphate/woa18_all_p00_01.nc"
    phosphate_dataset = nc.Dataset(phosphate_file)
    # Salinity
    salinity_file = "../data/salinity/woa18_decav_s00_01.nc"
    salinity_dataset = nc.Dataset(salinity_file)
    # Temperature
    temperature_file = "../data/temperature/woa18_decav_t00_01.nc"
    temperature_dataset = nc.Dataset(temperature_file)
    return nitrate_dataset, oxygen_dataset, phosphate_dataset, salinity_dataset, temperature_dataset


def generate_land_map(nitrate_dataset):
    # Get the values of the latitudes and longitudes
    latitudes_all = nitrate_dataset["lat"][:].tolist()
    longitudes_all = nitrate_dataset["lon"][:].tolist()
    # print(latitudes_all[111:117])
    # print(longitudes_all[73:80])
    
    # Create a map to hold the land mass map
    land_map = np.ones((len(latitudes_all), len(longitudes_all)))
    for latitude in range(np.shape(land_map)[0]):
        for longitude in range(np.shape(land_map)[1]):
            if globe.is_land(latitudes_all[latitude], longitudes_all[longitude]):
                land_map[latitude, longitude] = 0.0
    # land_map[land_map != 0.0] = 1.0
    # print("Shape: {0}, Unique Values:{1}".format(np.shape(land_map), np.unique(land_map)))
    # print(land_map[0:10,111:117:,73:80])
    land_map = np.flip(land_map, 0)
    # np.savetxt("land.csv", land_map, delimiter=",")

    return land_map



# nitrate_file = "../data/nitrate/woa18_all_n00_01.nc"
# nitrate_dataset = nc.Dataset(nitrate_file)
# generate_land_map(nitrate_dataset)