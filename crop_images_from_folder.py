import os
from PIL import Image

# 定義放原始圖片的資料夾
input_folder = "BOTAMEVE-A4"

# 定義裁切後的資料夾，位於 input_folder 下
output_folder = os.path.join(input_folder, "crop_img")

# 確保裁切後的資料夾存在
os.makedirs(output_folder, exist_ok=True)

cropped_size = 1280

# 讀取 input_folder 下的所有 .jpg 檔案並進行裁切
for filename in os.listdir(input_folder):
    # 確保只處理 .jpg 檔案，並且不包括子資料夾
    if filename.lower().endswith(".jpg") and os.path.isfile(os.path.join(input_folder, filename)):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 打開圖片
        image = Image.open(input_path)
        width, height = image.size

        # 設定裁切範圍 (保留左下方部分)
        crop_area = (0, height-cropped_size, cropped_size, height)
        # crop_area = (0, 35, width, height)

        # 裁切圖片
        cropped_image = image.crop(crop_area)

        # 儲存裁切後的圖片
        cropped_image.save(output_path)
        print(f"裁切完成: {input_path} -> {output_path}")

print(f"所有圖片處理完成！裁切後的圖片已存入 {output_folder} 資料夾。")
