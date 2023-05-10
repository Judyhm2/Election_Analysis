counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

#For Loop iteration
for county in counties:
    print(county)

#Range that simplifies for loop
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

#For indexing through the counties list
for i in range(len(counties)):
    print(counties[i])

#For iterating a tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for county in counties_tuple:
    print(county)

# Iterating through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

# Using the keys() method to iterate over a dictionary to get the keys
for county in counties_dict.keys():
    print(county)

# Iterating over the dictionary using the values() method
for voters in counties_dict.values():
    print(voters)

# For getting values in dictionary
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# For getting the key-value pairs of a dictionary using the items() method
for county, voters in counties_dict.items():
    print(county, voters)


# Iterate Through a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# Get the Values from a List of Dictionaries using nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

# Prining the name of the county keys
for county_dict in voting_data:
    print(county_dict['county'])

# F-strings: Formatted String Literals
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes *100}% of the total votes.")


# Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Better Use of F-Strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

# voting_data = (f{"county":"Arapahoe", "registered_voters": 422829:,}, f{"county":"Denver", "registered_voters": 463353:,}, f{"county":"Jefferson", "registered_voters": 432438:,})
