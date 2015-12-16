/*
-- Copyright 2015 Datawire. All rights reserved.
-- 
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
-- 
--    http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
*/

@version("1.0.0")
package hello {

    @doc("A value class for Request data for the hello service.")
    class Request {
        String text;
    }

    @doc("A value class for Response data from the hello service.")
    class Response {
        @doc("A greeting from the hello service.")
        String result;
    }

    @doc("The hello service.")
    interface Hello extends Service {

        @doc("Respond to a hello request.")
        @delegate(self.rpc) // XXX: The "self." in front of rpc is a workaround.
        Response hello(Request request);

    }

    @doc("A client adapter for the hello service.")
    class HelloClient extends Client, Hello {}

    @doc("A server adapter for the hello service.")
    class HelloServer extends Server<Hello> {}

}