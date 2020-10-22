import os
import sys
sys.path.insert(0, os.path.abspath(".."))
from my_src import read_audio  # noqa


def test1():
    assert read_audio() == 'output.wav'
