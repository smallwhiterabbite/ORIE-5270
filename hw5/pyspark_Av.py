import re
from pyspark import SparkConf, SparkContext


conf = SparkConf()
sc = SparkContext(conf=conf)


def matrix_multiplication(txt_file1, txt_file2):
    """
    Calculate A*v
    :param txt_file1: A txt file including matrix, with index
    :param txt_file2: A txt file including vector, with index
    :return: An RDD object of A*v
    """
    f1 = sc.textFile(txt_file1).map(lambda l: [float(x) for x in l.split(",")])
    f2 = sc.textFile(txt_file2).map(lambda l: l.split(","))

    A = f1.map(lambda l: [(l[0], (l[i], i)) for i in range(1, len(l))])
    A = A.flatMap(lambda l: f(l))
    v = f2.map(lambda l: [(l[0], (l[i], i)) for i in range(1, len(l))])
    v = v.flatMap(lambda l: [(i, l[i]) for i in range(1, len(l))])

    def f(x):
        for a in x:
            yield a[1][1], (a[0], a[1][0])

    Av = A.join(v)
    Av = Av.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1]))
    Av = Av.reduceByKey(lambda x, y: x + y)

    return Av.collect()


if __name__ == "__main__":

    product = matrix_multiplication("A.txt", 'B.txt')
    product.saveAsTextFile("product.txt")

