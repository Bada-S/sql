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

#average weapons per character
query4 = """
SELECT avg(weapon_count) as avg_weapons_per_char
FROM (
	SELECT 
		c.character_id,
		count(distinct w.item_ptr_id) as weapon_count
	FROM charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv on c.character_id = inv.character_id
	LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
	GROUP BY c.character_id
) subq
"""