import os
import random
import shutil

# SOURCE (your current dataset)
source_dir = r"E:\\augmented_resized_V2"

# TARGET (your project dataset)
target_dir = r"E:\\Lesion-Aware Hybrid Deep Learning DR Detection\\data\\dataset_small"

# How many images per class
LIMIT = 400   # You can change (300 / 500)

splits = ['train', 'val', 'test']
classes = ['0','1','2','3','4']

for split in splits:
    for cls in classes:

        src_path = os.path.join(source_dir, split, cls)
        dst_path = os.path.join(target_dir, split, cls)

        os.makedirs(dst_path, exist_ok=True)

        images = os.listdir(src_path)

        selected = random.sample(images, min(LIMIT, len(images)

        for img in selected:
            shutil.copy(
                os.path.join(src_path, img),
                os.path.join(dst_path, img)
            )

print("✅ Dataset reduced and copied successfully!")