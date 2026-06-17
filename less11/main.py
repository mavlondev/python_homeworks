# ### Task 1

# 1. **Database Creation**:
#    - Create a new SQLite database named `roster.db`.
#    - Define a table called **Roster** with the following schema:
#      - **Name**: TEXT
#      - **Species**: TEXT
#      - **Age**: INTEGER

# 2. **Insert Data**:
#    - Populate the **Roster** table with the following entries:

# | Name           | Species  | Age |
# |----------------|----------|-----|
# | Benjamin Sisko | Human    | 40  |
# | Jadzia Dax     | Trill    | 300 |
# | Kira Nerys     | Bajoran  | 29  |

# 3. **Update Data**:
#    - Update the `Name` of **Jadzia Dax** to **Ezri Dax**.

# 4. **Query Data**:
#    - Retrieve and display the **Name** and **Age** of all characters where the `Species` is **Bajoran**.

# 5. **Delete Data**:
#    - Remove all characters aged over 100 years from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rank` to the **Roster** table and update the data with the following values:
   
# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

# 7. **Advanced Query**:
#    - Retrieve all characters sorted by their `Age` in descending order.




# ### Task 2

# 1. **Database Creation**:
#    - Create a new SQLite database named `library.db`.
#    - Define a table called **Books** with the following schema:
#      - **Title**: TEXT
#      - **Author**: TEXT
#      - **Year_Published**: INTEGER
#      - **Genre**: TEXT

# 2. **Insert Data**:
#    - Populate the **Books** table with the following entries:

# | Title                  | Author          | Year_Published | Genre      |
# |------------------------|-----------------|----------------|------------|
# | To Kill a Mockingbird  | Harper Lee      | 1960           | Fiction    |
# | 1984                   | George Orwell   | 1949           | Dystopian  |
# | The Great Gatsby       | F. Scott Fitzgerald | 1925        | Classic    |

# 3. **Update Data**:
#    - Update the `Year_Published` of **1984** to **1950**.

# 4. **Query Data**:
#    - Retrieve and display the **Title** and **Author** of all books where the `Genre` is **Dystopian**.

# 5. **Delete Data**:
#    - Remove all books published before the year 1950 from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rating` to the **Books** table and update the data with the following values:

# | Title                  | Rating |
# |------------------------|--------|
# | To Kill a Mockingbird  | 4.8    |
# | 1984                   | 4.7    |
# | The Great Gatsby       | 4.5    |

# 7. **Advanced Query**:
#    - Retrieve all books sorted by their `Year_Published` in ascending order.


from dbm import sqlite3

import os
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
class RosterManager(DatabaseManager):
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        );
        """
        self.execute_query(create_table_query)

    def insert_data(self, name, species, age):
        insert_query = "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?);"
        self.execute_query(insert_query, (name, species, age))

    def update_name(self, old_name, new_name):
        update_query = "UPDATE Roster SET Name = ? WHERE Name = ?;"
        self.execute_query(update_query, (new_name, old_name))

    def query_bajoran(self):
        query = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';"
        return self.fetch_all(query)

    def delete_old_characters(self):
        delete_query = "DELETE FROM Roster WHERE Age > 100;"
        self.execute_query(delete_query)

    def add_rank_column(self):
        add_column_query = "ALTER TABLE Roster ADD COLUMN Rank TEXT;"
        self.execute_query(add_column_query)

    def update_rank(self, name, rank):
        update_rank_query = "UPDATE Roster SET Rank = ? WHERE Name = ?;"
        self.execute_query(update_rank_query, (rank, name))

    def advanced_query(self):
        query = "SELECT * FROM Roster ORDER BY Age DESC;"
        return self.fetch_all(query)

class LibraryManager(DatabaseManager):
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        );
        """
        self.execute_query(create_table_query)

    def insert_data(self, title, author, year_published, genre):
        insert_query = "INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?);"
        self.execute_query(insert_query, (title, author, year_published, genre))

    def update_year_published(self, title, new_year):
        update_query = "UPDATE Books SET Year_Published = ? WHERE Title = ?;"
        self.execute_query(update_query, (new_year, title))

    def query_dystopian(self):
        query = "SELECT Title, Author FROM Books WHERE Genre = 'Dystopian';"
        return self.fetch_all(query)

    def delete_old_books(self):
        delete_query = "DELETE FROM Books WHERE Year_Published < 1950;"
        self.execute_query(delete_query)

    def add_rating_column(self):
        add_column_query = "ALTER TABLE Books ADD COLUMN Rating REAL;"
        self.execute_query(add_column_query)

    def update_rating(self, title, rating):
        update_rating_query = "UPDATE Books SET Rating = ? WHERE Title = ?;"
        self.execute_query(update_rating_query, (rating, title))

    def advanced_query(self):
        query = "SELECT * FROM Books ORDER BY Year_Published ASC;"
        return self.fetch_all(query)
    
class Main:
    
    def run(self):
        # Task 1: Roster Database Operations
        roster_manager = RosterManager("roster.db")
        roster_manager.connect()
        roster_manager.create_table()
        roster_manager.insert_data("Benjamin Sisko", "Human", 40)
        roster_manager.insert_data("Jadzia Dax", "Trill", 300)
        roster_manager.insert_data("Kira Nerys", "Bajoran", 29)
        roster_manager.update_name("Jadzia Dax", "Ezri Dax")
        bajoran_characters = roster_manager.query_bajoran()
        print("Bajoran Characters:", bajoran_characters)
        roster_manager.delete_old_characters()
        roster_manager.add_rank_column()
        roster_manager.update_rank("Benjamin Sisko", "Captain")
        roster_manager.update_rank("Ezri Dax", "Lieutenant")
        roster_manager.update_rank("Kira Nerys", "Major")
        sorted_characters = roster_manager.advanced_query()
        print("Sorted Characters by Age:", sorted_characters)
        roster_manager.close()

        # Task 2: Library Database Operations
        library_manager = LibraryManager("library.db")
        library_manager.connect()
        library_manager.create_table()
        library_manager.insert_data("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
        library_manager.insert_data("1984", "George Orwell", 1949, "Dystopian")
        library_manager.insert_data("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
        library_manager.update_year_published("1984", 1950)
        dystopian_books = library_manager.query_dystopian()
        print("Dystopian Books:", dystopian_books)
        library_manager.delete_old_books()
        library_manager.add_rating_column()
        library_manager.update_rating("To Kill a Mockingbird", 4.8)
        library_manager.update_rating("1984", 4.7)
        library_manager.update_rating("The Great Gatsby", 4.5)
        sorted_books = library_manager.advanced_query()
        print("Sorted Books by Year Published:", sorted_books)
        library_manager.close()

def main():
    main_app = Main()
    main_app.run()

main()

