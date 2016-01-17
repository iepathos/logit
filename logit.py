#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse
from datetime import datetime
from subprocess import Popen, PIPE


log_filename = os.path.expanduser('~/logit.log')


class Logit(object):

    def __init__(self, cmd, log_filename=log_filename, silent=False):
        self.log_filename = log_filename
        self.cmd = cmd
        self.cmd_array = cmd.split(" ")
        self.silent = silent

    def create_file_if_not_found(self, filename):
        if os.path.dirname(filename) != "":
            os.makedirs(os.path.dirname(filename), exist_ok=True)

    def stream_command(self):
        execution_str = "Executing '%s'" % self.cmd
        if not SILENT:
            print(execution_str)
        self.create_file_if_not_found(self.log_filename)
        with open(self.log_filename, 'a') as f:
            if not SILENT:
                print("Saving output to %s" % self.log_filename)
            f.write(execution_str +
                    " - " +
                    str(datetime.utcnow()) + '\n')
            with Popen(self.cmd_array,
                       stdout=PIPE,
                       bufsize=1,
                       universal_newlines=True) as p:
                for line in p.stdout:
                    f.write(line)


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
        logit.stream_command()
    else:
        logit = Logit(args.cmd, log_filename, SILENT)
        logit.stream_command()
