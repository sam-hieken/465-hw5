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
    
