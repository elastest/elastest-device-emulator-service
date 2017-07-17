#Coap Client example
#PYTHONPATH=../:../../src:../../../futile/src python SimpleTestClient.py
from coap import CoapClient

import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContentInstances_Test")

client = CoapClient("coap://localhost:4000")

results = 0
def resultPrinter(result):
    global results
    results += 1
    # print "got result ", result
    # print result


errors = 0
def errorPrinter(error):
    global errors
    errors += 1
    # print "got error", error
    # print error

# c == nr of iterations
c = input("How many iterations?\n")
print "Press enter when you think the test is over. Starting in 2 seconds..."
time.sleep(2)

"""Create X contentInstances"""
# create container first, wait for completion with .get()
client.post("m2m/containers", '{"container": {"id":"myCon", "maxNrOfInstances":-1}}', accept='application/json',
            content_type='application/json').then(resultPrinter, errorPrinter).get()


# reset errors and results counters
errors = 0
results = 0

for i in range(c):
    client.post("m2m/containers/myCon/contentInstances", '{"cksalndjksad": "sdjfnjdngbsnpogjsgsog"}',
                accept='application/json', content_type='application/json').then(resultPrinter, errorPrinter)

# wait for user input instead of finishing execution


x = raw_input("")
print
print "DONE"
print "####################"
print "iterations:", c
print "    sucess:", results
print "    errors:", errors
print "####################"
print

# delete container at the end
client.delete("m2m/containers/myCon", accept='application/json').then(resultPrinter, errorPrinter).get()
