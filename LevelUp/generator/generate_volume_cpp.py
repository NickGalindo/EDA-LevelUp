from ctypes import cdll, c_int

run = cdll.LoadLibrary("structures_cpp/libmain.so")
run.createVolume_ref_py.argtypes = [c_int]
run.createVolume_arr_py.argtypes = [c_int]
run.encouple_pair.argtypes = [c_int, c_int]

def runVolumeProtocol_ref(n: int):
    """
    Generate the volume data and run the program console operations
    :param n: the size of data to be generated
    """


def runVolumeProtocol_arr(n: int):
    
