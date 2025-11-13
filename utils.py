# utils.py
import cv2
import numpy as np

def decode_udp_message(msg: str):
    """Parses a UDP message like 'speed:20,angle:15'."""
    try:
        parts = dict(item.split(":") for item in msg.split(","))
        return float(parts["speed"]), float(parts["angle"])
    except Exception as e:
        raise ValueError(f"Invalid UDP message: {msg}") from e
    

def draw_trajectory(frame, speed: float, angle: float):
    """Draws a simple line representing trajectory."""
    height, width = frame.shape[:2]
    start = (width // 2, height - 20)
    end = (int(width // 2 + angle * 10), int(height - 20 - speed * 5))
    cv2.line(frame, start, end, (0, 255, 0), 3)
    return frame