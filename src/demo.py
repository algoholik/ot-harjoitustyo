'''
Populate database with demo content:
- Notes x 100
- Snips x 100
'''
from faker import Faker
import database.db_handler as db_handler

fake = Faker()

for demo in range(100):
    note = db_handler.create_note(fake.name(), fake.text())
    snip = db_handler.create_snip(fake.name(), fake.text())
