country = "Brazil" # country name
visits = 2 # Number of visits
list_of_cities = ["Sao Paulo", "Rio de Janeiro"] #  list from formatted string

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

# Function that will allow new countries to be added to the travel_log. 

def add_new_country(name, visit_number, visited_cities):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_number
  new_country["cities"] = visited_cities
  travel_log.append(new_country)
  
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")