import re
from leerSecuencias import guarda_secuencias

def find_motis_in_sequence(sequence, moti_pattern=r"N[^P][ST]"):
    """
    Busca motivos en una secuencia de proteínas y devuelve un diccionario con cada motivo y las posiciones donde se encontraron.
    
    Params:
    sequence (str): La secuencia de proteínas en la que buscar.
    moti_pattern (str): El patrón de expresión regular para buscar los motivos.
    
    Returns:
    dict: Un diccionario donde las claves son los motivos encontrados y los valores son listas de posiciones donde esos motivos se encontraron.
    """
    moti_dict = {}
    pattern = re.compile(moti_pattern)
    
    for match in re.finditer(pattern, sequence):
        start = match.start()
        found_moti = sequence[start:start+3]
        
        if found_moti not in moti_dict:
            moti_dict[found_moti] = []
        moti_dict[found_moti].append(start)
    
    return moti_dict


def main_find_motiv_fasta(file_path):
    # primero obtenemos el diccionario de las secuencias 
    secuencias = guarda_secuencias(file_path)

    # diccionario para guardar ID:{motivo:posicion}
    motivos = {}
    
    # iteramos sobre todas las secuencias 
    for clave, valor in secuencias.items():
        moti_dict = find_motis_in_sequence(valor)
        motivos[clave] = moti_dict
    
    return motivos
