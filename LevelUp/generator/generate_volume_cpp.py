import time
from ctypes import cdll, c_longlong, c_int

run = cdll.LoadLibrary("structures_cpp/libmain.so")
run.createVolume_ref_py.argtypes = [c_int]
run.createVolume_arr_py.argtypes = [c_int]
run.encouple_pair.argtypes = [c_int, c_int]

def runVolumeProtocol():
    """
    Generate the volume data and run the program console operations qith linked list in reference implementation
    """

    try:
        N = int(input("What size data would you like to generate?\n"))
        if N > 1000000000 or N<0:
            raise Exception()
    except:
        print("Invalid input, reload page if you desire to continue operation")
        return False

    try:
        TP = int(input("1. Reference LinkedList\n2. Array LinkedList\n"))
        if TP < 1 or TP > 2:
            raise Exception()
    except:
        print("Invalid input, reload page if you desire to continue operation")
        return False

    linked_list = None

    start_time = time.perf_counter()
    if TP == 1:
        linked_list = run.createVolume_ref_py(N)
    else:
        linked_list = run.createVolume_arr_py(N)
    end_time = time.perf_counter()

    print(f"Data generated in linked_list in {end_time-start_time:0.4f} seconds")

    stay = True

    while stay:
        try:
            OP = int(input("1. Retrieve a workout volume analysis\n2. Add a new workout volume analysis\n3. Delete a workout volume analysis\n4. Leave\n"))
            if OP > 4 or OP < 1:
                raise Exception()
        except:
            run.delete_linkedlist(linked_list)
            print("Invalid input, asumed quit for memory safety reload page if you desire to continue operation")
            return False

        if OP == 4:
            stay = False
            continue

        if OP == 1:
            try:
                QUERY = int(input("Which position (index) would you like to retrieve?\n"))
                size = run.linkedlist_size(linked_list)
                if QUERY < 0 or QUERY >= size:
                    raise Exeption()
            except:
                print("Invalid input, please try again")
                continue

            start_time = time.perf_counter()
            ret_pair_pp = run.get_py(linked_list, QUERY)
            end_time = time.perf_counter()

            first_val = run.decouple_pair_first(ret_pair_pp)
            second_val = run.decouple_pair_second(ret_pair_pp)
            print("Workout_id:", first_val, end=" ")
            print("Volume:", second_val)
            print(f"Get operation finished in {end_time-start_time:0.4f} seconds")
            continue

        if OP == 2:
            try:
                QUERY_ID = int(input("What should the new workout_id be?\n"))
                QUERY_VOL = int(input("What is the total volume?\n"))
            except:
                print("Invalid input, please try again")
                continue

            coupled_pair = run.encouple_pair(QUERY_ID, QUERY_VOL)

            start_time = time.perf_counter()
            run.push_back_py(linked_list, coupled_pair)
            end_time = time.perf_counter()

            print("Workout_id, Volume added successfully")
            print(f"Push_back operation finished in {end_time-start_time:0.4f} seconds")
            continue

        if OP == 3:
            try:
                QUERY = int(input("Which position (index) would you like to delete?\n"))
                if QUERY < 0 or QUERY >= run.linkedlist_size(linked_list):
                    raise Exeption()
            except:
                print("Invalid input, please try again")
                continue

            start_time = time.perf_counter()
            run.remove_py(linked_list, QUERY)
            end_time = time.perf_counter()

            print(f"Remove operation finished in {end_time-start_time:0.4f} seconds")
            continue

    run.delete_linkedlist(linked_list)

    print("Goodbye :(")
    return True


if __name__ == "__main__":
    runVolumeProtocol()
