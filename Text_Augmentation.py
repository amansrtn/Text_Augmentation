import csv
from textaugment import Wordnet

# read the CSV file
with open('data1.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

# define a function to perform data augmentation

t = Wordnet()

# loop through the rows and perform data augmentation where Category=1
new_rows = []
for row in rows:
    if row['Category'] == '1':
        message = row['Message']
        augmented_messages = t.augment(message)
        new_row = row.copy()
        new_row['Message'] = augmented_messages
        new_row['Category'] = '1'
        new_rows.append(new_row)

# append the new rows to the original CSV file
with open('data1.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    for new_row in new_rows:
        writer.writerow(new_row)
