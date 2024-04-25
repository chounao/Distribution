"""
1.代发订单管理：
    case:
        同步订单关闭状态下
        待分配订单查询,查询后如果有订单进行分配 TestAllocateOrders
        已分配未发货订单查询，查询后如果有订单取消分配 TestCancelOrders
        已分配已发货订单查询 TestShippedOrders
        开启同步订单后已经绑定过厂家的订单是否分配
2.厂家管理：
    case:
        获取厂家链接 TestgetLink
        解绑流程
        取消操作
3.分销商品管理
    case:
        同步商品 TestQueryTasksGoods
        分配厂家 TestAllocationProduct
"""