import cv2

# 读取图片文件
image_path = '111.jpg'  # 替换为你的图片路径
image = cv2.imread(image_path)

# 检查图片是否成功加载
if image is None:
    print("Error: Unable to load image.")
else:
    # 显示图片
    cv2.imshow('Image', image)

    # 等待用户按键，然后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()

