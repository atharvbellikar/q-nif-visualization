# run.py
from visualizer import create_detection_image
from config import SAMPLES

print("?? Starting Q-NIF Visualization Pipeline...\n")

for sample in SAMPLES:
    create_detection_image(sample)

print("\n?? All visualizations generated successfully!")
print("?? Check the 'results/' folder")
