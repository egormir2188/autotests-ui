from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    def to_be_disabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()

    def to_be_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()