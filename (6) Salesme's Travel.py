import re

def travel(r, zipcode):

    #splits the addresses on the comma
    addresses = r.split(",")
    
    #list variables
    records = []
    streets = []
    houses = []
    
    #creates a loop to go through addresses
    for x in addresses:
        addr = re.search(r"(^\d+) ([a-zA-z.\s]+) ([A-Z]{2} \d+)$", x)
        records.append({"house": addr.group(1), "street": addr.group(2), "zip": addr.group(3)
        })

    #creates a loop to go through records
    for r in records:
        if (r["zip"] == zipcode):
            streets.append(r["street"])
            houses.append(r["house"])
                    
    return "{}:{}/{}".format(zipcode, ",".join(streets), ",".join(houses))
