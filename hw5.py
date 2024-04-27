# // => I’m competing for BONUS Points <=
import time
from locations import *

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

def writeFile(file, lines):
    with open(file, 'w') as f:
        for line in lines:
            f.write(line + "\n")

if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    lines = readFile("zipcodes.txt")
    next(lines) # Skip the first line
    locations = [Location(*(line.split("\t"))) for line in lines]

    states = [state for state in readFile("states.txt") if len(state) > 0]
    cities = commonCityNames(locations, states)
    writeFile("CommonCityNames.txt", cities)

    zips = [zipcode for zipcode in filter(lambda zipcode: len(zipcode) > 0, readFile("zips.txt"))]
    latLons = latLon(locations, zips)
    writeFile("LatLon.txt", latLons)

    cities = [city.lower() for city in readFile("cities.txt") if len(city) > 0]
    cityStates = cityStates(locations, cities)
    writeFile("CityStates.txt", cityStates)

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
