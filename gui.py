import tkinter as tk

import unicodedata

from post_import import import_decklist

desired_width = 40  # Shared variable for desired width


def resize_gui(text_box_pokemon, text_box_trainer, text_box_energy, label_pokemon, label_trainer, label_energy):
    max_width_pokemon = max(len(unicodedata.normalize("NFC", line)) for line in label_pokemon["text"].split("\n"))
    max_width_trainer = max(len(unicodedata.normalize("NFC", line)) for line in label_trainer["text"].split("\n"))
    max_width_energy = max(len(unicodedata.normalize("NFC", line)) for line in label_energy["text"].split("\n"))

    text_box_pokemon.config(width=desired_width)
    text_box_trainer.config(width=desired_width)
    text_box_energy.config(width=desired_width)
    label_pokemon.config(width=max_width_pokemon)
    label_trainer.config(width=max_width_trainer)
    label_energy.config(width=max_width_energy)


def run_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Decklist Importer")

    # Set the font to Arial for labels and text boxes
    label_font = ("Arial", 12, "bold")
    text_font = ("Arial", 10)

    # Create a frame for the Import button
    frame_import = tk.Frame(window)
    frame_import.pack(pady=10)

    # Create a button to import the decklist
    import_button = tk.Button(frame_import, text="Import Decklist",
                              command=lambda: import_decklist(text_box_pokemon, text_box_trainer, text_box_energy))
    import_button.pack()

    # Create a frame for the Pokémon cards
    frame_pokemon = tk.Frame(window)
    frame_pokemon.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a label for the Pokémon cards
    label_pokemon = tk.Label(frame_pokemon, text="Pokémon", font=label_font)
    label_pokemon.pack(side=tk.TOP)

    # Create a text box for the Pokémon cards
    text_box_pokemon = tk.Text(frame_pokemon, height=10, font=text_font)
    text_box_pokemon.pack(fill=tk.BOTH, expand=True)

    # Create a frame for the Trainer cards
    frame_trainer = tk.Frame(window)
    frame_trainer.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a label for the Trainer cards
    label_trainer = tk.Label(frame_trainer, text="Trainer", font=label_font)
    label_trainer.pack(side=tk.TOP)

    # Create a text box for the Trainer cards
    text_box_trainer = tk.Text(frame_trainer, height=10, font=text_font)
    text_box_trainer.pack(fill=tk.BOTH, expand=True)

    # Create a frame for the Energy cards
    frame_energy = tk.Frame(window)
    frame_energy.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a label for the Energy cards
    label_energy = tk.Label(frame_energy, text="Energy", font=label_font)
    label_energy.pack(side=tk.TOP)

    # Create a text box for the Energy cards
    text_box_energy = tk.Text(frame_energy, height=10, font=text_font)
    text_box_energy.pack(fill=tk.BOTH, expand=True)

    # Bind a function to the window resize event
    window.bind("<Configure>",
                lambda event: resize_gui(text_box_pokemon, text_box_trainer, text_box_energy, label_pokemon,
                                         label_trainer, label_energy))

    # Start the GUI event loop
    window.mainloop()
