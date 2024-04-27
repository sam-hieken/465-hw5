class Record:
    def __init__(self, id):
        self.id = id

class Location(Record):
    # Fields: Zipcode	ZipCodeType	City	State	LocationType	Lat	Long	Xaxis	Yaxis	Zaxis	WorldRegion	Country	LocationText	Location	Decommisioned	TaxReturnsFiled	EstimatedPopulation	TotalWages	Notes
    def __init__(self, *columns):
        super().__init__(columns[0])
        self.zipcode = columns[1]
        self.zipcode_type = columns[2]
        self.city = columns[3]
        self.state = columns[4]
        self.location_type = columns[5]
        self.lat = columns[6]
        self.long = columns[7]
        self.xaxis = columns[8]
        self.yaxis = columns[9]
        self.zaxis = columns[10]
        self.world_region = columns[11]
        self.country = columns[12]
        self.location_text = columns[13]
        self.location = columns[14]
        self.decommissioned = columns[15]

        if len(columns) > 16:
            self.tax_returns_filed = columns[16]
        else:
            self.tax_returns_filed = None 
        
        if len(columns) > 17:
            self.estimated_population = columns[17]
        else:
            self.estimated_population = None
            
        if len(columns) > 18:
            self.total_wages = columns[18]
        else:
            self.total_wages = None

        if len(columns) > 19:    
            self.notes = columns[19]
        else:
            self.notes = None
    
    # To String
    def __str__(self):
        # Format: Location(property=value, property=value, ...)
        return f"Location({self.__dict__})"