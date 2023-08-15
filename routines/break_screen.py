from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard

def break_screen(win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort):

    # --- Initialize components for Routine "break" ---
    key_break = keyboard.Keyboard()
    text_break = visual.TextStim(win=win, name='text_break',
        text='休息時間\n請雙手離開鍵盤，且通知實驗者',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # --- Prepare to start Routine "break" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_break.keys = []
    key_break.rt = []
    _key_break_allKeys = []
    # keep track of which components have finished
    breakComponents = [key_break, text_break]
    for thisComponent in breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "break" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_break* updates
        waitOnFlip = False
        
        # if key_break is starting this frame...
        if key_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_break.frameNStart = frameN  # exact frame index
            key_break.tStart = t  # local t and not account for scr refresh
            key_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'key_break.started')
            # update status
            key_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_break.status == STARTED and not waitOnFlip:
            theseKeys = key_break.getKeys(keyList=['space'], waitRelease=False)
            _key_break_allKeys.extend(theseKeys)
            if len(_key_break_allKeys):

                # send trigger to port
                thisExp.addData('space_trigger', globalClock.getTime())
                serialPort.write(bytes(chr(3), 'utf8'))
                
                key_break.keys = _key_break_allKeys[-1].name  # just the last key pressed
                key_break.rt = _key_break_allKeys[-1].rt
                key_break.duration = _key_break_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_break* updates
        
        # if text_break is starting this frame...
        if text_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_break.frameNStart = frameN  # exact frame index
            text_break.tStart = t  # local t and not account for scr refresh
            text_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_break.started')
            # update status
            text_break.status = STARTED
            text_break.setAutoDraw(True)
        
        # if text_break is active this frame...
        if text_break.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            # if eyetracker:
            #     eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "break" ---
    for thisComponent in breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            thisComponent.tStopRefresh = tThisFlipGlobal
    # check responses
    if key_break.keys in ['', [], None]:  # No response was made
        key_break.keys = None
    thisExp.nextEntry()
    thisExp.addData('text_break.start', text_break.tStartRefresh)
    thisExp.addData('text_break.stop', text_break.tStopRefresh)
    thisExp.addData('key_break.keys', key_break.keys)
    if key_break.keys != None:  # we had a response
        thisExp.addData('key_break.rt', key_break.rt)
        # thisExp.addData('key_break.duration', key_break.duration)
    # thisExp.nextEntry()
    # the Routine "break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()