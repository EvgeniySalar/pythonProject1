import pytest
from tstscenario_2.mainpgscr import MainPagescr
from tstscenario_2.home_page.home_pagescr import HomePageScr


class TestSiteFuncScr:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        self.home_page = HomePageScr(chrome_drv)
        self.main_page = MainPagescr(chrome_drv)
        yield chrome_drv

    def test_click_on_city_field(self):
        self.home_page.city_field_element_click()
        self.home_page.city_list_elements()
        self.main_page.citys_field_is_clicked()

    def test_search_button_click(self):
        self.home_page.search_button_selection()
        self.main_page.open_the_next_page()

    def test_calendar_field(self):
        self.home_page.calendar_field()
        self.main_page.calendar_day_today_check()
        self.home_page.calendar_today_data()
        self.home_page.calendar_field_out()
        self.main_page.calendar_next_day_check()
        self.home_page.calendar_next_day_data()
        self.home_page.search_button_selection()
        self.main_page.go_next_step()
