# Lab 10 - Analyze with Python (Bonus: membersihkan data secara program)
# Membaca preproinsulin-seq.txt, membuang ORIGIN, angka, //, spasi, dan
# baris baru, lalu memecahnya menjadi bagian-bagian insulin.

import re

with open('preproinsulin-seq.txt') as seqFile:
    rawSequence = seqFile.read()

# Hapus kata ORIGIN, lalu sisakan hanya huruf kecil
cleanSequence = re.sub(r'[^a-z]', '', rawSequence.replace('ORIGIN', ''))
print("Preproinsulin: " + cleanSequence)
print("Jumlah karakter: " + str(len(cleanSequence)))  # harus 110

# Posisi asam amino (1-based) -> slice Python (0-based)
parts = {
    'preproinsulin-seq-clean.txt': cleanSequence,        # 1-110
    'lsinsulin-seq-clean.txt': cleanSequence[0:24],      # 1-24
    'binsulin-seq-clean.txt': cleanSequence[24:54],      # 25-54
    'cinsulin-seq-clean.txt': cleanSequence[54:89],      # 55-89
    'ainsulin-seq-clean.txt': cleanSequence[89:110],     # 90-110
}

for fileName, sequence in parts.items():
    with open(fileName, 'w') as outFile:
        outFile.write(sequence)
    print("{}: {} karakter".format(fileName, len(sequence)))
