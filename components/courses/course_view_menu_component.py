from playwright.sync_api import Page

from elements.button import Button
from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Course menu')
        self.edit_menu_button = Button(page, 'course-view-edit-menu-item', 'Edit course')
        self.delete_menu_button = Button(page, 'course-view-delete-menu-item', 'Delete course')

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)