from playwright.sync_api import expect

from components.base_component import BaseComponent


class CreateCourseExerciseFormComponent(BaseComponent):
    def click_delete_button(self, index: int):
        exercise_delete_button = self.page.get_by_test_id(
            f'create-course-exercise-{index}-box-toolbar-delete-exercise-button'
        )
        exercise_delete_button.click()

    def check_visible_form(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        title_input = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        description_input = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f'#{index} Exercise')

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill_form(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        description_input = self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)