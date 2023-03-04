# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/3/5 0:02
    # @Author  : 有勇气的牛排
    # @FileName: main.py
"""

from couragesteak_python_sdk_demo import CsDemo, add, __version__

app = CsDemo("test程序")

res = add(1, 2)
print(res)

if __name__ == "__main__":
    app.run()
    print(__version__)
