from Bio import SeqIO

def compare_fasta_files(file1, file2):
    records1 = list(SeqIO.parse(file1, "fasta"))
    
    records2 = list(SeqIO.parse(file2, "fasta"))

    if len(records1) != len(records2):
        return False

    for record1, record2 in zip(records1, records2):
        if record1.id != record2.id or record1.seq != record2.seq:
            return False

    return True

file1 = "JX469983.1_biogenetika.fasta"
file2 = "file2.fasta"

if compare_fasta_files(file1, file2):
    print("Os arquivos são iguais.")
else:
    print("Os arquivos são diferentes.")
