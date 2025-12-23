from typing import Pattern
from playwright.sync_api import Page

from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,f'{identifier}-drawer-list-item-icon', 'Sidebar item icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Sidebar item title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Sidebar item')


    def check_visible(self, identifier: str, title: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.to_have_text(title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate(self, identifier: str, expected_url: Pattern[str]):
        self.button.click(identifier=identifier)
        self.check_current_url(expected_url)