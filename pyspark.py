shdf = spark.read.json("hdfs://yourhdpserver:8020/spark2-history")

shdf.printSchema()

shdf.createOrReplaceTempView("sparklogs")

stuffdf = spark.sql("SELECT * FROM sparklogs")

stuffdf.count()
