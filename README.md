# pypi项目规范案例



<div style="text-align:center;">
    <p>
        <sub>
            Built with ❤︎ by
            <a href="https://www.couragesteak.com/">
                有勇气的牛排
            </a>
        </sub>
    </p>
</div>



## 1 安装

```shell
pip3.8 uninstall couragesteak-python-sdk-demo

pip3.8 install couragesteak-python-sdk-demo==0.0.1
pip3.8 install couragesteak-python-sdk-demo==0.0.2
```



## 2 测试、编译和上传

### 2.1 本地测试

```shell
python setup.py develop
```



编译tar.gz：

```shell
python setup.py sdist
```





编译whl：

```
pip install wheel
python setup.py bdist_wheel
```



检查

```shell
python setup.py check 
```



上传到pypi：

```shell
pip install twine
twine upload dist/*
```



## 更新日志

`0.0.1` 基础版测试

