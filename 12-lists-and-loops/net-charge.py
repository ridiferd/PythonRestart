# Python3.11
# Coding: utf-8
# Lab 12 - Lists and Loops: net charge insulin dari pH 0 sampai pH 14

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Exercise 1: dictionary nilai pKa
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65,
       'e': 4.25}

# Exercise 2: menghitung jumlah tiap asam amino yang memengaruhi muatan
# Contoh satu entitas: float(insulin.count("y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r',
                                                   'd', 'e']})

print(seqCount)


                                                

# Exercise 3: rumus net charge di dalam while loop
pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) /
                   ((10 ** pH) + (10 ** pKR[x])))
               for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x] * (10 ** pH)) /
                    ((10 ** pH) + (10 ** pKR[x])))
                for x in ['y', 'c', 'd', 'e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
