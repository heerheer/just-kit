import requests
import logging
from typing import Optional
from .auth import Authenticator
from .service import ServieProvider
from bs4 import BeautifulSoup

class EpayOperator(ServieProvider):
    """
    用于查询账单信息的类
    """
    SERVICE_URL = "http://202.195.206.214/epay/"

    def __init__(self, auth:Authenticator):
        """
        初始化查询类
        :param auth: Authenticator实例
        """
        super().__init__(auth)
        

    @classmethod
    def get_service_url(cls) -> str:
        """
        获取服务地址
        :return: 服务的URL
        """
        return cls.SERVICE_URL

    def query_electric_bill(self, room_no: int =4372, sys_id: int = 2, 
                          elc_area: int = 2, elc_buis: int = 4355) -> Optional[float]:
        """
        查询电费
        :param room_no: 房间号
        :param sys_id: 系统ID
        :param elc_area: 电力区域
        :param elc_buis: 电力业务ID
        :return: 剩余电量,查询失败返回None
        """
        url = f"{self.SERVICE_URL}/electric/queryelectricbill"
        jsessionid = self.auth.jsessionid()
        
        if not jsessionid:
            self.logger.error("未获取到有效的JSESSIONID，请先登录")
            return None

        headers = {
            "Cookie": f'JSESSIONID={jsessionid}'
        }
        
        data = {
            "sysid": sys_id,
            "roomNo": room_no,
            "elcarea": elc_area,
            "elcbuis": elc_buis
        }
        
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            result = response.json()
            
            if result.get("retcode") == 0:
                rest_degree = result.get("restElecDegree", 0)
                self.logger.info(f"房间 {room_no} 剩余电量: {rest_degree} 度")
                return rest_degree
            else:
                self.logger.error(f"查询失败: {result.get('message', '未知错误')}")
                return None

        except requests.exceptions.RequestException as e:
            self.logger.error(f"请求失败: {e}")
            return None
        except ValueError as e:
            self.logger.error(f"解析响应失败: {e}")
            return None

    def query_account_bill(self):

        '''
        查询账户余额和浴室专款
        '''
        html_content= self.auth.session.get(f"{self.SERVICE_URL}/myepay/index").text

        # 解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 定位账户信息所在的<dd>标签
        dd_tag = soup.find('section', id='content').find('dd')

        # 提取所有<p>标签内容
        p_tags = dd_tag.find_all('p')

        account_balance = None
        bathroom_funds = None

        for p in p_tags:
            text = p.get_text(strip=True)
            if '账户余额' in text:
                account_balance = text.split('：')[1].replace('元', '')
            elif '浴室专款' in text:
                bathroom_funds = text.split('：')[1].replace('元', '')

        return account_balance, bathroom_funds