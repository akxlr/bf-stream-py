# swagger_client.DefaultApi

All URIs are relative to *http://stream-api.betfair.com:443/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_post**](DefaultApi.md#request_post) | **POST** /request | 


# **request_post**
> AllResponseTypesExample request_post(request_message)



This is a socket protocol delimited by CRLF (not http)

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
request_message = swagger_client.AllRequestTypesExample() # AllRequestTypesExample | Requests are sent to socket

try: 
    api_response = api_instance.request_post(request_message)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->request_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_message** | [**AllRequestTypesExample**](AllRequestTypesExample.md)| Requests are sent to socket | 

### Return type

[**AllResponseTypesExample**](AllResponseTypesExample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

