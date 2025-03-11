import h5py

try:
    with h5py.File('xgb_model (1).pkl', 'r') as f:
        print("File is valid HDF5 file")
except OSError:
    print("File is not a valid HDF5 file or it is corrupted")