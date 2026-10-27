# Lab 06 - Composite Data Types
# Jalankan dari folder ini agar car_fleet.csv ditemukan.

import csv
import copy

# Dictionary sebagai "cetakan" (composite type) untuk satu kendaraan
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# myVideoGame = {
#     "title": "<empty>",
#     "platform": "<empty>",
#     "genre": "<empty>",
#     "releaseYear": 0
# }

for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

myInventoryList = []

# Menyalin isi CSV dari disk ke memori
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, '
                  f'year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, '
                  f'zeroSixty: {row[6]}, mileage: {row[7]}')
            # deepcopy membuat "kotak" baru untuk setiap kendaraan
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

# Mencetak inventaris mobil
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
