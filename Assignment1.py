import csv
print("\nCreated by Cookhyeong Lee!")


class DataSet:
    def __init__(self, row):
        self.products = row[0]
        self.jan20 = row[1]
        self.feb20 = row[2]
        self.mar20 = row[3]
        self.apr20 = row[4]
        self.may20 = row[5]
        self.jun20 = row[6]
        self.jul20 = row[7]
        self.aug20 = row[8]
        self.sep20 = row[9]
        self.oct20 = row[10]
        self.nov20 = row[11]
        self.dec20 = row[12]
        self.jan21 = row[13]
        self.feb21 = row[14]
        self.mar21 = row[15]
        self.apr21 = row[16]
        self.may21 = row[17]
        self.jun21 = row[18]
        self.jul21 = row[19]
        self.aug21 = row[20]
        self.sep21 = row[21]
        self.oct21 = row[22]
        self.nov21 = row[23]
        self.dec21 = row[24]
        self.jan22 = row[25]
        self.feb22 = row[26]
        self.mar22 = row[27]


rows = []  # Array for the rows


def readCSV():
    try:
        with open('Monthly average retail prices.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            index = 0
            for row in spamreader:
                if index == 0:
                    index = index + 1
                    continue
                index = index + 1
                dataSet = DataSet(row)
                rows.append(dataSet)
    except:
        print("Something's wrong!")


readCSV()

for row in rows:
    print(f"Product: {row.products}", end=", ")
    print(f"Jan 20: {row.jan20}", end=", ")
    print(f"Feb 20: {row.feb20}", end=", ")
    print(f"Mar 20: {row.mar20}", end=", ")
    print(f"Apr 20: {row.apr20}", end=", ")
    print(f"May 20: {row.may20}", end=", ")
    print(f"Jun 20: {row.jun20}", end=", ")
    print(f"Jul 20: {row.jul20}", end=", ")
    print(f"Aug 20: {row.aug20}", end=", ")
    print(f"Sep 20: {row.sep20}", end=", ")
    print(f"Oct 20: {row.oct20}", end=", ")
    print(f"Nov 20: {row.nov20}", end=", ")
    print(f"Dec 20: {row.dec20}", end=", ")
    print(f"Jan 21: {row.jan21}", end=", ")
    print(f"Feb 21: {row.feb21}", end=", ")
    print(f"Mar 21: {row.mar21}", end=", ")
    print(f"Apr 21: {row.apr21}", end=", ")
    print(f"May 21: {row.may21}", end=", ")
    print(f"Jun 21: {row.jun21}", end=", ")
    print(f"Jul 21: {row.jul21}", end=", ")
    print(f"Aug 21: {row.aug21}", end=", ")
    print(f"Sep 21: {row.sep21}", end=", ")
    print(f"Oct 21: {row.oct21}", end=", ")
    print(f"Nov 21: {row.nov21}", end=", ")
    print(f"Dec 21: {row.dec21}", end=", ")
    print(f"Jan 22: {row.jan22}", end=", ")
    print(f"Feb 22: {row.feb22}", end=", ")
    print(f"Mar 22: {row.mar22}",)
