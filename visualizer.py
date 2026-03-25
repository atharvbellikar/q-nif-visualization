# visualizer.py
import cv2
import os
from pathlib import Path
from config import SAMPLES, SAMPLES_DIR, OUTPUT_DIR, TITLE, TITLE_FONT_SCALE, LABEL_FONT_SCALE
from config import BOX_COLOR, LABEL_COLOR, TITLE_COLOR, TITLE_OUTLINE_COLOR
from utils import add_text_with_outline

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_detection_image(sample):
    input_path = Path(SAMPLES_DIR) / sample["filename"]
    img = cv2.imread(str(input_path))
    if img is None:
        print(f"? Could not load {sample['filename']}")
        return

    h, w = img.shape[:2]

    # Draw red bounding box
    x1, y1, x2, y2 = sample["bbox"]
    cv2.rectangle(img, (x1, y1), (x2, y2), BOX_COLOR, 6)

    # Title
    add_text_with_outline(img, TITLE, (20, 70), TITLE_FONT_SCALE, 3, TITLE_COLOR, TITLE_OUTLINE_COLOR)

    # Label
    label = f"FOD: {sample['class_name']}   Confidence: {sample['confidence']:.2f}"
    label_y = y1 - 15 if y1 > 50 else y1 + 60
    add_text_with_outline(img, label, (x1, label_y), LABEL_FONT_SCALE, 3, LABEL_COLOR, TITLE_OUTLINE_COLOR)

    # Save After image
    out_path = Path(OUTPUT_DIR) / f"qnif_after_{sample['name']}.jpg"
    cv2.imwrite(str(out_path), img)

    # Side-by-side comparison
    before = cv2.imread(str(input_path))
    combined = cv2.hconcat([before, img])
    cv2.putText(combined, "BEFORE", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 4)
    cv2.putText(combined, "AFTER (Q-NIF)", (w+30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 4)
    cv2.imwrite(str(Path(OUTPUT_DIR) / f"comparison_{sample['name']}.jpg"), combined)

    print(f"? Saved ? {out_path.name}")
