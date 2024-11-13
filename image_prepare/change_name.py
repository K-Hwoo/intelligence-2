import os

# 이미지 폴더 경로
image_folder = 'pigeon'

# 이미지 파일 목록 불러오기
image_files = sorted(os.listdir(image_folder))

# 파일명 변경
for idx, img_file in enumerate(image_files):
    # 기존 파일 경로
    old_path = os.path.join(image_folder, img_file)
    
    # 새 파일명 및 경로 설정
    new_name = f'pigeon{idx}.jpg'
    new_path = os.path.join(image_folder, new_name)
    
    # 파일명 변경
    os.rename(old_path, new_path)

print("파일 이름 변경이 완료되었습니다!")
