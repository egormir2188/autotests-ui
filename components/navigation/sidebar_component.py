import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('logout', 'Logout')
        self.courses_list_item.check_visible('courses', 'Courses')
        self.dashboard_list_item.check_visible('dashboard', 'Dashboard')

    def click_logout_button(self):
        self.logout_list_item.navigate('logout', re.compile(r'.*/#/auth/login'))

    def click_courses_button(self):
        self.courses_list_item.navigate('courses', re.compile(r'.*/#/courses'))

    def click_dashboard_button(self):
        self.courses_list_item.navigate('dashboard', re.compile(r'.*/#/dashboard'))