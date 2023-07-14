import tkinter as tk
import unicodedata
from tkinter import filedialog

def resize_gui(text_box_pokemon, text_box_trainer, text_box_energy):
    max_width_pokemon = max(len(unicodedata.normalize("NFC", line)) for line in text_box_pokemon.get("1.0", tk.END).split("\n"))
    max_width_trainer = max(len(unicodedata.normalize("NFC", line)) for line in text_box_trainer.get("1.0", tk.END).split("\n"))
    max_width_energy = max(len(unicodedata.normalize("NFC", line)) for line in text_box_energy.get("1.0", tk.END).split("\n"))

    max_lines_pokemon = max(count_lines(text_box_pokemon), 10)  # Minimum of 10 lines
    max_lines_trainer = max(count_lines(text_box_trainer), 10)  # Minimum of 10 lines
    max_lines_energy = max(count_lines(text_box_energy), 10)  # Minimum of 10 lines

    text_box_pokemon.config(width=desired_width, height=max_lines_pokemon)
    text_box_trainer.config(width=desired_width, height=max_lines_trainer)
    text_box_energy.config(width=desired_width, height=max_lines_energy)

def count_lines(text_box):
    return int(text_box.index(tk.END).split(".")[0])

def display_parsed_decklist(parsed_decklist, text_box_pokemon, text_box_trainer, text_box_energy):
    # Clear the existing text in all text boxes
    text_box_pokemon.config(state="normal")
    text_box_trainer.config(state="normal")
    text_box_energy.config(state="normal")
    text_box_pokemon.delete('1.0', tk.END)
    text_box_trainer.delete('1.0', tk.END)
    text_box_energy.delete('1.0', tk.END)

    # Display the parsed decklist in the respective text boxes
    for card_type, card_list in parsed_decklist.items():
        if card_list:
            text_box = get_text_box_by_type(card_type, text_box_pokemon, text_box_trainer, text_box_energy)
            text_box.insert(tk.END, f"{card_type}:\n")
            for card in card_list:
                text_box.insert(tk.END, f"{card}\n")

    text_box_pokemon.config(state="disabled")
    text_box_trainer.config(state="disabled")
    text_box_energy.config(state="disabled")

    # Resize the GUI window after displaying the parsed decklist
    resize_gui(text_box_pokemon, text_box_trainer, text_box_energy)

def get_text_box_by_type(card_type, text_box_pokemon, text_box_trainer, text_box_energy):
    if card_type == "Pokémon":
        return text_box_pokemon
    elif card_type == "Trainer":
        return text_box_trainer
    elif card_type == "Energy":
        return text_box_energy

import tkinter as tk
import unicodedata
from tkinter import filedialog

def resize_gui(text_box_pokemon, text_box_trainer, text_box_energy):
    max_width_pokemon = max(len(unicodedata.normalize("NFC", line)) for line in text_box_pokemon.get("1.0", tk.END).split("\n"))
    max_width_trainer = max(len(unicodedata.normalize("NFC", line)) for line in text_box_trainer.get("1.0", tk.END).split("\n"))
    max_width_energy = max(len(unicodedata.normalize("NFC", line)) for line in text_box_energy.get("1.0", tk.END).split("\n"))

    max_lines_pokemon = max(count_lines(text_box_pokemon), 10)  # Minimum of 10 lines
    max_lines_trainer = max(count_lines(text_box_trainer), 10)  # Minimum of 10 lines
    max_lines_energy = max(count_lines(text_box_energy), 10)  # Minimum of 10 lines

    text_box_pokemon.config(width=desired_width, height=max_lines_pokemon)
    text_box_trainer.config(width=desired_width, height=max_lines_trainer)
    text_box_energy.config(width=desired_width, height=max_lines_energy)

def count_lines(text_box):
    return int(text_box.index(tk.END).split(".")[0])

def display_parsed_decklist(parsed_decklist, text_box_pokemon, text_box_trainer, text_box_energy):
    # Clear the existing text in all text boxes
    text_box_pokemon.config(state="normal")
    text_box_trainer.config(state="normal")
    text_box_energy.config(state="normal")
    text_box_pokemon.delete('1.0', tk.END)
    text_box_trainer.delete('1.0', tk.END)
    text_box_energy.delete('1.0', tk.END)

    # Display the parsed decklist in the respective text boxes
    for card_type, card_list in parsed_decklist.items():
        if card_list:
            text_box = get_text_box_by_type(card_type, text_box_pokemon, text_box_trainer, text_box_energy)
            text_box.insert(tk.END, f"{card_type}:\n")
            for card in card_list:
                text_box.insert(tk.END, f"{card}\n")

    text_box_pokemon.config(state="disabled")
    text_box_trainer.config(state="disabled")
    text_box_energy.config(state="disabled")

    # Resize the GUI window after displaying the parsed decklist
    resize_gui(text_box_pokemon, text_box_trainer, text_box_energy)

def get_text_box_by_type(card_type, text_box_pokemon, text_box_trainer, text_box_energy):
    if card_type == "Pokémon":
        return text_box_pokemon
    elif card_type == "Trainer":
        return text_box_trainer
    elif card_type == "Energy":
        return text_box_energy

def import_decklist(text_box_pokemon, text_box_trainer, text_box_energy, desired_width):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            decklist_text = file.read()

        parsed_decklist = parse_decklist(decklist_text)
        display_parsed_decklist(parsed_decklist, text

    return parsed_decklist

