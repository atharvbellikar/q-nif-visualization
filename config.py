# config.py
SAMPLES_DIR = "samples"
OUTPUT_DIR  = "results/qnif_detections"

TITLE = "Q-NIF Detection Output (After)"
TITLE_FONT_SCALE = 1.8
LABEL_FONT_SCALE = 1.3

BOX_COLOR = (0, 0, 255)          # Red BGR
LABEL_COLOR = (0, 255, 0)        # Green BGR
TITLE_COLOR = (255, 255, 255)
TITLE_OUTLINE_COLOR = (0, 0, 0)

SAMPLES = [
    {
        "name": "metal_strip",
        "filename": "metal_strip.jpg",
        "class_name": "Metal Strip",
        "confidence": 0.92,
        "bbox": [180, 120, 320, 580]      # ? Change if box is wrong
    },
    {
        "name": "debris",
        "filename": "debris.jpg",
        "class_name": "Debris",
        "confidence": 0.88,
        "bbox": [380, 620, 520, 820]
    },
    {
        "name": "nail",
        "filename": "nail.jpg",
        "class_name": "Nail",
        "confidence": 0.95,
        "bbox": [120, 680, 190, 880]
    }
]
