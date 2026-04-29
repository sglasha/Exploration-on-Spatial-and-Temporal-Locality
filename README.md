# Exploration-on-Spatial-and-Temporal-Locality
CSC 2770 Honors Project on Spatial and Temporal Locality

## Author:

- Simon Glashauser - [Github](https://github.com/sglasha)

## What the project actually analyzes:

The project analyzes the affects of spatial on an array of $size^2$, and a matrix which is a 2D array of $size*size$. It analyzes the affects of temporal locality on an array of size 1 by repeatedly calling it iteratively and recursively.

## Results:

Results can be found in the [report](./Report), and the graphs created by my test runs can be found in [Graphs](./Graphs). `figure_1.1` and `figure_1.2` show how different stride patterns of k affect the time it takes to traverse an array of size $10000^2$, where k is a power of 2 ($2^0$ through $2^{11}$) for `figure_1.2`. `figure_2.1` and `figure_2.2` show how row and column wise itteration are affected by spatial locality as the size of the matrix increases from size = $2^5$ to size = $2^{16}$ for `figure_2.2`. `figure_3.1` and `figure_2.3` shows how temporal locality affects the access time (the average time) to access each element n times where n is $2^5$ through $2^{16}$ times in `figure_3.2`.

## How to run the project?

The Project can be fully ran from main.py. When run there are 3 options. Option 1 will generate a single point of data for each test based on the size you input. Option 2 will generate 3 graphs with no user input. When these graphs are generated you need to close them to have the program continue and calculate the next graph. Option 3 will terminate the program. The `num_graph_sizes` variable on line 141 should be changed from 12 to a number below 10 if you would like the program to run in less than a few hours, since it took over 10 minutes to run at that size. If you increase the `num_graph_sizes` variable, you need to increase the max recursion limit on line 8 because the program needs a recursion limit of at least $2^{5 + num-graph-sizes}$ to be able to calculate and display graph 3.
