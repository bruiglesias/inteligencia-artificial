import pandas as pd
base = pd.read_csv('basedados.csv',  encoding = 'ISO-8859-1')

base = base.drop('dateCrawled', axis = 1)
base = base.drop('dateCreated', axis = 1)
base = base.drop('nrOfPictures', axis = 1)
base = base.drop('postalCode', axis = 1)
base = base.drop('lastSeen', axis = 1)

base['name'].value_counts()
base = base.drop('name', axis = 1)
