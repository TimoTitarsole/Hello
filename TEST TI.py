import psycopg2

try:
    conn = psycopg2.connect("dbname='lpdstrtn' " "user='lpdstrtn' " "host='dumbo.db.elephantsql.com' " "password='OQBOtTdWyf5xbdDqwGFyi_T_rQ2KcjNw'")
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()

def updatevolume(containernr, percentage):
    sql = "UPDATE container SET volume = %s WHERE containernummer = %s"
    try:
        cur.execute(sql, (percentage, containernr))
        conn.commit()
    except:
        print("Can't UPDATE container")

wanker = 69

updatevolume(1, wanker)