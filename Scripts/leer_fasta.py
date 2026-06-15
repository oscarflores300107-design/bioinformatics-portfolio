from Bio import SeqIO
from pathlib import Path

ruta_fasta = Path(__file__).parent.parent / "datos" / "ejemplo.fasta"

for record in SeqIO.parse(ruta_fasta, "fasta"):
    Secuencia = record.seq.upper()
    print("ID:", record.id)
    print("Longitud:", len(Secuencia))
    if len(Secuencia) > 50:
        print("Secuencia (primeros 50 caracteres):", Secuencia[:50])
  
    for letra in "ACGT":
        print(f"Cantidad de {letra}: {Secuencia.count(letra)}")
    porcent_gc = 100 * (Secuencia.count("G") + Secuencia.count("C")) / len(Secuencia)
    print(f"Porcentaje GC: {porcent_gc:.2f}%")

