from setuptools import setup, find_packages

setup(
    name="just-kit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests',  # 用于发送HTTP请求
        'beautifulsoup4',  # 用于解析HTML
    ],
    author="Anonymous",
    author_email="anonymous@example.com",
    description="江苏科技大学信息门户工具包",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/heerheer/just-kit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)