#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin", 
}

#Nesting a List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"], 
    "Germany": ["Berlin", "Hamburg", "Stuttgard"], 
}

# Nesting Dictionary in a Dictionary

travel_log1 = {
    "France": {"visited": ["Paris", "Lille", "Dijon"]}, 
    "Germany": {"visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 12}, 
}


#Nesting Dictionary in a List

travel_log = [
    {"Country": "France", "cities_visited": ["Paris", "Lille", "Dijon"]}, 
    {"Country": "Germany", "visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 12}, 
]

print(travel_log1)


