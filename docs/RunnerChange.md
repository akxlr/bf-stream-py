# RunnerChange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tv** | **float** | The total amount matched. This value is truncated at 2dp. | [optional] 
**batb** | **list[list[float]]** | Best Available To Back - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**spb** | **list[list[float]]** | Starting Price Back - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**bdatl** | **list[list[float]]** | Best Display Available To Lay (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**trd** | **list[list[float]]** | Traded - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**spf** | **float** | Starting Price Far - The far starting price (or null if un-changed) | [optional] 
**ltp** | **float** | Last Traded Price - The last traded price (or null if un-changed) | [optional] 
**atb** | **list[list[float]]** | Available To Back - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**spl** | **list[list[float]]** | Starting Price Lay - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**spn** | **float** | Starting Price Near - The far starting price (or null if un-changed) | [optional] 
**atl** | **list[list[float]]** | Available To Lay - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**batl** | **list[list[float]]** | Best Available To Lay - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**id** | **int** | Selection Id - the id of the runner (selection) | [optional] 
**hc** | **float** | Handicap - the handicap of the runner (selection) (null if not applicable) | [optional] 
**bdatb** | **list[list[float]]** | Best Display Available To Back (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


