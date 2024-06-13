import matplotlib.pyplot as plt
import pandas as pd
from encontrarMotivos import main_find_motiv_fasta

def export_to_excel(data, filename='analisisMotivos.xlsx'):
    """Exporta los datos a un archivo Excel."""
    # Transforma el diccionario para que sea adecuado para un DataFrame
    rows = []
    for id_key, motifs in data.items():
        for motif, positions in motifs.items():
            for position in positions:
                rows.append({'ID': id_key, 'Motivo': motif, 'Posición': position})
    
    df = pd.DataFrame(rows)
    
    # Escribe el DataFrame a un archivo Excel
    df.to_excel(filename, index=False)
    print(f"Datos exportados a {filename}")
