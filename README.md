# Exploration-on-Spatial-and-Temporal-Locality
CSC 2770 Honors Project on Spatial and Temporal Locality

## Author:

- Simon Glashauser - [Github](https://github.com/sglasha)

## What the project actually analyzes:

The project analyzes the affects of spatial on an array of $size^2$, and a matrix which is a 2D array of $size*size$. It analyzes the affects of temporal locality on an array of size 1 by repeatedly calling it iteratively and recursively.

## Results:

Results can be found in report.pdf, and the graphs created by my test runs can be found in [Graphs](./Graphs). `figure_1` shows how different stride patterns of k affect the time it takes to traverse an array of size $10000^2$, where k is a power of 2 ($2^0$ through $2^9$). `figure_2` shows how row and column wise itteration are affected by spatial locality as the size of the matrix increases from size = $2^5$ to size = $2^{14}$. `figure_3` shows how temporal locality is affected when accessing a single element $2^5$ through $2^{14}$ times.

## How to run the project?

The Project can be fully ran from main.py. When run there are 3 options. Option 1 will generate a single point of data for each test based on the size you input. Option 2 will generate 3 graphs with no user input. Option 3 will terminate the program.
