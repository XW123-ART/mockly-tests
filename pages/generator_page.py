"""
数据生成页面操作封装
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time


class GeneratorPage(BasePage):
    """数据生成页面对象"""
    url = "/generator"

    page_title = (By.TAG_NAME, "h1")
    user_name = (By.CLASS_NAME, "user-name")
    logout_btn = (By.CLASS_NAME, "logout-btn")

    source_inline = (By.CSS_SELECTOR, "input[value='inline']")
    source_file = (By.CSS_SELECTOR, "input[value='file']")
    source_openapi = (By.CSS_SELECTOR, "input[value='openapi']")

    schema_textarea = (By.ID, "schema")
    count_input = (By.ID, "count")
    smart_checkbox = (By.NAME, "smart")
    mutate_checkbox = (By.NAME, "mutate")
    report_checkbox = (By.NAME, "report")
    submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

    file_input = (By.NAME, "schema-file")
    file_schema_area = (By.ID, "file-schema")
    openapi_file_input = (By.NAME, "openapi-file")
    openapi_file_area = (By.ID, "openapi-file")

    format_select = (By.ID, "format")
    table_input = (By.ID, "table")
    result_pre = (By.TAG_NAME, "pre")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open(self):
        super().open(self.url)
        time.sleep(1)

    def get_page_title(self):
        return self.get_text(*self.page_title)

    def get_user_info(self):
        if self.is_element_exist(*self.user_name):
            return self.get_text(*self.user_name)
        return None

    def is_user_logged_in(self):
        return self.is_element_exist(*self.user_name)

    def click_logout(self):
        self.click(*self.logout_btn)
        time.sleep(2)

    def input_schema(self, schema_text):
        self.input_text(*self.schema_textarea, schema_text)

    def set_count(self, count):
        self.input_text(*self.count_input, str(count))

    def click_submit(self):
        self.click(*self.submit_btn)
        time.sleep(3)

    def generate_data(self, schema_text, count=1):
        self.input_schema(schema_text)
        self.set_count(count)
        self.click_submit()

    def get_result_text(self):
        if self.is_element_exist(By.TAG_NAME, "pre"):
            pre_elements = self.find_elements(By.TAG_NAME, "pre")
            if pre_elements:
                return pre_elements[0].text
        return None

    def is_on_generator_page(self):
        return "/generator" in self.get_current_url()

    def switch_to_inline_source(self):
        self.click(*self.source_inline)
        time.sleep(1)

    def switch_to_file_source(self):
        self.click(*self.source_file)
        time.sleep(1)

    def switch_to_openapi_source(self):
        self.click(*self.source_openapi)
        time.sleep(1)

    def is_file_source_active(self):
        file_area = self.find_element(*self.file_schema_area)
        style = file_area.get_attribute("style")
        is_hidden = "display: none" in style
        return not is_hidden or file_area.is_displayed()

    def is_openapi_source_active(self):
        openapi_area = self.find_element(*self.openapi_file_area)
        style = openapi_area.get_attribute("style")
        return "display: none" not in style

    def upload_schema_file(self, file_path):
        file_input = self.find_element(*self.file_input)
        file_input.send_keys(file_path)
        time.sleep(1)

    def upload_openapi_file(self, file_path):
        file_input = self.find_element(*self.openapi_file_input)
        file_input.send_keys(file_path)
        time.sleep(1)

    def set_smart_option(self, enabled=True):
        checkbox = self.find_element(*self.smart_checkbox)
        is_selected = checkbox.is_selected()
        if enabled and not is_selected:
            checkbox.click()
            time.sleep(0.5)
        elif not enabled and is_selected:
            checkbox.click()
            time.sleep(0.5)

    def set_mutate_option(self, enabled=True):
        checkbox = self.find_element(*self.mutate_checkbox)
        is_selected = checkbox.is_selected()
        if enabled and not is_selected:
            checkbox.click()
            time.sleep(0.5)
        elif not enabled and is_selected:
            checkbox.click()
            time.sleep(0.5)

    def set_report_option(self, enabled=True):
        checkbox = self.find_element(*self.report_checkbox)
        is_selected = checkbox.is_selected()
        if enabled and not is_selected:
            checkbox.click()
            time.sleep(0.5)
        elif not enabled and is_selected:
            checkbox.click()
            time.sleep(0.5)

    def select_output_format(self, format_type):
        select = Select(self.find_element(*self.format_select))
        select.select_by_value(format_type)
        time.sleep(1)

    def set_table_name(self, table_name):
        self.input_text(*self.table_input, table_name)

    def get_page_source(self):
        return self.driver.page_source
