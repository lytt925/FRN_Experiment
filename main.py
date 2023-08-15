#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on 七月 26, 2023, at 10:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import serial #Import the serial library
serialCom3 = serial.Serial(
    port='COM3',
    baudrate=115200,
    bytesize=8,
    #parity=None,
    stopbits=1,
    timeout=None,
)
import pandas as pd



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'weichen'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{np.random.randint(0, 999999):06.0f}",
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='',
    savePickle=False, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 


# point serialPort to device at port 'COM3' and make sure it's open
serialPort = serialCom3
serialPort.status = NOT_STARTED
if not serialPort.is_open:
    serialPort.open()

# Prepare Cues
df = pd.read_csv('database.csv')
arr = np.array(['bbb', 'bbr', 'nnn', 'brr', 'rrr' ]) # 五種情況
cond_array = np.repeat(arr , [180,60,40,60,180], axis=0) # 以上述比例重複
np.random.shuffle(cond_array) #重排
img_cue_mapping = {1: 'Stimuli/0.png', 2: 'Stimuli/1.png', 3: 'Stimuli/null_2.png'}
subj_correctness_list = []


from routines.instruction import instruction
from routines.text_only import text_only
from routines.choice import choice
from routines.jar_reminder import jar_reminder
from routines.cues import cues
from routines.break_screen import break_screen

fixation1 = {'name': 'fixation_1', 
             'text': '+', 
             "pos": (0,0), 
             "height": 48,
             "eeg_trigger": chr(95)}
fixation2 = {'name': 'fixation_2', 
             'text': '+', 
             "pos": (0,0), 
             "height": 48,
             "eeg_trigger":  chr(96)}
fixation3 = {'name': 'fixation_3', 
             'text': '+', 
             "pos": (0,0), 
             "height": 48,
             "eeg_trigger":  chr(97)}

## inst
instruction(win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort)


for trial in range(520):
    # add Trial number
    thisExp.addData('trial', trial+1)

    ## fixation_1 0.5s
    text_only(text_config=fixation1, duration=0.5, win=win, thisExp=thisExp, 
              routineTimer=routineTimer, globalClock=globalClock, defaultKeyboard=defaultKeyboard, serialPort=serialPort)

    ## choice
    jar_img_map, trial_choice = choice(win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort)

    # -- Prepare stimlus for Routine "jar_reminder" --- 
    try:
        choice_jar = jar_img_map[trial_choice]
        miss = False
    except:
        miss = True
    
    if not miss:
        ## jar_reminder
        jar_reminder(choice_jar, win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort)

        ## fixation_2 0.5s
        text_only(text_config=fixation2, duration=0.5, win=win, thisExp=thisExp, 
                routineTimer=routineTimer, globalClock=globalClock, defaultKeyboard=defaultKeyboard, serialPort=serialPort)

        # Choose the Cue 
        subset = df[df.cond == cond_array[trial]] # all rows w/ condition == current trial
        current_trial = subset.sample(n=1).iloc[0]
        print(current_trial)
        cueslist = current_trial[['result_1', 'result_2', 'result_3']].tolist()
        jar_mapping = {1: 'blue_jar', 2: 'red_jar'}
        ans_jar = jar_mapping[current_trial['jar']] # get the color of the jar: 'blue_jar' or 'red_jar'

        ## cue
        cues(choice_jar, cueslist, img_cue_mapping, win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort)

        ## fixation_3 0.7s
        text_only(text_config=fixation3, duration=0.7, win=win, thisExp=thisExp, 
                routineTimer=routineTimer, globalClock=globalClock, defaultKeyboard=defaultKeyboard, serialPort=serialPort)

        ## feedback 0.5s
        isCorrect = ans_jar == choice_jar
        if isCorrect:
            thisExp.addData('isCorrect', 1)
            text_feedback = '+200'
            subj_correctness_list.append(200)
        else:
            thisExp.addData('isCorrect', 0)
            text_feedback = '+0'
            subj_correctness_list.append(0)

        ## decide trigger
        feedback_trigger = {
            'True|red_jar|6': chr(101),
            'True|blue_jar|3':chr(191),
            'True|red_jar|5' : chr(121),
            'True|blue_jar|4': chr(171),
            'False|red_jar|3': chr(180),
            'False|blue_jar|6': chr(110),
            'False|red_jar|4': chr(160),
            'False|blue_jar|5': chr(130),
            'True|red_jar|3' : chr(181),
            'True|blue_jar|6': chr(111),
            'True|red_jar|4': chr(161),
            'True|blue_jar|5': chr(131),
            'False|red_jar|6': chr(100),
            'False|blue_jar|3': chr(190),
            'False|red_jar|5': chr(120),
            'False|blue_jar|4': chr(170),
            'False|red_jar|9': chr(140),
            'False|blue_jar|9': chr(150),
            'True|red_jar|9': chr(141),
            'True|blue_jar|9': chr(151)
        }

        text_only(text_config={"name": "feedback", 
                               "text": text_feedback, 
                               "height": 72,
                               "pos": (0,0),
                               "eeg_trigger": feedback_trigger[f'{isCorrect}|{choice_jar}|{sum(cueslist)}']}, 
                               duration=1, win=win, thisExp=thisExp, routineTimer=routineTimer, globalClock=globalClock, defaultKeyboard=defaultKeyboard, serialPort=serialPort)
            
    elif miss:
        ## miss
        text_only(text_config={"name": "jar_or_miss", 
                               "text": "Missed", 
                               "height": 48,
                               "pos": (0,0),
                               "eeg_trigger": chr(93)}, duration=0.5, win=win, thisExp=thisExp, routineTimer=routineTimer, globalClock=globalClock, defaultKeyboard=defaultKeyboard, serialPort=serialPort)
            
    if trial == 258: # Break after the trial of no. 259 trial (index = 258)
        ## break
        break_screen(win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort)

    # record next trial
    thisExp.nextEntry()

## reward
final_reward = np.random.choice(subj_correctness_list)
text_only(text_config={"name": "reward", 
                        "text": f'實驗結束\n本實驗得到的實驗報酬是 {final_reward} 法幣\n請通知實驗人員', 
                        "height": 36,
                        "pos": (0,0),
                        "eeg_trigger": chr(98)}, duration=5, win=win, thisExp=thisExp, routineTimer=routineTimer, defaultKeyboard=defaultKeyboard)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
# thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
