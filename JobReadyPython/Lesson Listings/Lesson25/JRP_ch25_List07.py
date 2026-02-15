class extract:
    @staticmethod
    def fromCSV(file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            # message to display if the user fails to provide a file path at all
            raise Exception("You must provide a valid file path.")
        try:
            import csv
            dataset = list()
            with open(file_path) as f:
                csv_file = csv.DictReader(f, delimiter = delimiter, 
                                          quotechar = quotechar) 
                for row in csv_file:
                    dataset.append(row)
            return dataset  
        except (IOError, OSError):
            raise Exception("You must provide a valid CSV file.")

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password, 
                             db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
            password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username  = username, 
                                     password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        dataset = list()
        if query:
            for document in tmp_collection.find(query):  
                dataset.append(document)
            return dataset
        for document in tmp_collection.find():  
                dataset.append(document)
        return dataset

dataset = extract.fromCSV(file_path="data/wrong_name.csv")
print(dataset[0])
