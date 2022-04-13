from fileinput import filename
import cv2
import os

def displayshiba():
    filePath = 'Shiba.jpg'
    img = cv2.imread(filePath, 1)
    resize = cv2.resize(img, (800, 540))
    cv2.imshow(filePath, resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def userinput():   
    while True:
        fileName = input("\nWhat do you want to see? \nmajestic husky (type husky) \nthug pug(type pug) \nchoose:")
        fileExtention = ".jpg"
        file = fileName + fileExtention
        if os.path.exists(file):
            image = cv2.imread(file,1)
            cv2.imshow(file, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

        else:
            print("File not found...")