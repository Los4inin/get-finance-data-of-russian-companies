with open('data-20200316-structure-20140105.csv', 'r', encoding="1251") as f, open('statreg.csv', 'w') as f1:
    for line in f: f1.write(line)
