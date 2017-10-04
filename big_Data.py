import csv
import random

woonplaats = (
    'Bunnik', 'Amsterdam', 'Utrecht', 'Eindhoven', 'Rotterdam', 'Nijmegen', 'Groningen', 'Leeuwarden', 'Woerden',
    'Delft')
kleur = ('rood', 'blauw', 'geel', 'groen', 'zwart', 'wit', 'paars', 'oranje', 'grijs', 'limoen')
naam = ('Bas', 'Joost', 'Piet', 'Klaas', 'Bart', 'Henk', 'Maartje', 'Anne', 'Mees', 'Pom')
merk = ('Hyundai', 'Volvo', 'Ford', 'Volkswagen', 'Peugot', 'Citroen', 'Honda', 'Skoda', 'Ferrari', 'Audi')
deur = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
leeftijd = (20, 30, 40, 50, 60, 70, 80, 90, 110, 120)
vloeistof = ('koffie', 'chocomel', 'water', 'limonade', 'thee', 'whiskey', 'wodka', 'cola', 'ice_tea', 'fanta')
snelheid = (40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140)
tankstation = ('Shell', 'BP', 'Esso', 'Total', 'Texaco', 'Q8', 'Caltex', 'Haan', 'ARCO', 'American Gas')
raam = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


def writeCSV():
    with open('file1.csv', 'w', newline='\n') as csvFile:
        fieldnames = (
            'Woonplaats', 'Kleur', 'Naam', 'Merk', 'Deuraantal', 'Leeftijd', 'Vloeistof', 'Snelheid', 'Tankstation',
            'Ramen')
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        # old code, please ignore
        # for x in range(10):
        #   number = random.randrange(100)
        #  while number in range(len(namen)):
        #     if number in range(len(namen)):
        #        writer.writerow({'Woonplaats': woonplaatsen[number]})
        #   elif number not in range(len(namen)):
        #      break

        writer.writeheader()
        line = 0
        while line < 100000:  # while line number is not reached, keep writing rows
            number = random.randrange(10)
            if number in range(len(woonplaats)):  # if the random generated indexnumber
                # does not appear in the indexrange of the tuples, try again
                writer.writerow({'Woonplaats': woonplaats[number], 'Kleur': kleur[number], 'Naam': naam[number],
                                 'Merk': merk[number], 'Deuraantal': deur[number], 'Leeftijd': leeftijd[number],
                                 'Vloeistof': vloeistof[number], 'Snelheid': snelheid[number],
                                 'Tankstation': tankstation[number], 'Ramen': raam[number]})
                line += 1
            elif number not in range(len(woonplaats)):
                continue
                # print('error')
                # break


# writeCSV()


def calculate():
    with open('file.csv', 'r', newline='\n') as csvread:
        reader = csv.reader(csvread)
        next(reader)
        dic = {'Woonplaats': {}, 'Kleur': {}}
        for x in reader:
            if x[0] in dic['Woonplaats']:
                dic['Woonplaats'][x[0]] += 1
            elif x[0] not in dic['Woonplaats']:
                dic['Woonplaats'][x[0]] = 1

            if x[1] in dic['Kleur']:
                dic['Kleur'][x[1]] += 1
            elif x[1] not in dic['Kleur']:
                dic['Kleur'][x[1]] = 1

        print(dic)


# calculate()
dic = {}

with open('test.csv', 'r', newline='\n') as testCSV:
    testReader = csv.reader(testCSV)
    for item in next(testReader):
        dic[item] = {}
    print(dic)
    for row in testReader:
        for indexNumber in range(len(row)):
            if row[indexNumber] in dic:
                for key in dic.keys():
                    dic[key][row[indexNumber]] += 1
            elif row[indexNumber] not in dic:
                for key in dic.keys():
                    dic[key][row[indexNumber]] = 0
    for x in dic.keys():
        print(x)