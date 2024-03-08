from Bio import Entrez
from Bio import SeqIO
import sys

def fetch_sequences(entry_ids):
    Entrez.email = "jonathan.magliano@biogenetika.com.br"

    entry_ids = list(set(entry_ids))
    
    id_string = ','.join(entry_ids)
    handle = Entrez.efetch(db="nucleotide", id=id_string, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    handle.close()
    
    return records

def save_sequence(sequence, filename):
    with open(filename, "w") as file:
        file.write(f">{sequence.description}\n")
        file.write(str(sequence.seq))

def get_entry_ids():
    print("Exemplo de IDs separados por espaço: FJ817486 JX069768 JX469983\n")
    print("Digite um ID ou mais (GenBank): ")
    entry_ids = input().split()

    if len(entry_ids) > 10:
        print("Por favor, forneça no máximo 10 IDs GenBank.")
        sys.exit(1)

    return entry_ids

def main():
    entry_ids = get_entry_ids()

    sequences = fetch_sequences(entry_ids)

    if not sequences:
        print("Nenhuma sequência encontrada para os IDs fornecidos.")
        sys.exit(1)

    for sequence in sequences:
        print(f">{sequence.description}")
        print(sequence.seq)
        save_sequence(sequence, f"{sequence.id}_biogenetika.fasta")

if __name__ == "__main__":
    main()
