[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=web-on-v3)](https://travis-ci.org/travis-ci/travis-web)

##Command line usage:

For standard usage:
  
    python3 hw2.py <Training population size in %>
  
Optional usage: Specify how many trials you would like to test
  
    python3 hw2.py <Training population size in %> <# of tests to run>
  
Even more optional usage: Specify the regular execution, or functional code execution
  
    python3 hw2.py <Training population size in %> <# of tests to run> <0 for regular mode; 1 for functional mode>
    
#####(functional mode still being worked on)



##Description of assignment:


This assignment is about studying data classification. Specifically, we study the Naïve Bayesian Classifier. Go to the following link to download the “adult” dataset:

http://archive.ics.uci.edu/ml/datasets/Adult

This is a dataset with people of different attributes (14 attributes) and the task is to classify whether an individual earns salary > $50K. There are in total 48842 data items.

1.	(10 pts.) Clean up the Adult dataset by removing all the data items with incomplete attributes. The cleaned up dataset will be used as the original dataset in the rest of the assignment.

2.	(30 pts.) Implement a sampling function that takes a stratified sampling of X percentage of the total number of data items in proportion to the total number of positive samples and the total number of negative samples in the dataset. Apply your function to Adult dataset to generate three different training datasets as 10%, 30%, and 50% of the original dataset, respectively.

3.	(60 pts.) Implement the Naïve Bayesian Classifier given a training dataset and an input sample. For each of the training dataset obtained in 2, the rest dataset is considered as the testing dataset. For each obtained training dataset, randomly pick up 20 data items from the testing dataset; for each testing data item, apply your Naïve Bayesian Classifier to compute whether the individual earns >$50K or not; then compare the returned result from your classifier with the given label of that individual; if the returned result agrees with the given label, it is considered as a correct result; otherwise, an incorrect result; finally, an accuracy is computed as the percentage of the total number of the correct results out of 20. Discuss the classification accuracies for all the three different training datasets.



  


