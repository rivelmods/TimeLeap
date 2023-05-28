# Timelapse
A simple command line timelapse recorder made for my personal use.

> :warning: This program only works in unix based systems

### Dependencies
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [ffmpeg](https://ffmpeg.org/)
- [python3](https://www.python.org/)

you can use [brew](https://brew.sh/) to install ffmpeg, which is a video encoder used in the program, using this command or from the official website.

```
brew install ffmpeg
```
pyautogui is a python library used for taking screenshots, which you can download using [pip](https://pypi.org/project/pip/) which you already know is a package manger for python.

```
pip3 install pyautogui
```

If you encouter some kind of error with pyautogui, you can try install [Pillow](https://pypi.org/project/Pillow/) with pip, which will fix it.

```
pip3 install Pillow
```
### How to use

You can pass in two arguments the time you want to record and the fps of the finished project. Once you enter the command it will record a timelapse for the given amount of time. It will ask you if you want to render the video, in case you want to use an external program to do it. After rendering, you will find the video in the output folder.
And it will also ask you if you want to clear the screenshots folder if you are no longer going to use the images. The command is give below. Replace record_time and fps with your desired values.

```
python3 timelapse.py -r <record_time> -f <fps>
```

