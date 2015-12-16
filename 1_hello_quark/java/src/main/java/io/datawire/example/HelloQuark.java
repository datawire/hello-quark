/*
Copyright 2015 Datawire. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package io.datawire.example;

import hello.Response;
import io.datawire.quark.netty.QuarkNettyRuntime;
import hello.*;

public class HelloQuark {
  public static void main(String... args) throws Exception {
    io.datawire.quark.runtime.Runtime runtime = new QuarkNettyRuntime();

    HelloClient client = new HelloClient(runtime, "http://localhost:12216/hello");
    Request request = new Request();
    request.text = "Hello Quark! (lang: java, version: " + System.getProperty("java.version") + ")";

    Response response = client.hello(request);
    System.out.println(response.result);
  }
}