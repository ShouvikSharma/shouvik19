from pyspark.sql import SparkSession    
from pyspark.sql.functions import col

# create a spark session
spark = SparkSession.builder.appName("WordSortDF").getOrCreate()

# Sample input data (replace this with your actual data or load from a file)
data = [("apple orange banana",),
        ("grape kiwi cherry",),
        ("pear mango pineapple",)]

# create a dataframe
df = spark.createDataFrame(data, ["words"])

# split the words into individual rows
df_split = df.SelectExpr("explode(split(words, ' ')) as word")

# Sort the words in aplhabetical order
df_sorted = df_split.orderBy("word")

# show the result
df_sorted.show(truncate=False)