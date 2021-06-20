# Sample code for a simple web app



This is the repo for a small web application in Python



## Intro

The application performs the following behaviors:

 - Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
 - Return a JSON object with the key “return_string” and a string containing every third letter from the original string

e.g., POST {"string_to_cut": "helloword"} will have a retun: {"return_string": "lwd"}



## Prerequisites

To excute this example, you will need:

- Python 3 installed in a local environment

- Flask installed. Use the follwoing command to install Flask:

  `pip install Flask`



## Use Case

To run the test sample, navigate into the repo directory, and

1. run Flask

```
$ flask run
```

(or directly run `$ python app.py`)

2. excute the following command

```
$ curl -X POST localhost:5000/test --data '{"string_to_cut": "helloword"}' -H 'Content-Type: application/json'
```

