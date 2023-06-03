from forms.base_form import BaseForm

from utils.tuple_utils import fill_locator_value
from utils.constant.ui_contant import LocatorConstant, ElementNameConstant


class SingerForm(BaseForm):
    def __init__(self, artist_name: str):
        super(SingerForm, self).__init__(LocatorConstant.FORM_ROOT_LOCATOR, ElementNameConstant.SINGER_PAGE_FORM)
        self.__artist_name = artist_name
        self.element_factory = self._get_element_factory()

    def get_song_by_name(self, song_name: str):
        locator = fill_locator_value(song_name, LocatorConstant.SONG_LOCATOR)
        return self.element_factory.get_text_box(locator, ElementNameConstant.SONG_LINK)
