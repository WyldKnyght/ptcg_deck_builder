import os

relevant_files = []

for root, dirs, files in os.walk('D:/my_apps/DEV/~PokemonTCG_Nexus/1_PTCG_Data_Auto-GPT-0.3.1/autogpt/auto_gpt_workspace/pokemon-tcg-data'):
    for file in files:
        if file.endswith('.json') and ('decks' in file or 'matches' in file):
            relevant_files.append(os.path.join(root, file))

print(relevant_files)