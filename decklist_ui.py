import tkinter as tk

# Create tkinter window
window = tk.Tk()
window.title('Decklist Viewer')

# Add labels and text boxes
label = tk.Label(window, text='Decklist Name:')
label.pack()
decklist_name = tk.Entry(window)
decklist_name.pack()

label = tk.Label(window, text='Decklist Cards:')
label.pack()
decklist_cards = tk.Text(window, height=10, width=50)
decklist_cards.pack()

# Read decklist data from file or input directly
# decklist_data = read_decklist_data()

# Populate labels and text boxes with decklist data
# decklist_name.insert(0, decklist_data['name'])
# decklist_cards.insert(tk.END, decklist_data['cards'])

# Run tkinter event loop
window.mainloop()