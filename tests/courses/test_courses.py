import pytest
import allure

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.severity import Severity
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from pages.courses.course_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTags.REGRESSION, AllureTags.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible()
        create_course_page.create_course_form.check_visible(
            title='', estimated_time='', description='', max_score='0', min_score='0'
        )

        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_file('./testdata/files/img.png')
        create_course_page.image_upload_widget.check_visible(is_image_upload=True)
        create_course_page.create_course_form.fill(
            title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
        )
        create_course_page.create_course_form.check_visible(
            title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10'
        )

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_courses(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.image_upload_widget.upload_preview_file('./testdata/files/img.png')
        create_course_page.create_course_form.fill(
            title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10', index=0
        )
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(
            title='Pytest', estimated_time='10 weeks', description='Pytest', max_score='10', min_score='1'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            title='Pytest', estimated_time='10 weeks', max_score='10', min_score='1', index=0
        )