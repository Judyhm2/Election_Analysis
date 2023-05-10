# Election_Analysis
## Deliverable 1
Candidate Results
Total Votes in the election are printed to the terminal and is stored in the variable total_votes.

Each candidate’s total votes and percentage of votes are printed to the terminal and is stored in the variable winning_percentage variable.

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
Deliverable 2
County Results
Each county and its total vote count are printed to the terminal and is stored in the following variables and dictionary:

total_county_votes = 0
county_options = []
county_votes = {}
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0
Each county and its percentage of the total votes are printed to the terminal and is executed with the following code: for county_name in county_votes: # 6b: Retrieve the county vote count. countyvotes = county_votes[county_name]

    # 6c: Calculate the percentage of votes for the county.
    countyvote_percentage = float(countyvotes) / float(total_votes) * 100

    county_results = (f"{county_name}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
The county with the largest number of voters is printed to the terminal and is executed with the following code:
if (countyvotes > winning_county_count) and (countyvote_percentage > winning_county_percentage): winning_county_count = countyvotes winning_county = county_name winning_county_percentage = countyvote_percentage

# 7: Print the county with the largest turnout to the terminal.
winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
print(winning_county_summary)
Deliverable 3
# 8: Save the county with the largest turnout to a text file.
txt_file.write(winning_county_summary)
Image of election results that was written on the text file

To view election analysis results files (python and text files) please click on the links below:

Election Challenge Python file
election analysis text file
