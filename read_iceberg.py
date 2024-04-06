from pyspark.sql import SparkSession
import os
import sys

SPARK_VERSION = '3.4'
ICEBERG_VERSION = '0.12.0'  # Adjust the Iceberg version based on compatibility

SUBMIT_ARGS = f"--packages org.apache.hadoop:hadoop-aws:3.3.2,org.apache.iceberg:iceberg-spark3-runtime:{ICEBERG_VERSION} pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = SUBMIT_ARGS
os.environ['PYSPARK_PYTHON'] = sys.executable

# Use --packages and --conf options directly in PySpark code
spark = SparkSession.builder \
    .appName("IcebergReadExample") \
    .config("spark.sql.catalog.ic_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://127.0.0.1:9000/")
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "admin")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "password")
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider",
                                     "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")

# Read data from Iceberg table
iceberg_table_path = "s3a://warehouse/database=default/table_name=sales"
df = spark.read.format("iceberg").load(iceberg_table_path)

# Show DataFrame
df.show()
