"""
This module will contains code for time count
"""
import time

""" Time """  ######################################################################


class Time:
    """ Time class contains all the function regarding time measurements of code"""

    def __init__(self):
        self.start_time = time.time()
        self.end_time = time.time()

    def startTime(self):
        """ Start time count """
        self.start_time = time.time()

    def endTime(self):
        """ end time count """
        self.end_time = time.time()

    def totalTime(self):
        """ total time count """
        print("[Time Elapse]: {}".format(self.end_time - self.start_time))

    def wait(self, waiting_time=5):
        """ wait for given time """
        time.sleep(waiting_time)


""" main """  ##########################################################################################################


def main():
    """ This function is used for testing the functionalists of the class and functions """

    t = Time()
    t.startTime()
    t.wait(10)
    t.endTime()
    t.totalTime()


if __name__ == "__main__":
    main()
