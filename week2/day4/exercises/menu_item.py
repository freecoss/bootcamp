import psycopg2

class MenuItem():
    def __init__(self, item_name, item_price):
        self.item_id = None
        self.item_name = item_name
        self.item_price = item_price
    
    
    def save(self):
        conn = psycopg2.connect(dbname='Menu_Items', user='postgres', password='root')
        cur = conn.cursor()
        if self.item_id is None:
            cur.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;",
                (self.item_name, self.item_price)
            )
            self.item_id = cur.fetchone()[0]
        else:
            cur.execute(
                "UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_id=%s;",
                (self.item_name, self.item_price, self.item_id)
            )
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        if self.item_id is None:
            print("Item not saved yet.")
            return
        conn = psycopg2.connect(dbname='Menu_Items', user='postgres', password='root')
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_id=%s;", (self.item_id,))
        conn.commit()
        cur.close()
        conn.close()
        self.item_id = None

    def update(self,new_id, new_name, new_price):
        conn = psycopg2.connect(dbname='Menu_Items', user='postgres', password='root')
        cur = conn.cursor()
        cur.execute("update Menu_Items set item_name = %s, item_price=%s where item_id = %s",(new_name, new_price,new_id))
        conn.commit()
        cur.close()
        conn.close()