# Milkstraw Python Client

This version is just a template and only does dummy test get requests to any given url.

Install the client:
``` shell
pip install git+ssh://git@github.com/milkstrawai/milkstraw-python-client@main
```
Then in python, you can test it as follows:
``` shell
$ python
>>> import milkstraw_client
>>> milkstraw_client.test_url("https://www.google.com")
The url 'https://www.google.com' responsed with 200 status code.
```
