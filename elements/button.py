from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    def to_be_disabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()

    def to_be_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()