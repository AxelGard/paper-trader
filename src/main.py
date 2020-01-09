from traders import randy_random, trader, cassandra_classic
import api_controller
import json


if __name__ == '__main__':
    print(" [*] paper-trader started ")
    cassandra_classic.run_cassandra()
    #randy_random.run_randy()
    print(" [*] paper-trader stoped")
