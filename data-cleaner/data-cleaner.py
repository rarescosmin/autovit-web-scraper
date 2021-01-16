import csv
from csv import DictReader
from csv import DictWriter
import string

def removeAllSpaces(word):
    return word.translate({ord(c): None for c in string.whitespace})



def sanitizeCsvData(rawDatFileName, outPutFileName):
    with open(rawDatFileName, 'r') as read_obj:
        csv_reader = DictReader(read_obj)

        with open(outPutFileName, 'a', newline='') as writer_obj:
            csv_writer = csv.DictWriter(writer_obj, fieldnames=['make', 'model', 'year', 'mileage', 'fuelType', 'engineCapacity', 'price'])
            csv_writer.writeheader()
            for row in csv_reader:
                for key in row:
                    row[key] = removeAllSpaces(row[key])

                if ('km' or 'KM' or 'kM' or 'Km' in row['mileage']):
                    row['mileage'] = row['mileage'][:-2]

                if ('cm' or 'CM' or 'cM' or 'Cm' in row['engineCapacity']):
                    row['engineCapacity'] = row['engineCapacity'][:-3]
                
                if (',' in row['price']):
                    row['price'] = row['price'][:len(row['price']) - row['price'].index(',') + 2]
                    
                row['price'] = ''.join([i for i in row['price'] if i.isdigit()])
                

                csv_writer.writerow(row)

if __name__ == '__main__':
    sanitizeCsvData('./raw-csv-data/cars_train.csv', './cleaned-csv-data/cars_train.csv')
    sanitizeCsvData('./raw-csv-data/cars_test.csv', './cleaned-csv-data/cars_test.csv')
    print('FINISHED CLEANING DATA')
