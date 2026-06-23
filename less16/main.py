# ### Homework: Pandas Basics

# #### Part 1: Reading Files  
# 1. **`chinook.db`**  
#    - Use the `sqlite3` library to connect to the database.  
#    - Read the `customers` table into a pandas DataFrame. Display the first 10 rows.  

# 2. **`iris.json`**  
#    - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.  

# 3. **`titanic.xlsx`**  
#    - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.  

# 4. **Flights parquet file**  
#    - Read the Parquet file into a DataFrame and use `info` to summarize it.  

# 5. **`movie.csv`**  
#    - Load the CSV file into a DataFrame and display a random sample of 10 rows.

# ---

# #### Part 2: Exploring DataFrames  
# 1. Using the DataFrame from **`iris.json`**:  
#    - Rename the columns to lowercase.  
#    - Select only the `sepal_length` and `sepal_width` columns.  

# 2. From the **`titanic.xlsx`** DataFrame:  
#    - Filter rows where the age of passengers is above 30.  
#    - Count the number of male and female passengers (`value_counts`).  

# 3. From the **Flights parquet file**:  
#    - Extract and print only the `origin`, `dest`, and `carrier` columns.  
#    - Find the number of unique destinations.  

# 4. From the **`movie.csv`** file:  
#    - Filter rows where `duration` is greater than 120 minutes.  
#    - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  

# ---

# #### Part 3: Challenges and Explorations  
 
# - From **`iris.json`**: Calculate the mean, median, and standard deviation for each numerical column.  
# - From **`titanic.xlsx`**: Find the minimum, maximum, and sum of passenger ages.  

# - From **`movie.csv`**:  
#     - Identify the director with the highest total `director_facebook_likes`.  
#     - Find the 5 longest movies and their respective directors.  

# - From **Flights parquet file**:  
#     - Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.


import pandas as pd
import sqlite3

# 1. chinook.db (SQLite Ma'lumotlar bazasi)
# Ma'lumotlar bazasiga ulanamiz
conn = sqlite3.connect('chinook.db')
# customers jadvalini o'qiymiz
df_chinook = pd.read_sql_query("SELECT * FROM customers", conn)
print("--- Chinook (Birinchi 10 ta qator) ---")
print(df_chinook.head(10))
conn.close() # Ulanishni yopamiz

# 2. iris.json (JSON fayl)
df_iris = pd.read_json('iris.json')
print("\n--- Iris Dataset ---")
print(f"Shakli (Shape): {df_iris.shape}")
print(f"Ustun nomlari: {df_iris.columns.tolist()}")

# 3. titanic.xlsx (Excel fayl)
df_titanic = pd.read_excel('titanic.xlsx')
print("\n--- Titanic (Birinchi 5 ta qator) ---")
print(df_titanic.head(5))

# 4. Flights parquet file (Parquet fayl)
# Izoh: fayl nomi 'flights.parquet' deb olindi
df_flights = pd.read_parquet('flights.parquet')
print("\n--- Flights Info ---")
print(df_flights.info())

# 5. movie.csv (CSV fayl)
df_movie = pd.read_csv('movie.csv')
print("\n--- Movie (Tasodifiy 10 ta qator) ---")
print(df_movie.sample(10))


# 1. Iris Dataframe ustida amallar
# Ustun nomlarini kichik harflarga o'tkazamiz
df_iris.columns = df_iris.columns.str.lower()
# Faqat sepal_length va sepal_width ustunlarini tanlaymiz
df_iris_selected = df_iris[['sepal_length', 'sepal_width']]

# 2. Titanic Dataframe ustida amallar
# Yoshi 30 dan katta bo'lgan yo'lovchilarni filtrlash
titanic_above_30 = df_titanic[df_titanic['Age'] > 30]
# Erkak va ayol yo'lovchilar sonini hisoblash
gender_counts = df_titanic['Sex'].value_counts()
print("\n--- Titanic: Jinslar bo'yicha soni ---")
print(gender_counts)

# 3. Flights Dataframe ustida amallar
# Faqat origin, dest, va carrier ustunlarini ajratib olish
df_flights_selected = df_flights[['origin', 'dest', 'carrier']]
# Unikal (takrorlanmas) yo'nalishlar soni
unique_destinations = df_flights['dest'].nunique()
print(f"\nFlights: Unikal yo'nalishlar soni: {unique_destinations}")

# 4. Movie Dataframe ustida amallar
# Davomiyligi 120 daqiqadan ko'p bo'lgan filmlar
long_movies = df_movie[df_movie['duration'] > 120]
# director_facebook_likes bo'yicha kamayish tartibida saralash
long_movies_sorted = long_movies.sort_values(by='director_facebook_likes', ascending=False)



# 1. Iris statistikasi
# Har bir sonli ustun uchun o'rtacha qiymat (mean), median va standart og'ish (std)
# Izoh: 'species' ustuni matnli bo'lsa, uni hisobga olmaydi
iris_stats = df_iris.describe().loc[['mean', '50%', 'std']] 
# 50% bu median hisoblanadi
print("\n--- Iris Statistikasi ---")
print(iris_stats)

# 2. Titanic statistikasi (Yosh bo'yicha)
age_min = df_titanic['Age'].min()
age_max = df_titanic['Age'].max()
age_sum = df_titanic['Age'].sum()
print(f"\nTitanic: Eng kichik yosh: {age_min}, Eng katta yosh: {age_max}, Yoshlar yig'indisi: {age_sum}")

# 3. Movie tahlili
# Eng ko'p jami layk to'plagan rejissyor (Director)
# Rejissyorlar bo'yicha guruhlab, layklarni qo'shamiz va eng kattasini topamiz
top_director = df_movie.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print(f"\nMovie: Eng ko'p layk olgan rejissyor: {top_director}")

# Eng uzun 5 ta film va ularning rejissyorlari
top_5_longest = df_movie.sort_values(by='duration', ascending=False)[['movie_title', 'director_name', 'duration']].head(5)
print("\n--- Eng uzun 5 ta film ---")
print(top_5_longest)

# 4. Flights: Bo'sh qiymatlar bilan ishlash
# Missing (bo'sh) qiymatlarni tekshirish
missing_values = df_flights.isnull().sum()
print("\n--- Flights: Bo'sh qiymatlar soni (har bir ustunda) ---")
print(missing_values)

# Biror bir sonli ustundagi bo'sh qiymatlarni o'sha ustunning o'rtacha qiymati bilan to'ldirish
# Misol tariqasida 'dep_delay' (uchish kechikishi) ustunini olamiz:
if 'dep_delay' in df_flights.columns:
    mean_delay = df_flights['dep_delay'].mean()
    df_flights['dep_delay'] = df_flights['dep_delay'].fillna(mean_delay)
    print("\nFlights: 'dep_delay' ustunidagi bo'sh joylar o'rtacha qiymat bilan to'ldirildi.")