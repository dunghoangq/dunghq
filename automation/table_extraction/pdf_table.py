'''
pip install tk
pip install ghostscript
pipinstall camelot-py
'''
import camelot

tables = camelot.read_pdf('file.pdf', pages='1')

# export all tables
tables.export('tables.csv', f='csv', compress=True)

# export first table
table[0].to_csv('table0.csv')