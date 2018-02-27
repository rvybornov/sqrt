from math import sqrt

import sys
import logging
import logging.config
import argparse

logging.config.fileConfig('sqrtlogging.conf')
logger = logging.getLogger("root")

parser = argparse.ArgumentParser()
parser.add_argument('a', help='first coefficient of trinomial')
parser.add_argument('b', help='second coefficient of trinomial')
parser.add_argument('c', help='third coefficient of trinomial')   
args = parser.parse_args()
              
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3]) 

if a == 0:
    logger.debug("It's not a square trinomial")
else:
    q = b**2 - 4*a*c
    if q < 0:
        logger.debug("There are no rational roots")
    else:          
        p = sqrt(q)
        x1 = (p - b)/(2*a)
        x2 = (-p - b)/(2*a)
        logger.info(x1)
        logger.info(x2)














