# // => I’m competing for BONUS Points <=
import time
from locations import Location

"""
  Homework#5

  Add your name here: Samuel Hieken

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.
"""

# Read a file line by line
# file: Path to file
# preprocess: Function to preprocess each line; strips whitespace by default.
def readFile(file, preprocess = lambda line: line.strip()):
    with open(file, 'r') as f:
        for line in f:
            yield preprocess(line)

if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    # for line in readFile("zipcodes.txt"):
    #     if first:
    #         first = False
    #         continue

    #     columns = line.split("\t")
    #     # print(columns)
    #     print(Location(*columns))

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

