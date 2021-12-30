import netCDF4 as nc


# Import the data files
def import_data():
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
    return nitrate_dataset, oxygen_dataset, phosphate_dataset, salinity_dataset, temperature_dataset
