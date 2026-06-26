# #### **Merging and Joining**
# 1. **Inner Join on Chinook Database**
#    - Load the `chinook.db` database.
#    - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
#    - Find the total number of invoices for each customer.

# 2. **Outer Join on Movie Data**
#    - Load the `movie.csv` file.
#    - Create two smaller DataFrames:
#      - One with only `director_name` and `color`.
#      - Another with `director_name` and `num_critic_for_reviews`.
#    - Perform a left join and then a full outer join on `director_name`.
#    - Count how many rows are in the resulting DataFrames for each join type.

# ---

# #### **Grouping and Aggregating**
# 1. **Grouped Aggregations on Titanic**
#    - Group passengers by `Pclass` and calculate the following:
#      - Average age.
#      - Total fare.
#      - Count of passengers.
#    - Save the results to a new DataFrame.

# 2. **Multi-level Grouping on Movie Data**
#    - Group the movies by `color` and `director_name`.
#    - Find:
#      - Total `num_critic_for_reviews` for each group.
#      - Average `duration` for each group.

# 3. **Nested Grouping on Flights**
#    - Group flights by `Year` and `Month` and calculate:
#      - Total number of flights.
#      - Average arrival delay (`ArrDelay`).
#      - Maximum departure delay (`DepDelay`).

# ---

# #### **Applying Functions**
# 1. **Apply a Custom Function on Titanic**
#    - Write a function to classify passengers as `Child` (age < 18) or `Adult`.
#    - Use `apply` to create a new column, `Age_Group`, with these values.

# 2. **Normalize Employee Salaries**
#    - Load the `employee.csv` file.
#    - Normalize the salaries within each department.

# 3. **Custom Function on Movies**
#    - Write a function that returns `Short`, `Medium`, or `Long` based on the duration of a movie:
#      - `Short`: Less than 60 minutes.
#      - `Medium`: Between 60 and 120 minutes.
#      - `Long`: More than 120 minutes.
#    - Apply this function to classify movies in the `movie.csv` dataset.

# ---

# #### **Using `pipe`**
# 1. **Pipeline on Titanic**
#    - Create a pipeline to:
#      - Filter passengers who survived (`Survived == 1`).
#      - Fill missing `Age` values with the mean.
#      - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.

# 2. **Pipeline on Flights**
#    - Create a pipeline to:
#      - Filter flights with a departure delay greater than 30 minutes.
#      - Add a column `Delay_Per_Hour` by dividing the delay by the scheduled flight duration.

import sqlite3
import pandas as pd

# --- 1. Inner Join on Chinook Database ---
# sqlite bazaga ulanamiz
conn = sqlite3.connect("chinook.db")

# Jadvallarni DataFrame-ga yuklaymiz
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

# Inner join amali
inner_joined = pd.merge(
    customers_df, invoices_df, on="CustomerId", how="inner"
)

# Har bir mijoz uchun jami hisob-fakturalar soni
invoice_counts = (
    inner_joined.groupby("CustomerId").size().reset_index(name="Total_Invoices")
)
print("Chinook Inner Join natijasi:\n", invoice_counts.head())
conn.close()


# --- 2. Outer Join on Movie Data ---
# CSV faylni yuklash
movie_df = pd.read_csv("movie.csv")

# Ikkita kichik DataFrame yaratish
df1 = movie_df[["director_name", "color"]].drop_duplicates()
df2 = movie_df[["director_name", "num_critic_for_reviews"]].drop_duplicates()

# Left join va satrlar soni
left_joined = pd.merge(df1, df2, on="director_name", how="left")
print(f"\nLeft Join satrlar soni: {len(left_joined)}")

# Full outer join va satrlar soni
outer_joined = pd.merge(df1, df2, on="director_name", how="outer")
print(f"Full Outer Join satrlar soni: {outer_joined.shape[0]}")

# --- 1. Grouped Aggregations on Titanic ---
titanic_df = pd.read_csv("titanic.csv")  # fayl nomiga qarab o'zgartiring

