# HOMEWORK 1

## Problem 1
Solution is provided in the PDF

## Problem 2
Solution is provided in the PDF

## Problem 3
Run the following in a terminal:
```
python3 snowfall.py < input_file
```


## Problem 4
```
python3 matches.py < input_file
```

## Problem 5

### Generate new data
Creates new dataset in and names it in the format `[uniform | normal]_input_<size_of_input>`

It will generate data for n = 100, 1000, 10000, 100000

It will generate data 100 test cases for each case
```
python3 data_generator.py
```

### Sorting

`sortingTest.py` contains the sorting functions

### Validating the sorted output

To validate whether the sorting was correct, you can use the `validate_sequence` funciton in the validator file `validator.py`

### Testig the times
`arr_size` - Set the number of inputs as 100 or 1000 or 10000 or 100000
`data_type` - Set the data type as normal or uniform
Run the file `time_analysis.py` to test all the test cases. It will test 100 test cases for each of n = 100, 1000, 10000, 10000

```
python3 time_analysis.py
```

Since insertion sort takes O(n^2) time, tests for it are not conducted for n > 1000
