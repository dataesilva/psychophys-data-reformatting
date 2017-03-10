import csv

print('Psychophys Data Reformatting by David E. Silva')
with open('data_long.csv', 'w', newline = '') as new:
    fieldnames = ['ID', 'metric', 'order', 'value']
    writer = csv.DictWriter(new, fieldnames = fieldnames)
    writer.writeheader()
    with open('data_wide.csv', 'r') as old:
        oldread = csv.reader(old, delimiter = ',')
        for row in oldread:
            for field in row[3:1100]: #depending on how long the data was recorded
                writer.writerow({'ID': row[0], 'metric': row[1], 'order': row[2], 'value': field})

print('Done')
