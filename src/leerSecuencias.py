from Bio import SeqIO

def read_fasta(file_path):
    """
    Lee un archivo FASTA y regresa una lista de objetos SeqRecord.
    
    Params:
    file_path (str): Ruta al archivo FASTA que se va a leer.
    
    Returns:
    list: Lista de objetos SeqRecord, cada uno representando una secuencia en el archivo FASTA.
    """
    sequences = []
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences.append(record)
    return sequences

def analyze_sequences(sequences):
    """
    Analiza una lista de secuencias (SeqRecord), almacena cada una en un diccionario con su ID como clave,
    y opcionalmente imprime detalles de cada secuencia.
    
    Params:
    sequences (list): Lista de objetos SeqRecord a analizar.
    
    Returns:
    dict: Diccionario con IDs de secuencias como claves y las secuencias como valores (en formato string).
    """
    secuencias = {}  # Inicializa un diccionario vacío

    for record in sequences:
        # Almacena cada secuencia en el diccionario usando su ID como clave
        secuencias[record.id] = str(record.seq)

    return secuencias  # Regresa el diccionario con las secuencias

def guarda_secuencias(file_path):
    """
    Método principal que manda a leer y analizar las secuencias de un archivo fasta

    Params:
    file_path (string): la ruta del archivo fasta
    
    Returns:
    dict: Diccionario con IDs de secuencias como claves y las secuencias como valores (en formato string).
    """
    sequences = read_fasta(file_path) # se lee el archivo fasta donde están las secuencias 
    diccionario = analyze_sequences(sequences) # guardamos en un diccionario cada secuencia con su ID
    return diccionario # regresamos el diccionario