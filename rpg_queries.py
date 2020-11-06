import pandas as pd 
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

#how many characers
query = """
    SELECT count(character_id)
    FROM charactercreator_character
"""

#how many items
query1 = """
    SELECT count(item_id)
    FROM armory_item
"""

#how many items are weapons
query2 = """
    SELECT count(item_id)
    FROM armory_item
    INNER JOIN armory_weapon 
    ON armory_item.item_id = armory_weapon.item_ptr_id
"""

#items per character(first 20)
query3 = """
    SELECT DISTINCT character_id, count(item_id) as num_items
    FROM charactercreator_character_inventory
    Group by character_id
    Limit 20
"""

#average items per character