titanic_agg = (
    titanic_df.groupby("Pclass")
    .agg(
        Average_Age=("Age", "mean"),
        Total_Fare=("Fare", "sum"),
        Passenger_Count=("PassengerId", "count"),
    )
    .reset_index()
)

print("Titanic guruhlash natijasi:\n", titanic_agg)


# --- 2. Multi-level Grouping on Movie Data ---
movie_agg = (
    movie_df.groupby(["color", "director_name"])
    .agg(
        Total_Critics=("num_critic_for_reviews", "sum"),
        Average_Duration=("duration", "mean"),
    )
    .reset_index()
)

print("\nMovie ko'p bosqichli guruhlash:\n", movie_agg.head())


# --- 3. Nested Grouping on Flights ---
flights_df = pd.read_csv("flights.csv")  # fayl nomiga qarab o'zgartiring

flights_agg = (
    flights_df.groupby(["Year", "Month"])
    .agg(
        Total_Flights=("FlightNum", "count"),  # yoki mos ID ustun
        Avg_ArrDelay=("ArrDelay", "mean"),
        Max_DepDelay=("DepDelay", "max"),
    )
    .reset_index()
)

print("\nFlights (Parvozlar) guruhlash natijasi:\n", flights_agg.head())

# --- 1. Apply a Custom Function on Titanic ---
def classify_age(age):
    if pd.isna(age):
        return "Unknown"
    return "Child" if age < 18 else "Adult"


titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)
print("Titanic Age_Group ustuni qo'shildi:\n", titanic_df[["Age", "Age_Group"]].head())


# --- 2. Normalize Employee Salaries ---
employee_df = pd.read_csv("employee.csv")


# Har bir departament ichida maoshni normallashtirish (Min-Max scaling) funksiyasi
def normalize(group):
    # Agar guruhda min va max teng bo'lsa, xatolik bermasligi uchun tekshiramiz
    if group.max() == group.min():
        return 0.0
    return (group - group.min()) / (group.max() - group.min())


employee_df["Normalized_Salary"] = employee_df.groupby("Department")[
    "Salary"
].transform(normalize)
print("\nEmployee Normallashgan Maoshlar:\n", employee_df.head())


# --- 3. Custom Function on Movies ---
def classify_duration(duration):
    if pd.isna(duration):
        return "Unknown"
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"


movie_df["Duration_Class"] = movie_df["duration"].apply(classify_duration)
print(
    "\nMovie davomiyligi klassifikatsiyasi:\n",
    movie_df[["duration", "Duration_Class"]].head(),
)

# --- 1. Pipeline on Titanic ---
def process_titanic(df):
    d = df.copy()
    # 1. Faqat omon qolganlarni filterlash
    d = d[d["Survived"] == 1]
    # 2. Age ustunidagi bo'shliqlarni o'rtacha qiymat bilan to'ldirish
    d["Age"] = d["Age"].fillna(d["Age"].mean())
    # 3. Yangi Fare_Per_Age ustunini yaratish
    d["Fare_Per_Age"] = d["Fare"] / d["Age"]
    return d


titanic_piped = titanic_df.pipe(process_titanic)
print("Titanic Pipeline natijasi:\n", titanic_piped[["Survived", "Age", "Fare_Per_Age"]].head())


# --- 2. Pipeline on Flights ---
def process_flights(df):
    d = df.copy()
    # 1. Kechikish 30 daqiqadan ko'p bo'lgan parvozlarni filterlash
    d = d[d["DepDelay"] > 30]
    # 2. Delay_Per_Hour ustunini hisoblash (Kechikish / Rejali davomiylik)
    # AirTime yoki ScheduledDuration ustunidan foydalaniladi (bu yerda 'AirTime' deb olindi)
    d["Delay_Per_Hour"] = d["DepDelay"] / (d["AirTime"] / 60)
    return d


flights_piped = flights_df.pipe(process_flights)
print("\nFlights Pipeline natijasi:\n", flights_piped[["DepDelay", "AirTime", "Delay_Per_Hour"]].head())
