# Real-Time-Facial-Expression-Recognition

Real time recognition of facial expressions using Keras, Flask and OpenCV.
Build and train a convolutional neural network (CNN) in Keras from scratch to recognize facial expressions. The data consists of 48x48 pixel grayscale images of faces. The objective is to classify each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). i have used OpenCV on haarcascade-file to automatically detect faces in images and draw bounding boxes around them.


# Link for Dataset:
You can find the original data here:
https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge
and split the data into train and test.


You can simply use the pre-trained models by running main.py .
And using ip mentioned in main.py file followed by .5000 you can open the interface in browser as we have used flask.

Before You run the program you will have to change the path of the video accordingly in camera.py. also you can give pass (0)
"self.video = cv2.VideoCapture(0)" to obtain Real Time Facial expression using your Webcam.

# To Run :
![Screenshot (55)_LI](https://user-images.githubusercontent.com/56965382/78216184-e6aad480-74d6-11ea-84fa-07729625227b.jpg)

# Here is the sample Output on Video:
1.
![Screenshot (61)](https://user-images.githubusercontent.com/56965382/78215376-050fd080-74d5-11ea-87bc-3c3a150a759c.png)
2.
![Screenshot (58)](https://user-images.githubusercontent.com/56965382/78215572-6899fe00-74d5-11ea-89b1-9219e8b5b685.png)
