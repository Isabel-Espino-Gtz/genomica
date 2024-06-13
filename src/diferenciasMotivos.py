import matplotlib.pyplot as plt
import pandas as pd
from itertools import islice
import os 
from encontrarMotivos import main_find_motiv_fasta

file_path = 'src/secuencias.fasta'
data = main_find_motiv_fasta(file_path)

def plot_motifs(data, save_directory):
    # Crear el directorio para guardar las imágenes si no existe
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # Determinar todos los motivos únicos
    all_motifs = ['NAS', 'NAT', 'NCT', 'NES', 'NFS', 'NFT', 'NGT', 'NHT', 'NIT', 'NKS']  # Lista de motivos a analizar
    
    # Crear y guardar un gráfico para cada motivo
    for motif in all_motifs:
        plt.figure(figsize=(10, 5))
        plt.title(f"Positions of {motif} in various IDs")
        plt.xlabel("Positions")
        plt.ylabel("IDs")
        
        # Agregar cada ID como una serie en el gráfico del motivo, considerando solo los primeros 10 ID
        for id, motifs in islice(data.items(), 10):
            if motif in motifs:
                positions = motifs[motif]
                plt.plot(positions, [id] * len(positions), 'o', label=id)
        
        plt.legend()
        plt.grid(True)
        # Guardar la figura en el directorio especificado
        plt.savefig(os.path.join(save_directory, f"{motif}.png"))
        plt.close()