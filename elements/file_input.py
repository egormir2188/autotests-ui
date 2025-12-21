from elements.base_element import BaseElement


class InputFile(BaseElement):
    def set_input_file(self, file: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)