data = range(1, 1000) 

rdd = sc.parallelize(data)

odd = rdd.filter(lambda n: n % 2 != 0).toDF()
