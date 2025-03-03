from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests

# 导入这个包
from just_kit.auth import Authenticator
from just_kit.epay import EpayOperator


# 加载 .env 文件中的环境变量
load_dotenv()

username = os.getenv('USER')
password = os.getenv('PASSWORD')



auther = Authenticator(EpayOperator.SERVICE_URL,debug=True)
epay = EpayOperator(auth=auther)

if not auther.check():
    auther.login(username, password)
    if auther.check():
        print("登录成功")
    else:
        print("登录失败")
        quit()

print(epay.query_electric_bill())
account_balance, bathroom_funds = epay.query_account_bill()
print(f"账户余额: {account_balance}")
print(f"专项额度: {bathroom_funds}")

