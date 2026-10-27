# Lab 04 - List, Tuple, Dictionary
# Catatan: berkas tidak dinamai collections.py agar tidak menutupi
# modul bawaan Python "collections".

# Exercise 1: list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

myMinion = ["Kevin", "Stuart", "Bob"]
print(myMinion)
print(type(myMinion))

# Mengakses list berdasarkan posisi (dimulai dari 0)
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# versi perulangan menggunakan for
for minion in myMinion:
    print(minion)

# Mengubah nilai di dalam list
myFruitList[2] = "orange"
print(myFruitList)

# Exercise 2: tuple (immutable / tidak bisa diubah)
myFinalAnswerTuple = ("kaya", "ganteng", "pintar")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# myfinalAnswerTuple[2] = "mango"  # This will raise an error because tuples are immutable    

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Exercise 3: dictionary (posisi bernama / key)
myFavoriteFruitDictionary = {
    "Lapar": "Sambat",
    "Kenyang": "Ngantuk",
    "Bokek": "Marah",
    "Senang": "Tersenyum"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Lapar"])
print(myFavoriteFruitDictionary["Kenyang"])
print(myFavoriteFruitDictionary["Bokek"])
print(myFavoriteFruitDictionary["Senang"])

# fungsi mencari key di dictionary
print("Lapar" in myFavoriteFruitDictionary)
print("Tersenyum" in myFavoriteFruitDictionary)

# fungsi mencari value di dictionary
print("Sambat" in myFavoriteFruitDictionary.values())
print("Ngantuk" in myFavoriteFruitDictionary.values())

# fungsi mencari index value di dictionary
def get_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

print(get_key_by_value(myFavoriteFruitDictionary, "Sambat"))
print(get_key_by_value(myFavoriteFruitDictionary, "Ngantuk"))
print(get_key_by_value(myFavoriteFruitDictionary, "Marah"))
print(get_key_by_value(myFavoriteFruitDictionary, "Tersenyum"))

