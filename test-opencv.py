import cv2
my_img=cv2.imread('/home/yu/projects/darkflow-master/preview.png')
cv2.namedWindow('1')
cv2.imshow('1',my_img)
cv2.waitKey(0)