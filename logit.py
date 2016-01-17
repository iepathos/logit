#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse
from subprocess import check_output
from datetime import datetime

log_filename = os.path.expanduser('~/logit.log')


class Logit(object):

    def __init__(self, cmd, log_filename=log_filename, silent=False):
        self.log_filename = log_filename
        self.cmd = cmd
        self.cmd_array = cmd.split(" ")
        self.silent = silent

    def check_log(self, func, text):
        if os.path.dirname(self.log_filename) != "":
            os.makedirs(os.path.dirname(self.log_filename), exist_ok=True)
        func(self.log_filename, text)

    def add_to_log(self, file_handle, text):
        with open(file_handle, "a") as f:
            f.write(str(text))

    def log(self, text):
        self.check_log(self.add_to_log, text)

    def execute_command(self):
        execution_str = "Executing '%s'" % self.cmd
        if not SILENT:
            print(execution_str)
        output = check_output(self.cmd_array).decode("utf-8")
        if not SILENT:
            print("Saving output to log %s" % self.log_filename)
        self.log(str(datetime.utcnow()) +
                 " - " + execution_str +
                 "\n" + output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Logit - An easy to use logging wrapper for command line applications'
        )
    parser.add_argument("cmd")
    parser.add_argument("--log", "-l")
    parser.add_argument("--silent", "-s", action='store_true')

    args = parser.parse_args()
    SILENT = False
    if args.silent:
        SILENT = True

    if args.log:
        logit = Logit(args.cmd, os.path.expanduser(args.log), SILENT)
        logit.execute_command()
    else:
        logit = Logit(args.cmd, log_filename, SILENT)
        logit.execute_command()
