from Bio import SeqIO
from pathlib import Path

ruta_fasta = Path(__file__).parent.parent / "datos" / "ejemplo.fasta"

for record in SeqIO.parse(ruta_fasta, "fasta"):
    print("ID:", record.id)
    print("Longitud:", len(record.seq))
    print("Secuencia:", record.seq)