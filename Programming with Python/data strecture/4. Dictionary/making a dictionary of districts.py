bd_division = {}
bd_division["Barisal"]={
    "district": 6,
    "upazila": 39,
    "union":333
}
bd_division["Chittagong"]={
    "district": 11,
    "upazila": 97,
    "union":336
}
bd_division["Dhaka"]={
    "district": 13,
    "upazila": 93,
    "union":1833
}
bd_division["Khulna"]={
    "district": 10,
    "upazila": 59,
    "union":270
}
bd_division["Mymensingh"]={
    "district": 4,
    "upazila": 34,
    "union":350
}
bd_division["Rajshahi"]={
    "district": 8,
    "upazila": 70,
    "union":558
}
bd_division["Rangpur"]={
    "district": 8,
    "upazila": 58,
    "union":536
}
bd_division["Sylhet"]={
    "district": 4,
    "upazila": 38,
    "union":334
}

print(bd_division)
print('\t')

# Now if we want to print the name of the district name we can use .keys() method 
# since the district names are keys so the .keys() method will print the keys which is the name of the districts
divisions = bd_division.keys()
for division in divisions:
    print("Division: ",division,"Upazilas: ",bd_division[division]["upazila"],"Union: ",bd_division[division]['union'],"District: ",bd_division[division]['district'])
    
    
# if we launch a loop on a dictionary we will only get the keys
for division in divisions:
    print(division)