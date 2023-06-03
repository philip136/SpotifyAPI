import pytest

from utils.constant.common_constant import SingerNameConstant, SongConstant, GroupMarkerConstant
from utils.constant.ui_contant import UrlConstant

from page_forms.navigation_form import NavigationForm


@pytest.mark.xdist_group(GroupMarkerConstant.GROUP_UI)
class TestSpotifyUI:
    navigation_form: NavigationForm = NavigationForm()

    @pytest.mark.parametrize(
        "singer_name, song_name",
        [
            pytest.param(SingerNameConstant.DRAKE, SongConstant.ONE_DANCE),
            pytest.param(SingerNameConstant.THE_BEATLES, SongConstant.HERE_COMES_THE_SUN)
        ]
    )
    def test_check_song(self, browser, singer_name: str, song_name: str):
        browser.go_to(url=UrlConstant.SPOTIFY_HOME_PAGE)
        singer_form = self.navigation_form.go_to_singer_form(singer_name=singer_name)
        song_text_box = singer_form.get_song_by_name(song_name=song_name)
        assert song_text_box.text.lower() == song_name.lower(), f"Wrong name for the song {song_name}"

    def test_recent_searches(self, browser):
        browser.go_to(url=UrlConstant.SPOTIFY_HOME_PAGE)
        for singer_name in (SingerNameConstant.DRAKE, SingerNameConstant.THE_BEATLES):
            self.navigation_form.go_to_singer_form(singer_name=singer_name)
            singer_box = self.navigation_form.go_to_recent_searches()
            assert singer_name.lower() in singer_box.text.lower(), \
                f"{singer_name.capitalize()} not found in recent search"
