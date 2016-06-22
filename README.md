# swagger_client
API to receive streamed updates. This is an ssl socket connection of CRLF delimited json messages (see RequestMessage & ResponseMessage)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1423
- Package version: 1.0.0
- Build date: 2016-06-22T18:29:22.944Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developer.betfair.com/support/](https://developer.betfair.com/support/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.DefaultApi
request_message = swagger_client.AllRequestTypesExample() # AllRequestTypesExample | Requests are sent to socket

try:
    api_response = api_instance.request_post(request_message)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->request_post: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *http://stream-api.betfair.com:443/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**request_post**](docs/DefaultApi.md#request_post) | **POST** /request | 


## Documentation For Models

 - [AllRequestTypesExample](docs/AllRequestTypesExample.md)
 - [AllResponseTypesExample](docs/AllResponseTypesExample.md)
 - [AuthenticationMessage](docs/AuthenticationMessage.md)
 - [ConnectionMessage](docs/ConnectionMessage.md)
 - [HeartbeatMessage](docs/HeartbeatMessage.md)
 - [MarketChange](docs/MarketChange.md)
 - [MarketChangeMessage](docs/MarketChangeMessage.md)
 - [MarketDataFilter](docs/MarketDataFilter.md)
 - [MarketDefinition](docs/MarketDefinition.md)
 - [MarketFilter](docs/MarketFilter.md)
 - [MarketSubscriptionMessage](docs/MarketSubscriptionMessage.md)
 - [Order](docs/Order.md)
 - [OrderChangeMessage](docs/OrderChangeMessage.md)
 - [OrderFilter](docs/OrderFilter.md)
 - [OrderMarketChange](docs/OrderMarketChange.md)
 - [OrderRunnerChange](docs/OrderRunnerChange.md)
 - [OrderSubscriptionMessage](docs/OrderSubscriptionMessage.md)
 - [RequestMessage](docs/RequestMessage.md)
 - [ResponseMessage](docs/ResponseMessage.md)
 - [RunnerChange](docs/RunnerChange.md)
 - [RunnerDefinition](docs/RunnerDefinition.md)
 - [StatusMessage](docs/StatusMessage.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

bdp@betfair.com

