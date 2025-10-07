marks = {
    "Rahim":{
        "Bangla":74,
        "English":73,
        "Math":71
    },
    "Kahim":{
        "Bangla":78,
        "English":63,
        "Math":70
    },
    "Salim":{
        "Bangla":79,
        "English":78,
        "Math":81
    },
}
name = input("Enter your name: ")
sub = input("Enter your subject: ")

print(marks[name][sub])