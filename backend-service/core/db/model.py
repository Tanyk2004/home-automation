import sqlite3


class dbManager:

    TABLE_NAME = "relays_record"

    def __init__(self):
        self.con = sqlite3.connect("relays.db")
        self.c = self.con.cursor()
        # self.c.execute(f"CREATE TABLE {dbManager.TABLE_NAME} (id INTEGER PRIMARY KEY, state bool);")

    def checkIfRelayExists(self, id : int) -> bool:
        """
        Return
            :return True if a relay entity with the 'id' exists
        """
        self.c.execute(f"SELECT 1 from {dbManager.TABLE_NAME} WHERE id='{id}';")
        result = self.c.fetchone()
        return bool(result)

    def addRelay(self, id : int, state : bool):
        """
        Adds a relay entity into the database

        Args:
            :param id relay Number
            :param state relay state

        Raises:
            ValueError: If another relay with the same ID already exists in the database
        """
        if self.checkIfRelayExists(id):
            raise ValueError(f"Relay with the ID {id} already exists in the database.")
        self.c.execute(f"insert into {dbManager.TABLE_NAME} values ({id} , {state})")
        self.con.commit()
    
    def getRelayState(self, id : int) -> bool:
        """
        Returns the state of the relay with the specific id

        Args:
            :param id of the relay
        
        Return:
            :return the state of the relay

        Raises:
            ValueError: If a relay with the id doesn't exist
        """
        if not (self.checkIfRelayExists(id)):
            raise ValueError(f"Relay with the ID {id} doesn't exist in the database.")
        self.c.execute(f"SELECT state FROM {dbManager.TABLE_NAME} WHERE id={id}")
        state = self.c.fetchone()[0]
        return bool(state)

    
    def dropRelay(self, id : int) -> bool:
        """
        Drops a relay with the passed in id

        Args:
        :param id of the relay

        Return:
        :return True if the relay was successfully dropped

        Return:
            :return True if relay was successfully dropped
        """
        if not (self.checkIfRelayExists(id)):
            return False
        self.c.execute(f"DELETE FROM {dbManager.TABLE_NAME} where id={id}")
        self.con.commit()
        return True

    def updateRelayState(self, id: int, state: bool) -> bool:
        """
        Updates the state of the relay with the passed in id

        Args:
            :param id of the relay
            :param state of the relay
        Return:
            :return True if the relay was successfully updated
        Raises:
            ValueError: If a relay with the id doesn't exist
        """
        if not (self.checkIfRelayExists(id)):
            raise ValueError(f"Relay with the ID {id} doesn't exist in the database.")
        self.c.execute(f"UPDATE {dbManager.TABLE_NAME} SET state={state} WHERE id={id}")
        self.con.commit()
        return True
    
    def getAllRelays(self) -> list:
        """
        Returns all the relays in the database

        Return:
            :return list of all the relays in the database
        """
        self.c.execute(f"SELECT * FROM {dbManager.TABLE_NAME}")
        return self.c.fetchall()


# if __name__ == "__main__":
#     m = dbManager()
#     cursor = m.c
#     # cursor.execute(f"CREATE TABLE {dbManager.TABLE_NAME} (id INTEGER PRIMARY KEY, state bool);")
#     # cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
#     # cursor.execute("INSERT INTO relays_record VALUES (4 , FALSE)")
#     # cursor.execute(f"PRAGMA table_info({dbManager.TABLE_NAME})")
#     # cursor.execute("select * from relays_record")
#     # m.addRelay(4, False)
#     # m.updateRelayState(5, True)
#     # m.addRelay(1, False)
#     # print(m.getRelayState(4))
#     m.dropRelay(4)
#     cursor.execute("select * from relays_record")
#     tables = cursor.fetchall()
#     print("******* OUTPUT *******")
#     for i in tables:
#         print(i)
#     m.con.commit()
#     cursor.close()

