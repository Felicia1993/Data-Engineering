%pip install dbldatagen
import dbldatagen as dg
from pyspark.sql.types import StructType, StructField,  StringType

shuffle_partitions_requested = 8
partitions_requested = 8
data_rows = 10000000

spark.sql("""Create table if not exists test_vehicle_data(
                name string, 
                serial_number string, 
                license_plate string, 
                email string
                ) using Delta""")

table_schema = spark.table("test_vehicle_data").schema

print(table_schema)
  
dataspec = (dg.DataGenerator(spark, rows=10000000, partitions=8)
            .withSchema(table_schema))

dataspec = (
    dataspec.withColumnSpec("name", percentNulls=0.01, template=r"\\w \\w|\\w a. \\w")
    .withColumnSpec(
        "serial_number", minValue=1000000, maxValue=10000000, prefix="dr", random=True
    )
    .withColumnSpec("email", template=r"\\w.\\w@\\w.com")
    .withColumnSpec("license_plate", template=r"\\n-\\n")
)
df1 = dataspec.build()

df1.write.format("delta").mode("overwrite").saveAsTable("test_vehicle_data")
