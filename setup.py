from setuptools import setup, find_packages

setup(
    name="just_kit",
    version="0.1.0",
    packages=find_packages(exclude=['just_kit.utils*']),
    install_requires=[
        'requests',  # 用于发送HTTP请求
        'beautifulsoup4',  # 用于解析HTML
        'dotenv',
        'PyExecJS',  # 用于执行JavaScript代码
        'pycryptodome'
    ],
    author="Harmog",
    author_email="harmog@foxmail.com",
    description="江苏科技大学信息门户工具包",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    url="https://github.com/heerheer/just-kit",
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.6',
)