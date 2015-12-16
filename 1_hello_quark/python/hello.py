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

    client = hello.HelloClient(runtime, "http://127.0.0.1:8910/hello")
    request = hello.Request()
    request.text = "Hello Quark! (lang: python, version: %s)" % '.'.join(str(x) for x in sys.version_info[0:3])
    print "Request says %r" % request.text

    response = client.hello(request)
    print "Response says %r" % response.result

    runtime.join()


if __name__ == '__main__':
    main()
