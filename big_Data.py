import csv
import random

tup = ((
           'Bunnik', 'Amsterdam', 'Utrecht', 'Eindhoven', 'Rotterdam', 'Nijmegen', 'Groningen', 'Leeuwarden', 'Woerden',
           'Delft'),
       ('rood', 'blauw', 'geel', 'groen', 'zwart', 'wit', 'paars', 'oranje', 'grijs', 'limoen'),
       ('Bas', 'Joost', 'Piet', 'Klaas', 'Bart', 'Henk', 'Maartje', 'Anne', 'Mees', 'Pom'),
       ('Hyundai', 'Volvo', 'Ford', 'Volkswagen', 'Peugot', 'Citroen', 'Honda', 'Skoda', 'Ferrari', 'Audi'),
       (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
       (20, 30, 40, 50, 60, 70, 80, 90, 110, 120),
       ('koffie', 'chocomel', 'water', 'limonade', 'thee', 'whiskey', 'wodka', 'cola', 'ice_tea', 'fanta'),
       (40, 50, 60, 70, 80, 90, 100, 110, 120, 130),
       ('Shell', 'BP', 'Esso', 'Total', 'Texaco', 'Q8', 'Caltex', 'Haan', 'ARCO', 'American Gas'),
       (2, 3, 4, 5, 6, 7, 8, 9, 10, 11))


def writeCSV():
    with open('file.csv', 'w', newline='\n') as csvFile:
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
        # old code, please ignore
        # line = 0
        # while line < 100000:  # while line number is not reached, keep writing rows
        #    number = random.randrange(10)
        #    if number in range(len(kleur)):  # if the random generated indexnumber
        #        # does not appear in the indexrange of the tuples, try again
        #        writer.writerow({'Woonplaats': woonplaats[number], 'Kleur': kleur[number], 'Naam': naam[number],
        #                         'Merk': merk[number], 'Deuraantal': deur[number], 'Leeftijd': leeftijd[number],
        #                         'Vloeistof': vloeistof[number], 'Snelheid': snelheid[number],
        #                         'Tankstation': tankstation[number], 'Ramen': raam[number]})
        #        line += 1
        #    elif number not in range(len(kleur)):
        #        continue

        for line in range(100000):
            writer.writerow({fieldnames[i]: tup[i][random.randrange(10)] for i in range(10)})



writeCSV()


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


'''# calculate()
dic = {}
count = 0
with open('test.csv', 'r', newline='\n') as testCSV:
    testReader = csv.reader(testCSV)
    for item in next(testReader):
        dic[item] = {}
    print(dic)
    for row in testReader:
        'print(row)'
        for indexNumber in range(len(row)):
            print(row[indexNumber])

    print(dic)'''
