start = '2016-11-15'# 回测起始时间
end = '2017-11-09' # 回测结束时间
stocks=['000001']
freq = 'd'  #d表示使用日频率回测，m表示使用分钟频率回测。默认为d
capital_base=1000000#初始资金
calendar='SHSZ'#SHSZ表示使用A股，不设置，使用美股NYSE
benchmark='000001'#基准，如果calendar不为美股NYSE，基准则一定要设置
def initialize(context):
    pass

def before_trading_start(context, data):
    pass
        
def handle_data(context, data):
    for stock in data:
      context.order(stock, 10)
