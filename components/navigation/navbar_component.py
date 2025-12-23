from playwright.sync_api import Page

from elements.text import Text
from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'Navbar title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Wellcome title')

    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.to_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.to_have_text(f'Welcome, {username}!')