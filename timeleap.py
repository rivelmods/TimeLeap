print("Initializing the program...")

import os
import time
import subprocess
import getopt
import sys
import pyautogui

def clear_screenshots():
    print()
    clear = input("Do you wish to clear the screenshots folder? (y/n): ")

    if clear.lower() == 'y':
        clear_cmd = "rm screenshots/*"
        subprocess.run(clear_cmd, shell=True)
    else:
        sys.exit(2)


def render_video(fps):
    render_choice = input("Do you want to render the video? (y/n): ")

    if render_choice.lower() == 'y':
        video_name = input("What do you want to name the output video?: ")

        render_cmd = f"cd screenshots && ffmpeg -framerate {fps} -pattern_type glob -i '*.png' \
      -c:v libx264 -pix_fmt yuv420p out.mp4"

        subprocess.run(render_cmd, shell=True)
        os.rename("screenshots/out.mp4", "output/" + video_name +".mp4")

        clear_screenshots()
        print('Thank you for using the program.')

    else:
        print()
        print('Thank you for using the program.')


def record(record_time):
    count = 1
    images = []
    recording = True

    while recording:
        image = pyautogui.screenshot()
        image.save('screenshots/image_' + str(count) + '.png')
        count += 1
        images.append(image)
        time.sleep(1)

        if len(images) == record_time:
            print('Recording is done')
            break
        else:
            print('Recording', end="\r", flush=True)

def get_args(argv, record_time, fps):
    try:
        opts, args = getopt.getopt(argv, "r:f:", ["record_time=", "fps="])
    except getopt.GetoptError:
        print('ERROR: usage - timeleap.py -r <record_time> -f <fps>')
        sys.exit(2)

    if not opts:
        print('ERROR: usage - timeleap.py -r <record_time> -f <fps>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-r", "--record_time"):
            record_time = int(arg)
        elif opt in ("-f", "--fps"):
            fps = arg

    return record_time, fps


def main(argv):
    record_time = ''
    fps = ''

    record_time, fps = get_args(argv, record_time, fps)

    record(record_time)
    render_video(fps)

if __name__ == '__main__':
    main(sys.argv[1:])
