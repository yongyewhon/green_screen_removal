# green_screen_removal
Remove green screen on images and replace with another background with OpenCV/Python

1. Load the images
2. Resize the images to the same size with background image
3. Convert image to LAB space
4. Threshold a-channel to remove green background
5. Apply the mask and then use bitwise_and
6. Check for matrix value 0 and replace it by the background image
7. Save final image
  
Final result:
![Save_1](https://github.com/yongyewhon/green_screen_removal/assets/151745867/47c0e8a6-1834-41eb-9bfa-b711a411ea2e)
![Save_3](https://github.com/yongyewhon/green_screen_removal/assets/151745867/2bdc16fb-496b-45d1-ba2d-d73965ff2bc4)
![Save_9](https://github.com/yongyewhon/green_screen_removal/assets/151745867/e192cb12-7719-4839-8882-167b783e7c9d)
![Save_10](https://github.com/yongyewhon/green_screen_removal/assets/151745867/017504f0-90f0-449d-84e6-acf6e603e0f2)
![Save_11](https://github.com/yongyewhon/green_screen_removal/assets/151745867/ae2da617-ed2c-4757-8be6-f3a5f34abf83)



