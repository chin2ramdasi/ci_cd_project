# main.py

import cv2
import numpy as np
from utils import decode_udp_message, draw_trajectory


def main():
    # Simulate UDP message input
    msg = "speed:20,angle:15"
    speed, angle = decode_udp_message(msg)

    # Create dummy image (black background)
    frame = np.zeros((480, 640, 3), dtype=np.uint8)

    # Draw trajectory based on the message
    frame = draw_trajectory(frame, speed, angle)

    # Save the result
    cv2.imwrite("output.jpg", frame)
    print("Processed frame saved as output.jpg")

if __name__ == "__main__":
    main()