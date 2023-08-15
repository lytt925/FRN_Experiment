from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

def jar_reminder(choice_jar, win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort):
    # --- Initialize components for Routine "jar_reminder" ---
    text_jar_reminder = visual.TextStim(win=win, name='text_jar_reminder',
        text='你選擇的是',
        font='Open Sans',
        pos=(0, 320), height=24.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    img_jar_reminder = visual.ImageStim(
        win=win,
        name='img_jar_reminder', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), # tbd
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    img_jar_reminder.image = 'Stimuli/' + choice_jar + '.png'
    trigger_mapping = {'blue_jar': chr(92), 'red_jar': chr(91)}

    frameTolerance = 0.001
    endExpNow = False
    # --- Prepare to start Routine "jar_reminder" ---
    continueRoutine = True
    sendTrigger = False
    # update component parameters for each repeat
    # keep track of which components have finished
    jar_reminderComponents = [text_jar_reminder, img_jar_reminder]
    for thisComponent in jar_reminderComponents:
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

    # --- Run Routine "jar_reminder" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *img_jar_reminder* updates
        
        # if img_jar_reminder is starting this frame...
        if img_jar_reminder.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            img_jar_reminder.frameNStart = frameN  # exact frame index
            img_jar_reminder.tStart = t  # local t and not account for scr refresh
            img_jar_reminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_jar_reminder, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'img_jar_reminder.started')
            # update status
            img_jar_reminder.status = STARTED
            img_jar_reminder.setAutoDraw(True)
        
        # if img_jar_reminder is active this frame...
        if img_jar_reminder.status == STARTED:
            # update params
            pass
        
        # if img_jar_reminder is stopping this frame...
        if img_jar_reminder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_jar_reminder.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                img_jar_reminder.tStop = t  # not accounting for scr refresh
                img_jar_reminder.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'img_jar_reminder.stopped')
                # update status
                img_jar_reminder.status = FINISHED
                img_jar_reminder.setAutoDraw(False)

        # *text_jar_reminder* updates
        
        # if text_jar_reminder is starting this frame...
        if text_jar_reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_jar_reminder.frameNStart = frameN  # exact frame index
            text_jar_reminder.tStart = t  # local t and not account for scr refresh
            text_jar_reminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_jar_reminder, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_jar_reminder.started')
            # update status
            text_jar_reminder.status = STARTED
            text_jar_reminder.setAutoDraw(True)
        
        # if text_jar_reminder is active this frame...
        if text_jar_reminder.status == STARTED:
            # update params
            pass
        
        # if text_jar_reminder is stopping this frame...
        if text_jar_reminder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_jar_reminder.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_jar_reminder.tStop = t  # not accounting for scr refresh
                text_jar_reminder.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_jar_reminder.stopped')
                # update status
                text_jar_reminder.status = FINISHED
                text_jar_reminder.setAutoDraw(False)
        
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
        for thisComponent in jar_reminderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            if not sendTrigger:
                # send trigger to port
                serialPort.write(bytes(trigger_mapping[choice_jar], 'utf8'))
                thisExp.addData('jar_reminder_trigger', globalClock.getTime())   
                sendTrigger = True

    # --- Ending Routine "jar_reminder" ---
    for thisComponent in jar_reminderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            thisComponent.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    thisExp.addData('jar_or_miss.start', img_jar_reminder.tStartRefresh)
    thisExp.addData('jar_or_miss.stop', img_jar_reminder.tStopRefresh)