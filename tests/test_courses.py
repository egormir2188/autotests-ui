from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='./browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        course_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_header).to_be_visible()
        expect(course_header).to_have_text('Courses')

        course_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(course_list_title).to_be_visible()
        expect(course_list_title).to_have_text('There is no results')

        empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_block_icon).to_be_visible()

        course_empty_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_empty_list_description).to_be_visible()
        expect(course_empty_list_description).to_have_text('Results from the load test pipeline will be displayed here')