# fraudDetectionML
Find outliers based on users history data. I used data.py to generate some random data, saved it on fixtures.py for
local testing. 
You can override the get_data method so you can work with your own data.   


# How to?
execute the run.py file to see:
- Blue dots - the train data that used.
- Green triangles - test data that the algorithm things is a normal user.
- Red triangles - test data that the algorithm things is NOT a normal user - might be fraud!
- Orange shape - the decision boundary of the algorithm. 

# Example of trained classifier
![alt tag](http://scikit-learn.org/stable/_images/plot_oneclass_001.png)