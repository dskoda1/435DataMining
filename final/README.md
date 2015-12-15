#CS435 Data Mining: Final Project


###Environment

This project needs to be run using Python v3 or higher.
Also, the following libraries need to be available:

`scipy, numpy`


###Usage

Usage information can be obtained by running:

`python3 main.py usage` or just `python3 main.py`

Typical usage is:

`python3 main.py <number of runs to average together> <k value for DCT(optional)>`

The optional k value specified could be:

0: This tells the program to simply select the largest C value from all data points, after performing DCT.

n <- [1..59]: This will add n to the largest C value from DCT, allowing for trial and error testing.


###Description

This assignment focuses on clustering study, and in particular, the K-means method and 
its application to cluster analysis.

1. (50 pts.) Implement the K-means clustering algorithm we have discussed in class. Go 
to http://kdd.ics.uci.edu/databases/synthetic_control/synthetic_control.html
to download the data as well as the documents. Note that there are 600 data points with 6 
classes as the ground truth. Take each data point as a 60 dimensional vector. Then apply 
your implemented K-means algorithm to this data set with the parameter K=6, and 
evaluate your implemented algorithm against the given ground truth. Report your 
clustering accuracy with respect to the ground truth.

2. (50 pts.) Implement the DCT-based dimensionality reduction method and apply your 
implemented method to the whole dataset (of the 600 data points). Now do the following 
error-and-trial test. For a reduced dimensionality value h (h<60), apply your K-means to 
the whole dataset (of the 600 data points) in the h dimensional space, and document the 
accuracy for such a reduced dimensionality value h. What is the minimum such h value 
that the accuracy can still be maintained at least 90%?