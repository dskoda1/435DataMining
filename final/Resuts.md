##Trial and Error testing of DCT 

####Results

The K-Means algorithm produces an accuracy of ~66% with respect to the ground truth.

####Task:

For a reduced dimensionality value h (h<60), apply your K-means to the whole dataset 
(of the 600 data points) in the h dimensional space, and document the accuracy for such 
a reduced dimensionality value h. What is the minimum such h value that the accuracy 
can still be maintained at least 90%? Edit: 90% of accuracy from Q1.

All of the below results are from averaging 5 different runs together.

Table starts at an h-value of 7 because that is the value obtained through DCT. 

h-value | Accuracy %
--------|------------
7 | 42.9
10 | 51.5
11 | 54.2
12 | 56.2
13 | 58.4
14 | 60.2
15 | 62.1
20 | 64.0
25 | 65.6
30 | 66.6
35 | 67.8
40 | 67.2
45 | 69.8
50 | 70.3
55 | 66.0
60 | 65.7

#####Analysis

After analysis of the above data, you can see that an h-val of 13-14 produces the desired 90% 
of the accuracy of Q1, which was 65.7% for all 60 attributes. 