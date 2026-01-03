# Reading the CSV file and printing its contents       
import csv
csv_rows=[]
with open('Input.csv', mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        csv_rows.append(row)
print(csv_rows)


# Writing to a new CSV file with specified formatting
with open('Clean_CSV.csv', mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_rows:
        if len(row) !=0:
            csvwriter.writerow(row)
print("New CSV file created successfully.")