from playwright.sync_api import Page

from elements.icon import Icon
from elements.text import Text
from elements.image import Image
from elements.button import Button
from elements.file_input import FileInput
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page)

        self.preview_image = Image(
            page, '{identifier}-image-upload-widget-preview-image', 'Preview image'
        )
        self.image_upload_info_icon = Icon(
            page, '{identifier}-image-upload-widget-info-icon', 'Upload info icon'
        )
        self.image_upload_info_title = Text(
            page, '{identifier}-image-upload-widget-info-title-text', 'Upload info title'
        )
        self.image_upload_info_description = Text(
            page, '{identifier}-image-upload-widget-info-description-text', 'Upload info description'
        )
        self.upload_button = Button(
            page, '{identifier}-image-upload-widget-upload-button', 'Upload image button'
        )
        self.remove_button = Button(
            page, '{identifier}-image-upload-widget-remove-button', 'Remove image button'
        )
        self.upload_image_input = FileInput(
            page, '{identifier}-image-upload-widget-input', 'Upload image input'
        )

    def check_visible(self, identifier: str, is_image_upload: bool = False):
        self.image_upload_info_icon.check_visible(identifier=identifier)

        self.image_upload_info_title.check_visible(identifier=identifier)
        self.image_upload_info_title.to_have_text(
            'Tap on "Upload image" button to select file', identifier=identifier
        )

        self.image_upload_info_description.check_visible(identifier=identifier)
        self.image_upload_info_description.to_have_text(
            'Recommended file size 540X300', identifier=identifier
        )

        self.upload_button.check_visible(identifier=identifier)

        if is_image_upload:
            self.remove_button.check_visible(identifier=identifier)
            self.preview_image.check_visible(identifier=identifier)

        if not is_image_upload:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here',
                identifier=identifier
            )

    def upload_preview_file(self, file: str, identifier: str):
        self.upload_image_input.set_input_file(file, identifier=identifier)

    def click_remove_image_button(self, identifier: str):
        self.remove_button.click(identifier=identifier)