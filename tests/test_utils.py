# tests/test_utils.py
from ci_cd_project.utils import decode_udp_message, draw_trajectory
import numpy as np
import cv2


def test_decode_udp_message_valid():
    msg = "speed:30,angle:10"
    speed, angle = decode_udp_message(msg)
    assert speed == 30
    assert angle == 10

def test_decode_udp_message_invalid():
    import pytest
    with pytest.raises(ValueError):
        decode_udp_message("wrong_message")

    