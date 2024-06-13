from diferenciasMotivos import plot_motifs
from analizarMotivos import export_to_excel
from encontrarMotivos import main_find_motiv_fasta

def main():
    file_path = 'src/secuencias.fasta'
    data = main_find_motiv_fasta(file_path)

    export_to_excel(data)
    plot_motifs(data, "resultados")

if __name__ == '__main__':
    main()