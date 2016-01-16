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

import hello
import sys

from quark_threaded_runtime import get_runtime

def main():
    runtime = get_runtime()

    # "http://hello.datawire.io/" is the URL of the Hello Quark! cloud 
    # service run by Datawire, Inc. to serve as a simple first test. We
    # promise that we won't be evil if you talk to our server! 
    #
    # You can test completely locally, too: 
    # - comment out the http://hello.datawire.io line
    # - uncomment the http://127.0.0.1:12216/hello line
    # - fire up the local version of the server by running
    #
    #   python etc/hello_server.py
    #
    # from the main project directory.
    
    client = hello.HelloClient(runtime, "http://hello.datawire.io/")
    # client = hello.HelloClient(runtime, "http://127.0.0.1:12216/hello")
    
    request = hello.Request()
    request.text = "Hello Quark! (lang: python, version: %s)" % '.'.join(str(x) for x in sys.version_info[0:3])
    print "Request says %r" % request.text

    response = client.hello(request)
    print "Response says %r" % response.result

if __name__ == '__main__':
    main()
