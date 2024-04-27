class Record:
    def __init__(self, id):
        self.id = id

class Location(Record):
    # Fields: Zipcode	ZipCodeType	City	State	LocationType	Lat	Long	Xaxis	Yaxis	Zaxis	WorldRegion	Country	LocationText	Location	Decommisioned	TaxReturnsFiled	EstimatedPopulation	TotalWages	Notes
    def __init__(self, *columns):
        super().__init__(int(columns[0]))
        self.zipcode = columns[1]
        self.zipcode_type = columns[2]
        self.city = columns[3]
        self.state = columns[4]
        self.location_type = columns[5]

        if len(columns[6]) > 0:
            self.lat = float(columns[6])
        else:
            self.lat = None

        if len(columns[7]) > 0:
            self.long = float(columns[7])
        else:
            self.long = None
        
        self.yaxis = float(columns[9])
        self.zaxis = float(columns[10])
        self.world_region = columns[11]
        self.country = columns[12]
        self.location_text = columns[13]
        self.location = columns[14]
        self.decommissioned = columns[15].lower() == "true"

        if len(columns) > 16 and len(columns[16]) > 0:
            self.tax_returns_filed = int(columns[16])
        else:
            self.tax_returns_filed = None 
        
        if len(columns) > 17 and len(columns[17]) > 0:
            self.estimated_population = int(columns[17])
        else:
            self.estimated_population = None
            
        if len(columns) > 18 and len(columns[18]) > 0:
            self.total_wages = int(columns[18])
        else:
            self.total_wages = None

        if len(columns) > 19 and len(columns[19]) > 0:    
            self.notes = columns[19]
        else:
            self.notes = None
    
    # To String
    def __str__(self):
        # Format: Location(property=value, property=value, ...)
        return f"Location({self.__dict__})"
    
    # Overload >
    def __gt__(self, other):
        if self.estimated_population is None or other.estimated_population is None:
            return None
        
        return self.estimated_population > other.estimated_population
    
    # Overload <
    def __lt__(self, other):
        if self.estimated_population is None or other.estimated_population is None:
            return None
        
        return self.estimated_population < other.estimated_population
    
# locations: The locations to check
# states: The states to find common city names between. Can be a list or set, though set is preferred for speed.
def commonCityNames(locations, states):
    # Map of cities to (set of) states
    city_dict = {}
    common_cities = set()
    for location in locations:
        city = location.city
        if location.state in states:
            if city not in city_dict:
                city_dict[city] = set()
            
            city_dict[city].add(location.state)

            # Check if the city's states match the states passed to the function
            # Since we're only adding states from the passed set, the length is more than enough to compare
            if len(city_dict[city]) == len(states):
                common_cities.add(city)
    
    # Return common cities in a sorted list
    return sorted(list(common_cities))

# locations: The locations to check
# zipcodes: The zipcodes to return the lat/lon for
# Returns: A list of strings corresponding to each zipcode in zipcodes, where the string is the lat/lon of the zipcode
def latLon(locations, zipcodes):
    zipcodes_found = {}

    for location in locations:
        zip = location.zipcode
        # Don't care about this zipcode, or already found it
        if zip not in zipcodes or zip in zipcodes_found:
            continue
        
        zipcodes_found[zip] = f"{location.lat} {location.long}"

        # Short circuit if we found all the zipcodes
        if len(zipcodes_found) == len(zipcodes):
            break
    
    # Return the values from zipcodes_found in the order the zipcodes were provided
    # in the list 
    return [zipcodes_found[zip] for zip in zipcodes]

# locations: The locations to check
# cities: The cities to return the states for
# Returns: A list of strings corresponding to each city in cities, where the string is each state having said city in alphabetical order
def cityStates(locations, cities):
    city_dict = {}

    for location in locations:
        city = location.city.lower()
        if city not in cities:
            continue

        elif city not in city_dict:
            city_dict[city] = set()
        
        city_dict[city].add(location.state)
    
    return [" ".join(sorted(list(city_dict[city]))) for city in cities]