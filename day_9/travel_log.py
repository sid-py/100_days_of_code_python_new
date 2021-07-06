travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, visits, cities):
    add_entry = {}
    add_entry["country"] = country_visited
    add_entry["visits"] = visits
    add_entry["cities"] = cities
    travel_log.append(add_entry)
    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Spain", 2, ["Barcelona, Madrid"])
print(travel_log)