import psycopg2

from menu_item import MenuItem

class MenuManager():

    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(dbname='restaurant', user='postgres', password='your_password')
        cur = conn.cursor()
        cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_name=%s;", (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            item = MenuItem(row[1], row[2])
            item.item_id = row[0]
            return item
        return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(dbname='restaurant', user='postgres', password='your_password')
        cur = conn.cursor()
        cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        items = []
        for row in rows:
            item = MenuItem(row[1], row[2])
            item.item_id = row[0]
            items.append(item)
        return items
