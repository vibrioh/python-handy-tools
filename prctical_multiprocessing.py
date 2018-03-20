# ! -*- coding:utf-8 -*-

from prctical_logging import *
import multiprocessing
import time
import random
import math
import sys



def isOdd(n):
    time.sleep(1)
    is_odd = (n % 2 == 0)
    logger.debug("{} is odd: {}".format(n, is_odd))
    return is_odd, n


def isPrime(n):
    if n <= 1:
        # logger.debug("{} is prime: {}".format(n, False))
        return False, n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # logger.debug("{} is prime: {}".format(n, False))
            return False, n
    # logger.debug("{} is prime: {}".format(n, True))
    return True, n


def isFib(num):
    """
    Checks if given number is a fibonacci number.

    @param num  Number to be tested if it is fibonacci number
    @return     Boolean value indicating if given number is a fibonacci number
    """

    time.sleep(TIME_SLEEP)

    x1 = 5 * math.pow(num, 2) + 4
    x2 = 5 * math.pow(num, 2) - 4

    x1_sqrt = math.sqrt(x1)
    x2_sqrt = math.sqrt(x2)

    logger.debug("{} is fibonacci: {}".format(num, ((x1_sqrt * x1_sqrt == x1) or (x2_sqrt * x2_sqrt == x2))))

    return ((x1_sqrt * x1_sqrt == x1) or (x2_sqrt * x2_sqrt == x2)), num


if __name__ == "__main__":
    TIME_SLEEP = float(sys.argv[1])
    cores = multiprocessing.cpu_count()
    logger.debug("CPU cores = " + str(cores))
    pool = multiprocessing.Pool(processes=cores)
    result_list = []
    res = []

    time_start = time.time()

    for i in range(30):
        rn = random.randrange(0, 10000000000000000000000000000)
        result_list.append(pool.apply_async(isFib, (rn,)))
    pool.close()
    pool.join()
    for obj in result_list:
        if obj.get()[0]:
            res.append(obj.get()[1])
    logger.debug("length of result_list is: " + str(len(result_list)))
    logger.debug("length of res is: " + str(len(res)))
    logger.info(res)

    time_now = time.time()

    result_list = []
    res = []

    for i in range(30):
        rn = random.randrange(0, 10000000000000000000000000000)
        result_list.append(isFib(rn))
    for obj in result_list:
        if obj[0]:
            res.append(obj[1])
    logger.debug("length of result_list is: " + str(len(result_list)))
    logger.debug("length of res is: " + str(len(res)))
    logger.info(res)

    time_end = time.time()
    logger.info("multi_async used ---%s seconds---" % (time_now - time_start))
    logger.info("single_sync used ---%s seconds---" % (time_end - time_now))
