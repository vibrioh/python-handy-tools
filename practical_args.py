from prctical_logging import *
import argparse

parser = argparse.ArgumentParser(description="A practical test for argparse", epilog="Here are more info for help")
# '+'. Just like '*', all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present.
parser.add_argument("arg1", nargs='+')
parser.add_argument("-a", "--arg2", help="this is the second argument that can be optional")
# 上一个用法中-a必须指定参数值，否则就会报错，有没有像-h那样，不需要指定参数值的呢，答案是有，通过定义参数时指定action="store_true"即可
# -aa 没有指定任何参数也可，其实存的是True和False，如果出现，则其值为True，否则为False
parser.add_argument("-aa", "--arg3", help="this is the third argument that can be optional with store_true", action="store_true")
# 默认的参数类型为str，如果要进行数学计算，需要对参数进行解析后进行类型转换，如果不能转换则需要报错，这样比较麻烦 argparse提供了对参数类型的解析，如果类型不符合，则直接报错
parser.add_argument("-int", "--integer", help="put an integer here", type=int)
# -aa 中的action的例子中定义了默认值为True和False的方式，如果要限定某个值的取值范围，比如-int中的整形，限定其取值范围为0， 1， 2
parser.add_argument("-ii", "--integerIn", help="put an integer from 0, 1, 2 here", type=int, choices=[0, 1, 2])
# 第一行定义了一个互斥组，第二、三行在互斥组中添加了-v和-q两个参数, 可以看出，-q和-v不出现，或仅出现一个都可以，同时出现就会报错
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
# default
parser.add_argument("-d", "--default", help="we can define default", default="SeeMe", type=str)
# The 'store_const' action is most commonly used with optional arguments that specify some sort of flag.
parser.add_argument('--foo', action='store_const', const=42)

#  The name of this attribute is determined by the dest keyword


args = parser.parse_args()
logger.info(args)