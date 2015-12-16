# Hello, Quark!

A sample of Datawire's Quark programming language meant to get you started quickly!

# Getting Started

Datawire's Quark programming language compiler is required for all of these examples. Please install Quark before proceeding: `pip install datawire-quark`

## Python

Instructions for Python (2.7.x)

```bash
cd 1_hello_quark
quark package hello.q --python -o python/hello --python-out=.
cd python
pip install datawire-quark-threaded 
pip install hello/dist/hello-1.0.0-py2-none-any.whl
python hello.py
```

## Java

Instructions for Java (1.7+)

```bash
cd 1_hello_quark
quark package hello.q --java -o java/target --java-out=.
cd java
mvn install target/pom.xml
mvn -q compile && mvn -q exec:java
```