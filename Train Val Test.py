import os
import shutil
import random

classes = ['normal', 'covid_19']
main_dir = 'C:/Users/Hemanth/Desktop/Pre-trained with GradCAM'
img_dir = ['Normal', 'COVID']

os.mkdir(os.path.join(main_dir, 'val'))
os.mkdir(os.path.join(main_dir, 'train'))
os.mkdir(os.path.join(main_dir, 'test'))

for x, y in enumerate(img_dir):
    os.renames(
        os.path.join(main_dir, y),
        os.path.join(main_dir, classes[x])
    )

for c in classes:
    os.mkdir(os.path.join(main_dir, 'test', c))
    os.mkdir(os.path.join(main_dir, 'val', c))

    all_img = [i for i in os.listdir(os.path.join(
        main_dir, c)) if i.lower().endswith('png')]
    test_samples = random.sample(all_img, 300)
    all_img = list(set(all_img) - set(test_samples))
    val_samples = random.sample(all_img, 300)

    for i in test_samples:
        shutil.move(
            os.path.join(main_dir, c, i),
            os.path.join(main_dir, 'test', c, i)
        )

    for i in val_samples:
        shutil.move(
            os.path.join(main_dir, c, i),
            os.path.join(main_dir, 'val', c, i)
        )

    shutil.move(
        os.path.join(main_dir, c),
        os.path.join(main_dir, 'train')
    )
