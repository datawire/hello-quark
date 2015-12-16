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
package HelloQuark {
    
    class Request {
        String user_id;
        String event_time;
        String email_address;
        String runtime_info;
        String system_info;
        String quark_version;
        String app_version;
        String query;
    }

    class Response {
        String status;
        String message;
    }

    String defaultURL() {
        return "https://exfc0lkzc6.execute-api.us-east-1.amazonaws.com/prod/HelloQuark";
    }

    interface HelloQuark extends Service {
        @delegate(self.rpc)
        Response helloQuark(Request request);
    }

    class HelloClient extends Client, HelloQuark {}
} 
