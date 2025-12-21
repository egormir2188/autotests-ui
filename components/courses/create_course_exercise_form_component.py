from playwright.sync_api import Page

from elements.text import Text
from elements.input import Input
from elements.button import Button
from components.base_component import BaseComponent


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercise_delete_button = Button(
            page,
            'create-course-exercise-{index}-box-toolbar-delete-exercise-button',
            'Delete exercise'
        )
        self.subtitle = Text(
            page,
            'create-course-exercise-{index}-box-toolbar-subtitle-text',
            'Exercise subtitle'
        )
        self.title_input = Input(
            page, 'create-course-exercise-{index}-box-toolbar-subtitle-text', 'Title'
        )
        self.description_input = Input(
            page, 'create-course-exercise-form-description-{index}-input', 'Description'
        )

    def click_delete_button(self, index: int):
        self.exercise_delete_button.click(index=index)

    def check_visible_form(self, index: int, title: str, description: str):
        self.subtitle.check_visible(index=index)
        self.subtitle.to_have_text(f'#{index + 1} Exercise', index=index)

        self.title_input.check_visible(index=index)
        self.title_input.to_have_value(title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.to_have_value(description, index=index)

    def fill_form(self, index: int, title: str, description: str):
        self.title_input.fill(title, index=index)
        self.title_input.to_have_value(title, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.to_have_value(description, index=index)