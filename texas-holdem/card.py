class Card:
    """
    Card类：用于模拟与描述单张扑克牌的类
    """
    def __init__(self):
        """
        构造方法
        两个成员变量分别表示该张扑克牌的花色和数字
        """
        self.__color = ''
        self.__value = 1

    @property
    def color(self):
        """
        相当于java中的color的getter方法
        :return:
        """
        return self.__color

    @color.setter
    def color(self, value):
        """
        相当于java中的color的setter方法
        :param value:
        :return:
        """
        self.__color = value

    @property
    def value(self):
        """
        相当于java中的value的getter方法
        :return:
        """
        return self. __value

    @value.setter
    def value(self, v):
        """
        相当于java中的value的setter方法
        :param v:
        :return:
        """
        # 防止非法扑克牌的出现
        if v < 1 or v >= 14:
            self.__value = 1
        else:
            self.__value = v

    def __str__(self):
        """
        相当于java中的toString()方法
        :return:
        """
        # 定义特殊点数字典
        special_value = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        # 如果赋值的点数在特殊的点数中，那么我们需要处理一下
        if self.value in special_value:
            # 将特殊点数key对应的value取出来
            real_value = special_value[self.value]
        else:
            # 如果不是特殊的点数，那么转成字符串即可
            real_value = str(self.__value)
        #拼接输出对象信息 花色+点数
        return self.__color + real_value+" "
