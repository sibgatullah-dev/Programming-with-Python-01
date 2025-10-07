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

district = 0
upazila = 0
union = 0

for division in bd_division.keys():
    district += bd_division[division]["district"]
    upazila += bd_division[division]["upazila"]
    union += bd_division[division]["union"]
    
print("Total Districts: ",district)
print("Total Upazilas : ",upazila)
print("Total Unions   : ",union)
    