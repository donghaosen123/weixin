import sys,os
sys.path.append(os.getcwd())
import base
from base.base_driver import init_driver
from page.sms_page import SmsPage

class TestSms:
    def setup(self):
        self.driver = init_driver(base.app_package,base.app_activity)
        self.sms_page = SmsPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_sms(self):

        self.sms_page.click_add_sms1()
        self.sms_page.click_add_sms2()
        self.sms_page.test_sendkeys()

