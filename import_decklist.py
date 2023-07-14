# This code prompts the user to input the filename of a Pokemon TCG Online decklist text file export to import and parse.

import os
from parse_decklist import parse_decklist

# Prompt user to input filename of decklist file
filename = input('Enter filename of decklist file to import: ')

# Check if file exists
if not os.path.isfile(filename):
    print('Error: File does not exist')
    exit()

# Read decklist file
with open(filename, 'r') as f:
    decklist = f.read()

# Parse decklist
cards = parse_decklist(decklist)

# Write card names and quantities to log file
log_filename = 'log/' + os.path.splitext(os.path.basename(filename))[0] + '_log.txt'
with open(log_filename, 'w') as f:
    for card, quantity in cards.items():
        f.write('{} x {}\n'.format(quantity, card))

print('Import successful. Card names and quantities written to log file: {}'.format(log_filename))
