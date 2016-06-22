# OrderSubscriptionMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation type | [optional] 
**id** | **int** | Client generated unique id to link request with response (like json rpc) | [optional] 
**segmentation_enabled** | **bool** | Segmentation Enabled - allow the server to send large sets of data in segments, instead of a single block | [optional] 
**order_filter** | [**OrderFilter**](OrderFilter.md) |  | [optional] 
**clk** | **str** | Token value delta (received in MarketChangeMessage) that should be passed to resume a subscription | [optional] 
**heartbeat_ms** | **int** | Heartbeat Milliseconds - the heartbeat rate (looped back on initial image after validation: bounds are 500 to 30000) | [optional] 
**initial_clk** | **str** | Token value (received in initial MarketChangeMessage) that should be passed to resume a subscription | [optional] 
**conflate_ms** | **int** | Conflate Milliseconds - the conflation rate (looped back on initial image after validation: bounds are 0 to 120000) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


