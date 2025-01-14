# python官方文档
from distutils.core import setup

setup(
    name="IRCRA",
    version="1.0",
    description="Intelligent Road Condition Report Application",
    author="Qinning Xu",
    # 包路径与python模块(.py扩展名文件)
    packages=[
        "trafficapp",
        "trafficapp.aicv",
        "trafficapp.biz",
        "trafficapp.uis",
        "trafficapp.dao",
    ],

    #脚本文件
    scripts=[
        "run_app.sh",
    ],

    #数据文件
    package_data={
        "":["",""],
    },

)


# python setup_app.py --help
# python setup_app.py --help-commands
# python setup_app.py build
# python setup_app.py install