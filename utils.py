# utils.py
import cv2

def add_text_with_outline(img, text, pos, font_scale, thickness, text_color, outline_color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Black outline
    cv2.putText(img, text, pos, font, font_scale, outline_color, thickness + 4, cv2.LINE_AA)
    # Main text
    cv2.putText(img, text, pos, font, font_scale, text_color, thickness, cv2.LINE_AA)
