from pyspark.sql import SparkSession
import os
import sys

SPARK_VERSION = '3.4'
DELTA_VERSION = '2.4.0'  # Adjust the Delta version based on compatibility

SUBMIT_ARGS = f"--packages org.apache.hadoop:hadoop-aws:3.3.2,io.delta:delta-core_2.12:{DELTA_VERSION} pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = SUBMIT_ARGS
os.environ['PYSPARK_PYTHON'] = sys.executable

# Use --packages and --conf options directly in PySpark code
spark = SparkSession.builder \
    .appName("DeltaReadExample") \
    .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension') \
    .config('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog') \
    .getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://127.0.0.1:9000/")
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "admin")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "password")
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider",
                                     "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")

# Read data from Delta table
delta_table_path = "s3a://warehouse/database=default/table_name=sales"
spark.read.format("delta").load(delta_table_path).createTempView("temp")

spark.sql("select salesid, referral from temp").show()

