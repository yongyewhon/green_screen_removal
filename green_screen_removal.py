import numpy as np
import cv2
import os

directory_path = "./Images/" #input image
#background_image = cv2.imread("./Background/Eiffel-Tower.jpg")
#background_image = cv2.imread("./Background/Nature-Scenery.jpg")
#background_image = cv2.imread("./Background/Sky.jpg")
#background_image = cv2.imread("./Background/Sky2.jpg")
#background_image = cv2.imread("./Background/Spotlight-Stage.jpg")
background_image = cv2.imread("./Background/Stage.jpg")
bg_height, bg_width, _ = background_image.shape

for path_img in os.listdir(directory_path):
    if path_img.endswith(".jpg"):
        input_image = cv2.imread(os.path.join(directory_path, path_img))
        img = cv2.resize(input_image, (bg_width, bg_height))
        
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        a_channel = lab[:,:,1]
        thresh = cv2.threshold(a_channel, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        #cv2.imshow("thresh", thresh)
        #cv2.waitKey(0)
        
        masked = cv2.bitwise_and(img, img, mask=thresh) # contains dark background
        #cv2.imshow("masked", masked)
        #cv2.waitKey(0)
        
        final = np.where(masked==0, background_image, masked)
        cv2.imwrite("./Result/" + f"Save_{path_img}", final)
        print(f"Save_{path_img}")
        cv2.putText(final, "Press any key to continue...", (int(bg_width/100), int(bg_height/20)), 
                    cv2.FONT_HERSHEY_COMPLEX, bg_height*0.002, (255, 255, 255), int(bg_height*0.004))
        cv2.imshow("final", final)
        cv2.waitKey(0)
cv2.destroyAllWindows()
