#Done: import time library and any numpy
import time
import sys
import matplotlib.pyplot as plt
import numpy as np

# Set Recursion limit to 100000
sys.setrecursionlimit(100000)

# Functions
def stop_program():
    print("Exiting...")
    exit()

def generate_array(array_size):
    rng = np.random.default_rng()
    return rng.integers(1, 100, pow(size, 2))

def generate_graph(graph_size):
    return np.random.randint(1, 101, size=(graph_size, graph_size))

def sequential_traversal(array):
    array_access = 0
    time_taken = time.perf_counter()
    for element in array:
        array_access = element
    time_taken = time.perf_counter() - time_taken
    return time_taken

def strided_traversal(array, stride):
    stride = int(stride) # allows for stride to be a float when passed
    array_access = 0
    time_taken = time.perf_counter()
    for i in range(stride):
        for j in range(i, len(array), stride):
            array_access = array[j]
    time_taken = time.perf_counter() - time_taken
    return time_taken

def row_wise_iteration(graph_matrix):
    matrix_access = 0
    time_taken = time.perf_counter()
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[i])):
            matrix_access = graph_matrix[i][j]
    time_taken = time.perf_counter() - time_taken
    return time_taken

def col_wise_iteration(graph_matrix):
    matrix_access = 0
    time_taken = time.perf_counter()
    for i in range(len(graph_matrix[0])):
        for j in range(len(graph_matrix)):
            matrix_access = graph_matrix[j][i]
    time_taken = time.perf_counter() - time_taken
    return time_taken

def itterative_locality(array, times):
    access = 0
    for i in range(times):
        sequential_traversal(array)

def recursive_locality(array, times):
    access = 0
    if times == 0:
        return access
    sequential_traversal(array)
    return recursive_locality(array, times - 1)

#should only be passed row and col wise iteration functions in function
#learned how to pass a function from https://www.geeksforgeeks.org/python/passing-function-as-an-argument-in-python/
def get_average(function, graph_matrix):
    total = 0
    # get a reasonable number of runs to get accurate data in a reasonable amount of time
    if len(graph_matrix) < 512:
        num_runs = 20
    elif len(graph_matrix) < 2048:
        num_runs = 10
    elif len(graph_matrix) < 8192:
        num_runs = 5
    else:
        num_runs = 3

    for run in range(num_runs):
        total += function(graph_matrix)
    return total / num_runs

def get_average_traversal(function, array, stride = None):
    total = 0
    # get a reasonable number of runs to get accurate data in a reasonable amount of time
    if len(array) < pow(2, 20):
        num_runs = 20
    elif len(array) < pow(2, 23):
        num_runs = 10
    elif len(array) < pow(2, 25):
        num_runs = 5
    else:
        num_runs = 3

    if stride is None:
        for run in range(num_runs):
            total += function(array)
        return total / num_runs

    else:
        for run in range(num_runs):
            total += function(array, stride)
        return total / num_runs

def get_recursive_average(function, array, times):
    total = 0
    for i in range(times):
        time_taken = time.perf_counter()
        function(array, times)
        time_taken = time.perf_counter() - time_taken
        total += time_taken
    return total / times

#Done: Generate a nxn array such that each element is a random value as a test case for spatial and temporal locality
#    Allow user to save a .txt file of the array as controlled test data
#    Allow user to import a .json or .txt file to use the premade test data
size = 0
choice = 0
matrix = 0
while choice not in [1, 2, 3]:
    print("Select Analysis Data:\n1. Generate New Data\n2. Generate Graph\n3. Exit")
    choice = int(input())
if choice == 1:
    size = int(input("Size of array to analyze: "))
    array = generate_array(size)
    matrix = generate_graph(size)

