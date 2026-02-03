import json

with open(r'App/config/prod.json', 'r', encoding='utf-8') as file:
    CONFIG = json.load(file)

class Caminhos:
    legendas_originais = CONFIG['pastas']['legendas_originais']
    legendas_ajustadas = CONFIG['pastas']['legendas_ajustadas']
