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

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

class HelloRpcHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_type = 'text/plain'

        if self.path in ['/hello']:
            msg = self.rfile.read(int(self.headers.getheader('Content-Length')))
            print("---> received message: {}".format(msg))
          
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.wfile.write('\n')
            self.wfile.write('Hello from Datawire!\n')
        else:
            self.send_response(404)

def main(args):
    port = 12216
    if len(args) >= 2:
        port = int(args[1])
  
    print("---> starting hello rpc server (port: {})".format(port))
    server = HTTPServer(('127.0.0.1', port), HelloRpcHandler)
    server.serve_forever()

if __name__ == "__main__":
    import sys
    main(sys.argv)
