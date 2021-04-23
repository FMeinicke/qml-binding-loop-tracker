#!/bin/env python3

#This program prints a backtrace of binding evaluations
# Usage ./binding-loop-tracker.py applicationName
# for example ./binding-loop-tracker.py qmlscene someFile.qml

import sys
import subprocess


#to keep everything in one file this has two "mains"
#a launcher than starts GDB with this as a --command argument
#and the code that should be run in GDB

mode = "launcher"

try:
    import gdb
    mode = "gdb"
except:
    pass


def convertQString(val):
    d = val['d']
    data = d.reinterpret_cast(gdb.lookup_type('char').pointer()) + d['offset']
    data_len = d['size'] * gdb.lookup_type('unsigned short').sizeof
    return data.string('utf-16', 'replace', data_len)


def breakpointHandler(event):
    #stopped for some other reason, ignore
    frame = gdb.newest_frame()
    if frame.name() != "QQmlAbstractBinding::printBindingLoopError":
        return

    print("===== Binding loop detected - printing backtrace =====")

    i = 0
    while True:
        frame = frame.older()
        if frame == None or not frame.is_valid():
            break

        #print (frame.name()) # enable to see full trace between binding updates
        if frame.name() == "QQmlBinding::update":
            currentBinding = frame.read_var("this")
            eval_string = "(*(QQmlBinding*)("+str(currentBinding)+")).expressionIdentifier()"
            identifier = convertQString(gdb.parse_and_eval(eval_string))

            print("#" + str(i) + " - " + identifier)
            i += 1

    print()
    gdb.execute("continue")


def gdbMain():
    gdb.events.stop.connect(breakpointHandler)
    breakpoint = gdb.Breakpoint("QQmlAbstractBinding::printBindingLoopError")
    gdb.execute("run")


def launcherMain():
    args = sys.argv
    selfName = args.pop(0)
    x = ["gdb", "--command", selfName, "--args"] + args
    subprocess.call(x)


if __name__ == "__main__":
    if mode == "gdb":
        gdbMain()
    else:
        launcherMain()
