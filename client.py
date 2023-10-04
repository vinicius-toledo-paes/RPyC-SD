import time
import rpyc
import sys
import os

import random


#Questão 1 e 2
#if len(sys.argv) < 2:
#    exit("Usage {} SERVER".format(sys.argv[0]))
#server = sys.argv[1]
#conn = rpyc.connect(server,18861)
#print(conn.root)
#print(conn.root.get_answer())
#print(conn.root.the_real_answer_though) 


#Questão 3
#if len(sys.argv) < 2:
#    exit("Usage {} SERVER".format(sys.argv[0]))
#server = sys.argv[1]
#conn = rpyc.connect(server,18861)
#print(conn.root.get_question())


#Questões restantes
start = time.time()
if len(sys.argv) < 3:
    exit("Usage {} SERVER".format(sys.argv[0]))
n = int(sys.argv[2])
v = []
for i in range(n):
    v.append(random.randrange(n))
server = sys.argv[1]
conn = rpyc.connect(server, 18861)
print(conn.root.get_sum(v))
end = time.time()
print(end-start)