# Processing Animation ABC Project
This project was designed to teach young children or those with diverse learning styles to learn the alphabet, along with an image association. 


## Table of Contents

 
* [General info](#general-info)
* [Technologies Used](#technologiesused)
* [Features](#Features)
* [Screenshots](#Screenshots)
* [Setup](#Setup)
* [Usage](#Usage)
* [Project Status](#ProjectStatus)
* [Room for Improvement](#RoomForImprovement)
* [Acknowledgements](#Acknowledgements)
* [Contact](#Contact)

## General info
This project was created on Processing 4 to create an animation smoothly. 
My project's intention and purpose is to teach the alphabet in a manner that is easy to engage with and simple to understand, with simple images, colours and music that syncs up with the images. 
I decided to create this project as I have an interest in diverse education and the development of young minds, exploring alternative ways that this can be done. 

## Technologies Used
- Processing 4
- Macbook
- Chrome

## Features
The features of this project include an animation of the alphabet, with each letter being accompanied by an image of something beginning with that letter. There was also a pattern used with the colour scheme for smoother aesthetics. 
I included a 'reset' button that allows the user to click it and go back to the beginning of the presentation if they wish.

## Screenshots
Feature 1 - Alphabet letter with a corresponding colour-coded image.

<img width="764" alt="Screenshot 2024-11-08 at 8 16 02 pm" src="https://github.com/user-attachments/assets/56bd0ee8-a25a-458b-b0da-9b89f0779b7e">

Feature 2 - Interactive reset button.

<img width="143" alt="Screenshot 2024-11-08 at 8 16 07 pm" src="https://github.com/user-attachments/assets/85dbade0-4261-4e66-9a66-100a3dfbd393">

## Setup
This project required the use of Processing 4. It also required the utilisation of the project's library to be able to add images to the animation. To complete this kind of project, you would simply download Processing 4 and add images to the file's library. You would also need to familiarise yourself with code commands. I found the following links useful.

https://quickref.me/python.html - Python Commands

https://py.processing.org/reference/ - Processing References for Python

https://processing.org/tutorials/ - Processing Animation Tutorials

https://www.youtube.com/watch?v=InBy_qyXWPA&ab_channel=Mr.Cordiner - YouTube Tutorial for Processing Animation Beginners.

## Usage
To use Processing to animate, you will need to do the following. 

Firstly, make sure that Python Mode for Processing by Jonathan Feinberg is downloaded, as Processing opens with Java and will not run this code. 
Install this by going to the top of the screen where it says Java and clicking it.
You then press manage modes, search Python and press Python Mode for Processing by Jonathan Feinberg. Once it is downloaded, press the Java symbol and change it to Python.
Make sure all the images from my GitHub file for "Data and Code" are downloaded into your Python processing folder. Once the images are added to the folder from the Git, it will run.

import time 
frame=0
last_frame = time.time()
images = []
def setup():
    global reset
    size(800, 600)

Firstly, we are referring to the images, beginning at frame 0. In Processing with Python, 0 will represent the first image, not 1. 
Size, (800, 600) refers to the size of the screen that will run. It is constructed like an x and y axis. This means 800 (X) represents the width while 600 (Y) represents the height of the image. 
'last_frame = time.time()' ensures that everything starts and finishes as it should in the loop without skipping the first image.

Then, the images you have saved into your project file library will need to be entered. To do this, you must load the image with its actual name. The image's actual name will be, for example, "Image.PNG". It will have a period, followed by the acronym for the file type. It will look something like this:

 letter_a = loadImage('a.png')
 letter_b = loadImage('b.png')
 
 etc.
 
You then would append the images:

  images.append(letter_a)
  images.append(letter_b)

etc.

If you were also adding a reset on top of the images, you would not need to append the image. If it was appended, it would be like adding an extra slide, which is not the idea. 

def draw():
    global frame, last_frame
    background(0)
    image(images[frame], 100, 100, 600, 400)
    image(reset, 600, 0, 200, 200)
    if (mousePressed and mouseX >600 and mouseY <200) :
        frame=0
        last_frame = time.time()
    if time.time() - last_frame > 2:
        frame = (frame + 1) % len(images)
        last_frame = time.time()    

'Def draw' or define draw is how we are going to paste the image in a certain spot.
Global frame and last frame means it'll show up on all frames.
'Background (0)' means the background colour for the images will be black, as 0 represents black.

The first image line 'image(images[frame], 100, 100, 600, 400)' is the code for positioning the images. This is where the image sits and its size.
The second line is for the image button's size.
The 'If mousePressed' command is for when clicking the reset button. Where the user clicks and where the image is on the screen must align. It will be greater than 600 on the X-axis and less than 200 on the Y-axis. 
The 'if time.time()' line represents how many seconds each image will play for; I have chosen 2 seconds.
The frame = '(frame + 1) % len(images)' line is for how the animation will loop back to the beginning once it has played all the images. The '% len(mgaes)' is for the loop. 
 

## Project Status
This project is complete.

## Room for Improvement
An improvement I could have made was to perhaps separate the corresponding images from the letter instead of making it all one image. This way, I could have potentially animated the images, as adding a transition would be more appealing to children, who are my target audience. 

I also could have added a sound features. I found it very difficult to include sound in the project, so I decided not to include it altogether. With further time, practice and troubleshooting, I believe this could have been achieved. 

## Acknowledgements
This project was inspired by alphabet songs taught in schools while giving it a unique and interactive twist.
I'd like to thank my tutor and head of Working with Data and Code for helping to educate myself and the cohort on coding.
Furthermore, I would not have been able to perfect this project without the help of the resources I have linked in the 'Setup' heading.

## Contact
This project was created by @Johannahhh. 
Feel free to contact me via my institution's email; johannah.s.schwiebert@student.uts.edu.au



