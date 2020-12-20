"""
file for testing all of my_src code and functionalities
"""
import unittest
from unittest.mock import patch, MagicMock  # noqa: F401
from my_src import (getSoilConditions, getIllConditions,
                    getSunConditions, getWaterConditions)

# class that all tests will go into


class TestStuff(unittest.TestCase):

    def test_sun_al(self):
        assert getSunConditions(
            'my_src/care_files/alocasia.txt') == ('alocasia', ['indirect', 'direct sun will cause the leaves to burn']) # noqa

    def test_sun_dieff(self):
        assert getSunConditions(
            'my_src/care_files/dieffenbachia.txt') == ('dieffenbachia', ['low filtered light', 'if the light is too bright or shines directly on the plant']) # noqa

    def test_sun_po(self):
        assert getSunConditions(
            'my_src/care_files/pothos.txt') == ('pothos', ['bright indirect light', 'they do not do well in direct sunlight']) # noqa

    def test_sun_pl(self):
        assert getSunConditions(
            'my_src/care_files/peace_lily.txt') == ('peace_lily', ['medium to low light', 'peace lilies that are placed in more direct light']) # noqa

    def test_soil_al(self):
        assert getSoilConditions(
            'my_src/care_files/alocasia.txt') == ('alocasia', ['aerating', 'allow the top 2 - 3 \" to dry between watering to ensure the plant isn \' t sitting in soil that is too wet']) # noqa

    def test_soil_dieff(self):
        assert getSoilConditions(
            'my_src/care_files/dieffenbachia.txt') == ('dieffenbachia', ['moist , but not soggy', 'moist']) # noqa

    def test_soil_po(self):
        assert getSoilConditions(
            'my_src/care_files/pothos.txt') == ('pothos', ['nutrient rich soil , but do almost as well in nutrient poor soil', 'dry soil']) # noqa

    def test_soil_pl(self):
        assert getSoilConditions(
            'my_src/care_files/peace_lily.txt') == ('peace_lily', ['touch the top of the soil to see if it is dry', 'damp']) # noqa

    def test_water_al(self):
        assert getWaterConditions(
            'my_src/care_files/alocasia.txt') == ('alocasia', ['allow the top 2 - 3 \" to dry between watering to ensure the plant isn \' t sitting in soil that is too wet . alocasias can be susceptible to root rot and fungal infections if their soil doesn \' t have proper drainage and becomes waterlogged , so we always advise potting these plants in a vessel with a drainage hole']) # noqa

    def test_water_dieff(self):
        assert getWaterConditions(
            'my_src/care_files/dieffenbachia.txt') == ('dieffenbachia', ['lightly']) # noqa

    def test_water_po(self):
        assert getWaterConditions(
            'my_src/care_files/pothos.txt') == ('pothos', ['a jug of water where it can remain untouched as long as water remains in the jug']) # noqa

    def test_water_pl(self):
        assert getWaterConditions(
            'my_src/care_files/peace_lily.txt') == ('peace_lily', ['touch the top of the soil to see if it is dry']) # noqa

    def test_ill_al(self):
        assert getIllConditions(
            'my_src/care_files/alocasia.txt') == ('alocasia', ['root rot and fungal infections', 'lower light conditions']) # noqa

    def test_ill_dieff(self):
        assert getIllConditions(
            'my_src/care_files/dieffenbachia.txt') == ('dieffenbachia', ['too much moisture', 'spider mite infestation gets too bad']) # noqa

    def test_ill_po(self):
        assert getIllConditions(
            'my_src/care_files/pothos.txt') == ('pothos', ['they do well in bright indirect light as well as low light', 'direct sunlight']) # noqa

    def test_ill_pl(self):
        assert getIllConditions(
            'my_src/care_files/peace_lily.txt') == ('peace_lily', ['overwatering', 'watering them on a schedule']) # noqa
