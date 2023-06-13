from forms.base_form import BaseForm

from page_forms.singer_form import SingerForm
from utils.tuple_utils import fill_locator_value
from utils.constant.ui_contant import LocatorConstant, ElementNameConstant


class NavigationForm(BaseForm):
    __search_btn_locator = fill_locator_value(ElementNameConstant.SEARCH_BTN, LocatorConstant.NAVBAR_BTN_LOCATOR)

    def __init__(self):
        super(NavigationForm, self).__init__(LocatorConstant.ROOT_LOCATOR, ElementNameConstant.ROOT_NAME)

    def go_to_singer_form(self, singer_name: str) -> SingerForm:
        self._element_factory.get_button(self.__search_btn_locator, ElementNameConstant.SEARCH_BTN).click()
        self._element_factory.get_text_box(LocatorConstant.SONG_TEXT_BOX_LOCATOR, ElementNameConstant.SONG_TEXT_BOX).\
            type(singer_name)
        self._element_factory.get_button(LocatorConstant.SINGER_BTN_LOCATOR, ElementNameConstant.SINGER_BTN).click()
        return SingerForm(artist_name=singer_name)

    def go_to_recent_searches(self):
        self._element_factory.get_button(self.__search_btn_locator, ElementNameConstant.SEARCH_BTN).click()
        return self._element_factory.get_combo_box(LocatorConstant.RECENT_SEARCH_SINGER,
                                                   ElementNameConstant.RECENT_SINGERS)

