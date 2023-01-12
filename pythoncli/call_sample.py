import argparse
import os
import pathlib

def hello():
    print('hello qiita')

def add(a, b):
    print(a + b)

def printString(a):
    print(a)

def printJSONString(json):
    try:
        print(json["key1"])
        print(json["key2"])
    except Exception:
        print("Error printJSONString(json) ")

def multiFunc(a, b, c):
    hello()
    add(a, b)
    printString(c)


def editFile(path):
    print(path)
    pathc = pathlib.Path(path)
    print(pathc)
    isFile = os.path.isfile(pathc)
    if isFile == False:
        print("Not exit file")
        return

    with open(pathc) as f:
        s = f.read()
        print("Read File1")
        print(s)

    with open(pathc, mode='a') as f:
        addstr = "2nd write"
        f.write(addstr)

    with open(pathc) as f:
        s = f.read()
        print("Read File2")
        print(s)

    print("Complete Editting File")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name',
                        type=str,
                        help='set fuction name in this file')
    parser.add_argument('-i', '--func_args',
                        nargs='*',
                        help='args in function',
                        default=[])
    args = parser.parse_args()

    # このファイル内の関数を取得
    func_dict = {k: v for k, v in locals().items() if callable(v)}
    # 引数のうち，数値として解釈できる要素はfloatにcastする
    func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
    # 関数実行
    ret = func_dict[args.function_name](*func_args)