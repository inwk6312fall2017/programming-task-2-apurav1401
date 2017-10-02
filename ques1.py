import cvs

with open('crime.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    crime = []
    id = []
    for row in readCSV:
        crime = row[3]
        id = row[0]

        crime.append(date)
        id.append(color)

    print(crime)
    print(id)
