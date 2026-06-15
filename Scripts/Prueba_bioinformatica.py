from Bio.Seq import Seq

secuencia = Seq("ATGCGTAA")

print("Secuencia:", secuencia)
print("Longitud:", len(secuencia))
print("Complementaria:", secuencia.complement())
