# This code parses a Pokemon TCG Online decklist text file export and extracts the card names and quantities.

import re


def parse_decklist(decklist):
    # Initialize empty dictionary to store card names and quantities
    cards = {}
    # Split decklist into lines
    lines = decklist.split('\n')
    # Loop through each line
    for line in lines:
        # Check if line contains a card name
        if re.search('[A-Za-z]+', line):
            # Extract card name and quantity
            match = re.search('([0-9]+) ([A-Za-z ]+)', line)
            quantity = int(match.group(1))
            name = match.group(2)
            # Add card name and quantity to dictionary
            if name in cards:
                cards[name] += quantity
            else:
                cards[name] = quantity
    # Return dictionary of card names and quantities
    return cards
