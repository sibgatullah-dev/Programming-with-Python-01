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

for key,value in bd_division.items():# indicating the keys and values of the items of the dictionary
    print(key,value)