#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
from subprocess import check_output
from datetime import datetime

log_filename = os.path.expanduser('~/logit.log')


class Logit(object):

    def __init__(self, cmd, log_filename=log_filename):
        self.log_filename = log_filename
        self.cmd = cmd
        self.cmd_array = cmd.split(" ")

    def check_log(self, func, text):
        try:
            os.makedirs(os.path.dirname(self.log_filename), exist_ok=True)
        except:
            pass
        func(self.log_filename, text)

    def add_to_log(self, file_handle, text):
        with open(file_handle, "a") as f:
            f.write(str(text))

    def log(self, text):
        self.check_log(self.add_to_log, text)

    def execute_command(self):
        execution_str = "Executing '%s'" % self.cmd
        print(execution_str)
        output = check_output(self.cmd_array).decode("utf-8")
        print("Saving output to log %s" % self.log_filename)
        self.log(str(datetime.utcnow()) +
                 " - " + execution_str +
                 "\n" + output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Logit - An easy to use logging wrapper for commandline applications'
        )
    parser.add_argument("cmd")
    parser.add_argument("--log", "-l")

    args = parser.parse_args()
    if args.log:
        logit = Logit(args.cmd, os.path.expanduser(args.log))
        logit.execute_command()
    else:
        logit = Logit(args.cmd, log_filename)
        logit.execute_command()
