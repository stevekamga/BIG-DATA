import sys

from pyspark import SparkContext, SparkConf



if __name__ == "__main__":

	#Create Spark contect with Spark configuration
	conf = SparkConf().setAppName("Word Count with Python")
	sc = SparkContext(conf=conf)


	# read in text file and split each documents into words
	wordlist = sc.textFile("/home/hadoop/opt/PythonScripts/spark/text.txt").flatMap(lambda line: line.split(""))

	# Count the occurence of each word
	wordCounts = wordlist.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a +b)

	wordCounts.saveAsTextFile("/home/hadoop/opt/PythonScripts/spark/")

