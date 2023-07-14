# Import the regular expressions module
import re

# Open the tournament results and decklists file
with open('tournament_results_and_decklists.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Define the regular expressions to extract the relevant data
tournament_regex = r'(?P<place>\d+)\.\s+(?P<deck_name>[^\n]+)\s+(?P<win_percentage>\d+\.\d+)%\s+(?P<description>[^\n]+)' # Extracts tournament results
deck_regex = r'(?P<deck_name>[^\n]+)\s+(?P<win_percentage>\d+\.\d+)%\s+(?P<description>[^\n]+)' # Extracts decklists

# Extract the tournament results and decklists data using the regular expressions
tournament_results = re.findall(tournament_regex, contents)
decklists = re.findall(deck_regex, contents)

# Store the extracted data in a list of dictionaries
data = []
for result in tournament_results:
    data.append({
        'place': result[0],
        'deck_name': result[1],
        'win_percentage': result[2],
        'description': result[3]
    })
for decklist in decklists:
    data.append({
        'deck_name': decklist[0],
        'win_percentage': decklist[1],
        'description': decklist[2]
    })

# Print the extracted data
print(data)