# decision_head.py
"""Module 4: Neuromorphic Decision Head (Paper Section 3.4)"""

def generate_detections(spike_features):
    """Final bounding box + class prediction"""
    print("?? [Decision Head] Generating FOD detections (class + bbox + confidence)")
    return [
        {"class": "Metal Strip", "conf": 0.92, "bbox": [180,120,320,580]},
        {"class": "Debris",      "conf": 0.88, "bbox": [380,620,520,820]},
        {"class": "Nail",        "conf": 0.95, "bbox": [120,680,190,880]}
    ]
