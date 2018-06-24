import sqlite3
import Investigator
conn = sqlite3.connect(r'C:\Users\Gwen\PycharmProjects\ArkhamHorrorV2\Database\Arkham.db')
c = conn.cursor()
for key in c.execute("SELECT name FROM Investigators"):
    print(key)


def selectInvestigator(pkey):
    pkey = (pkey,)
    c.execute('SELECT * FROM investigators WHERE key = ?', pkey)
    i = c.fetchone()
    print(i)
    return Investigator.Investigator(i[0], i[2], i[3], i[4], i[5], i[6], i[7])

if __name__ == '__main__':
    Daisy = selectInvestigator("2")
