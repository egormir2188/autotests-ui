import pytest
import allure

from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.severity import Severity
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTags.REGRESSION, AllureTags.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_display(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        )

        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_toolbar.check_visible()

        dashboard_page_with_state.scores_chart_view.check_visible(title='Scores')
        dashboard_page_with_state.courses_chart_view.check_visible(title='Courses')
        dashboard_page_with_state.students_chart_view.check_visible(title='Students')
        dashboard_page_with_state.activities_chart_view.check_visible(title='Activities')