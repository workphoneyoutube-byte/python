class extract:
    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, password, \
            database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password, db = db, 
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

e = extract()
query = "select * from artist;"
dataset = e.fromMYSQL(host = "localhost", username = "root", password = "admin", 
                      db = "vinylrecordshop",query = query)
print(dataset)
print(len(dataset))
