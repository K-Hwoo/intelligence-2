import os
import shutil
from zipfile import ZipFile

# 이미지 폴더 경로 및 그룹 수
image_folder = 'gorani'
num_groups = 4

# 이미지 파일 목록 불러오기
image_files = sorted(os.listdir(image_folder))
num_images = len(image_files)
images_per_group = num_images // num_groups

# 그룹별로 폴더 생성 및 이미지 분할
for i in range(num_groups):
    group_folder = f'gorani_images_part{i+1}'
    os.makedirs(group_folder, exist_ok=True)
    
    # 이미지 할당 범위 설정
    start_idx = i * images_per_group
    end_idx = (i+1) * images_per_group if i < num_groups - 1 else num_images
    
    # 이미지 이동
    for img_file in image_files[start_idx:end_idx]:
        shutil.move(os.path.join(image_folder, img_file), os.path.join(group_folder, img_file))
    
    # 압축 파일로 만들기
    with ZipFile(f'{group_folder}.zip', 'w') as zipf:
        for root, _, files in os.walk(group_folder):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), group_folder))

    # 완료 후 임시 폴더 삭제
    shutil.rmtree(group_folder)

print("4개의 압축 파일이 생성되었습니다.")