if choice == 2:
    arrays = []
    matrices = []
    accesses = []
    array_data = {}
    matrix_data = {}
    test_matrix = []
    starting_size = 5
    num_graph_sizes = 12

    # Generate sample lists for 2^0 - 2^num_graph_sizes
    array = generate_array(10000)
    array_data["Sqrt of Array Size"] = 10000
    array_data["Stride"] = 1
    array_data["Access Time"] = get_average_traversal(sequential_traversal, array)
    arrays.append(array_data)
    array_data = {}
    for stride in range(num_graph_sizes):
        array_data["Sqrt of Array Size"] = 10000
        array_data["Stride"] = pow(2, stride)
        array_data["Access Time"] = get_average_traversal(strided_traversal, array, array_data["Stride"])
        arrays.append(array_data)
        array_data = {}

    # Generate sample graphs for sizes 2^starting_size - 2^starting_size + num_graph_sizes for visual representation through pyplot
    for power in range(num_graph_sizes):
        sized = pow(2, starting_size + power)
        test_matrix = generate_graph(sized)
        matrix_data["Matrix Size"] = sized
        matrix_data["Row Wise Time"] = get_average(row_wise_iteration, test_matrix)
        matrix_data["Col Wise Time"] = get_average(col_wise_iteration, test_matrix)
        matrices.append(matrix_data)
        matrix_data = {} # clear matrix data to prevent bad data

    # Generate Sample Graphs for sizes 2^(starting_size + num_graph_sizes) to 2^(starting_size + 2 * num_graph_sizes)
    for power in range(num_graph_sizes):
        sized = pow(2, starting_size + power)
        test_array = [0]
        array_data["Accesses"] = sized
        array_data["Iterative"] = get_recursive_average(itterative_locality, test_array, sized)
        array_data["Recursive"] = get_recursive_average(recursive_locality, test_array, sized)
        accesses.append(array_data)
        array_data = {} # clear matrix data to prevent bad data

    # Generate Each Pyplot with the data here to reduce wait time because all the data is finished generating

    # Generate Figure 1

    strides = []
    times = []

    for data in arrays:
        strides.append(data["Stride"])
        times.append(data["Access Time"])

    # Show data using pyplot
    plt.plot(strides, times, marker='o', label="Access Time")
    plt.xscale("log", base=2)
    plt.xlabel("Stride Size (n)")
    plt.ylabel("Time (s)")
    plt.title("Sequential vs Stride Access Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Generate Figure 2

    sizes = []
    row_times = []
    col_times = []

    for data in matrices:
        sizes.append(data["Matrix Size"])
        row_times.append(data["Row Wise Time"])
        col_times.append(data["Col Wise Time"])

    # Show data using pyplot
    plt.plot(sizes, row_times, marker='o', label="Row Wise")
    plt.plot(sizes, col_times, marker='s', label="Col Wise")
    plt.xscale("log", base=2)
    plt.xlabel("Matrix Size (n)")
    plt.ylabel("Time (s)")
    plt.title("Row vs Column Wise Traversal Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Generate Figure 3

    sizes = []
    iterative_results = []
    recursive_results = []

    for i in accesses:
        sizes.append(i["Accesses"])
        iterative_results.append(i["Iterative"])
        recursive_results.append(i["Recursive"])

    # Show data using pyplot
    plt.plot(sizes, iterative_results, marker='o', label="Iteration")
    plt.plot(sizes, recursive_results, marker='s', label="Recursion")
    plt.xscale("log", base=2)
    plt.xlabel("Accesses (n)")
    plt.ylabel("Time (s)")
    plt.title("Temporal Locality")
    plt.legend()
    plt.grid(True)
    plt.show()

    # terminates program after pyplots are closed by user
    stop_program()

if choice == 3:
    stop_program()

#Done: Create code that shows sequential vs strided traversal
print(f"Sequential Traversal took {get_average_traversal(sequential_traversal, array)}")
print(f"Strided Traversal took {get_average_traversal(strided_traversal, array, stride = size / 3)}")

#Done: Create code that gives time taken to traverse row wise
print(f"Row Wise Iteration took {get_average(row_wise_iteration, matrix)}")

#Done: Create code that gives time taken to traverse column wise
print(f"Column Wise Iteration took {get_average(col_wise_iteration, matrix)}")

#Done: Create recursive code that accesses one element to demonstrate temporal locality
small_array = [0]
print(f"Access Same Element of Array 10000 times {get_recursive_average(itterative_locality, small_array, 10000)}")
print(f"Recursively Access Same Element of Array 10000 times {get_recursive_average(recursive_locality, small_array, 10000)}")

#Done: Exit once project is finished
stop_program()

