
class DBConection:                                                  

    class MyDBConnection:                                           
        def __init__(self,host, user, pswd, db_name):
            self.host = host
            self.user = user
            self.pswd = pswd
            self.db_name = db_name
            self.cursor = ""

        def GetCursor(self):
            self.cursor = "Cursor"
            print("Getting a cursor")
            return self.cursor
        
        def executeMyQuery(self, query, cursor):
            if (cursor == self.cursor):
                print("Executing query: ")
                print(query+ "\n")
            else:
                print ("Invalid cursor")
            
        def closeConnection(self):
            self.host = ""
            self.user = ""
            self.pswd = ""
            self.db_name = ""
            self.cursor = ""
            print("Connection closed")

    instance = None                                        #the instance of the class that will be created only once               
    
    def __init__(self):
        if not DBConection.instance:                            # If the instance is not created
            DBConection.instance = DBConection.MyDBConnection("host1", "user1", "pswd123", "hw3.db")
        

    def executeQuery(self, query):
        cursor = self.instance.GetCursor()
        self.instance.executeMyQuery(query, cursor)

    
DB1 = DBConection()
DB1.executeQuery("SELECT * FROM table1")
DB2 = DBConection()
DB1.executeQuery("SELECT * FROM table1")
print(DB1.instance is DB2.instance)