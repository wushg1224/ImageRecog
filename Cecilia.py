import cv2
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("Test1.jpg")  # read image

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert image to gray

# 应用双边滤波以减少噪声
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction

# 创建子图
plt.figure(figsize=(10, 5))

# 显示原始图像
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# 显示处理后的图像
plt.subplot(1, 2, 2)
plt.imshow(bfilter, cmap='gray')
plt.title('Processed Image')

# 显示图形
plt.show()
