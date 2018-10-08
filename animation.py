# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:15:50 2018

@author: Ron

This is a small collection of functions to record, 
edit and save time animation movie with the computer's camera
"""

import cv2
import numpy as np


def setup_camera_and_get_images():
    """
    This function opens the computer’s camera #0 and stream the video to the screen.
   (if this is not the camera that facing the right direction, change the number in 
   cv2.VideoCapture(0) from “0” to “1”) Click on "i" add the current frame to the 
   animation video.
    """
    cap = cv2.VideoCapture(0)    
    video = []
    i=0
    while True:
        _, frame = cap.read()
        cv2.imshow('', frame)
        k = cv2.waitKey(30)
        if k==27:
            break
        if k==ord('i'):
            video.append(frame)
            i += 1
            print('Frame # {} is saved'.format(i))
    cv2.destroyAllWindows()
    cap.release()
    return video


def filter_bad_frames(video):
    """
    Flips through the frames that got added in the setup_camera_and_get_images
    function by clicking any key. Clicking on "i" will keep the frame in the animation, 
    clock on any other key will omit the frame from the video. This allow to remove 
    unwanted frame.
    ------------------------------------------------------------------------------------
    args:
        video (numpy array) - the animation video frames in a numpy array.
    returns:
        good_video (numpy array) - an array with the frames that were kept
    """
    
    good_video = []
    for f in video:
        cv2.imshow('',f)
        if cv2.waitKey(0)==ord('i'):
            good_video.append(f)
    cv2.destroyAllWindows()
    return good_video


def play_video(video, delay=100):
    """
    plays the video.
    ------------------------------------------------------------------------------------
    args:
        video (numpy array) - the animation video frames in a numpy array.'
        delay (int) - delay in milliseconds between frames
    returns:
        None
    """

    for f in video:
        cv2.imshow('', f)
        cv2.waitKey(delay)
    cv2.destroyAllWindows()


def save(video, name, fps=10):
    """
    Save the video as mp4 file
    ------------------------------------------------------------------------------------
    args:
        video (numpy array) - the animation video frames in a numpy array.
        name (str) - file name
        fps (int) - frame per second of the saved file
    returns:
        good_video (numpy array) - an array with the frames that were kept
    """

    heigth, width, _ = video[0].shape
    ffourc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(name, ffourc, fps, (width, heigth), 1)
    for f in video:
        out.write(f)
    out.release()
    
if __name__=='__main__':
    
    video = setup_and_get_images()
    view_resurlts(video,150)