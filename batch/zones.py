from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('zones') \
    .getOrCreate()

# read without telling Spark there's a header - watch the column names
df = spark.read.csv('taxi_zone_lookup.csv')
print("Without header option:")
df.show(5)

# now read it properly
df = spark.read \
    .option("header", "true") \
    .csv('taxi_zone_lookup.csv')
print("With header option:")
df.show(5)

# write it out as parquet
df.write.mode("overwrite").parquet('zones')

print("Done - check the 'zones' folder")

input("Press Enter to stop Spark (keep this open to check the UI)...")
spark.stop()
