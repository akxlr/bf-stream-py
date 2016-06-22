# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | Side - the side of the order | [optional] 
**sv** | **float** | Size Voided - the amount of the order that has been voided | [optional] 
**pt** | **str** | Persistence Type - whether the order will persist at in play or not (L &#x3D; LAPSE, P &#x3D; PERSIST, MOC &#x3D; Market On Close) | [optional] 
**ot** | **str** | Order Type - the type of the order (L &#x3D; LIMIT, MOC &#x3D; MARKET_ON_CLOSE, LOC &#x3D; LIMIT_ON_CLOSE) | [optional] 
**p** | **float** | Price - the original placed price of the order | [optional] 
**sc** | **float** | Size Cancelled - the amount of the order that has been cancelled | [optional] 
**rc** | **str** | Regulator Code - the regulator of the order | [optional] 
**s** | **float** | Size - the original placed size of the order | [optional] 
**pd** | **int** | Placed Date - the date the order was placed | [optional] 
**rac** | **str** | Regulator Auth Code - the auth code returned by the regulator | [optional] 
**md** | **int** | Matched Date - the date the order was matched (null if the order is not matched) | [optional] 
**sl** | **float** | Size Lapsed - the amount of the order that has been lapsed | [optional] 
**avp** | **float** | Average Price Matched - the average price the order was matched at (null if the order is not matched | [optional] 
**sm** | **float** | Size Matched - the amount of the order that has been matched | [optional] 
**id** | **str** | Bet Id - the id of the order | [optional] 
**bsp** | **float** | BSP Liability - the BSP liability of the order (null if the order is not a BSP order) | [optional] 
**status** | **str** | Status - the status of the order (E &#x3D; EXECUTABLE, EC &#x3D; EXECUTION_COMPLETE) | [optional] 
**sr** | **float** | Size Remaining - the amount of the order that is remaining unmatched | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


