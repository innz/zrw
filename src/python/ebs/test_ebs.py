__author__ = 'zrw'
#!/usr/bin/env python

from ebs import *
import uuid
import sqlite3
import os

db = os.getcwd() + "\cinder.db"

def test():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS volume(uuid text primary key, volume_id text)''')
    volume = {}
    driver = BCEBSDriver()
    volume['user_id'] = str(uuid.uuid1())
    volume['size'] = 2
    vid = driver.create_volume(volume)
    c.execute("INSERT INTO volume VALUES (?,?)", (volume['user_id'], vid))
    print vid

    conn.commit()
    conn.close()


if __name__ == "__main__":
    test()
