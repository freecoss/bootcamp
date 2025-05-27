import sqlite3
import requests
import random

conn = sqlite3.connect('countries.db')
conn.execute('''CREATE TABLE IF NOT EXISTS countries
             (name TEXT, capital TEXT, flag TEXT, subregion TEXT, population INTEGER)''')

countries = requests.get('https://restcountries.com/v3.1/all').json()
for country in random.sample(countries, 10):
    conn.execute('INSERT INTO countries VALUES (?,?,?,?,?)', (
        country['name']['common'],
        country['capital'][0] if 'capital' in country else 'None',
        country['flags']['png'],
        country.get('subregion', 'None'),
        country['population']
    ))

conn.commit()
conn.close()