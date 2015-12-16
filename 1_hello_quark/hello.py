#!/usr/bin/env python

# Copyright 2015 Datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import datetime
import errno
import json
import os
import platform
import time
import traceback
import uuid

import dateutil.tz
import pyisemail

from quark_threaded_runtime import get_threaded_runtime as get_runtime

import HelloQuark

VERSION = '0.1.1'

def getEmail():
    emailAddress = None

    print("Welcome to Quark!")
    print("")
    print("We've just created you a new Datawire account! We need your email address to wrap")
    print("that up.")
    print("")

    while True:
        sys.stdout.write("Email: ")
        sys.stdout.flush()

        emailAddress = sys.stdin.readline().strip()

        if not emailAddress:
            print("We really do need your email address! We promise not to spam you.")
        elif not pyisemail.is_email(emailAddress):
            print("We really do need a valid email address! We promise not to spam you.")
        else:
            print("Thanks!")
            break

    return emailAddress

def warnAboutDWState(verb, path, exception):
    sys.stderr.write("WARNING: could not %s %s\n    (%s)\n" %
                     (verb, path, exception))
    sys.stderr.write("Your Datawire account state will not be persistent. This may make other\n")
    sys.stderr.write("Datawire tools unhappy.\n")

def getDatawireState():
    # Make sure we have ~/.datawire...
    dwStateDir = os.path.join(os.path.expanduser('~'), '.datawire')

    dwStatePath = os.path.join(dwStateDir, "datawire.json")
    dwState = None
    justCreated = False
    inFile = None

    try:
        inFile = open(dwStatePath, "r")
    except IOError as exception:
        if exception.errno != errno.ENOENT:
            warnAboutDWState("open", dwStatePath, exception)

    if inFile != None:
        try:
            dwState = json.load(inFile)
        except ValueError as exception:
            warnAboutDWState("load", dwStatePath, exception)
        except IOError as exception:
            warnAboutDWState("read", dwStatePath, exception)

    if inFile != None:
        inFile.close()

    if not dwState:             # Implies that the file was empty
        justCreated = True

        emailAddress = getEmail()

        dwState = {
            'userID': str(uuid.uuid4()).upper(),
            'emailAddress': emailAddress
        }

    if justCreated:
        haveStateDir = False

        try:
            os.makedirs(dwStateDir)
            haveStateDir = True
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                warnAboutDWState("create", dwStateDir, exception)
            else:
                haveStateDir = True

        if haveStateDir:
            try:
                outFile = open(dwStatePath, "w")
                json.dump(dwState, outFile, indent=4, separators=(',',':'), sort_keys=True)
                outFile.close()
            except IOError as exception:
                warnAboutDWState("save dwState to", dwStatePath, exception)

    if not dwState:
        raise RuntimeError("No dwState could be determined (impossible!)")

    return dwState

def now8601():
    # Yeek.
    return datetime.datetime.now(dateutil.tz.tzlocal()).isoformat()

def osVersion():
    sysName = platform.system()

    if sysName == 'Darwin':
        release, versioninfo, machine = platform.mac_ver()

        return "MacOS X %s (%s)" % (release, machine)
    else:
        # Should be Linux

        distname, version, id = platform.linux_distribution()

        if distname:
            return "%s %s (%s)" % (distname, version, platform.machine())
        else:
            # Oh well.
            return "%s %s (%s)" % (sysName, platform.release(), platform.machine())

def pythonVersion():
    return "Python %s" % platform.python_version()

def main():
    runtime = get_runtime()
    runtime.launch()

    try:
        client = HelloQuark.HelloClient(runtime, HelloQuark.defaultURL())

        dwState = getDatawireState()

        request = HelloQuark.Request()
        request.user_id = dwState['userID']
        request.event_time = now8601()
        request.email_address = dwState['emailAddress']
        request.runtime_info = pythonVersion()
        request.system_info = osVersion()
        request.quark_version = "X.Y.Z"
        request.app_version = VERSION

        request.query = 'Hello world'

        print("Request: %s" % request)

        response = client.helloQuark(request)

        print("%s %s" % (response.status, response.message))

        # if response.stack:
        #     print("Stack:\n    %s" % "\n    ".join(response.stack))
    except Exception as exception:
        traceback.print_exc()
        print("")
        print("Hello Quark! did not work; your Datawire setup may not be functional.")
        print("Contact support@datawire.io if you think this is a problem we can help with.")

    runtime.finish()

if __name__ == '__main__':
    main()
