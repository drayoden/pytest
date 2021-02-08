# people = [
#     {
#         "given_name": "Alfonsa",
#         "family_name": "Ruiz",
#         "title": "Senior Software Engineer",
#     },
#     {
#         "given_name": "Sayid",
#         "family_name": "Khan",
#         "title": "Project Manager",
#     },
# ]

def format_data_for_display(people):
    display = []
    for i in people:
        display.append(i["given_name"] + " " + i["family_name"] + ": " + i["title"])
    return display


# print(format_data_for_display(people))

def test_format_data_for_display():
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]