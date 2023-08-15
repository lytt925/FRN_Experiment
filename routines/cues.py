from psychopy import visual, core
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)


trigger_mapping =  {'6|red_jar': chr(10), 
                    '6|blue_jar': chr(11),
                    '5|red_jar': chr(12),
                    '5|blue_jar': chr(13),
                    '9|red_jar': chr(14),
                    '9|blue_jar': chr(15),
                    '4|red_jar': chr(16),
                    '4|blue_jar': chr(17),
                    '3|red_jar': chr(18),
                    '3|blue_jar': chr(19)}


def cues(choice_jar, cueslist, img_cue_mapping, win, thisExp, routineTimer, globalClock, defaultKeyboard, serialPort):

    frameTolerance = 0.001
    endExpNow = False
    # --- Prepare to start Routine "cue" ---
    continueRoutine = True
    sendTrigger = False
    # update component parameters for each repeat
    # keep track of which components have finished

    cueComponents = []
    for i, cue in enumerate(cueslist):
        cueComponents.append(visual.ImageStim(win=win, pos=(-300+i*300, 0), image=img_cue_mapping[cue]))

    for thisComponent in cueComponents:
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

    # --- Run Routine "cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *ball* updates
        
        for ball in cueComponents:
            # if ball is starting this frame...
            if ball.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ball.frameNStart = frameN  # exact frame index
                ball.tStart = t  # local t and not account for scr refresh
                ball.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ball, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'ball.started')
                # update status
                ball.status = STARTED
                ball.setAutoDraw(True)
            
            # if ball is active this frame...
            if ball.status == STARTED:
                # update params
                pass
            
            # if ball is stopping this frame...
            if ball.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ball.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    ball.tStop = t  # not accounting for scr refresh
                    ball.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    # thisExp.timestampOnFlip(win, 'ball.stopped')
                    # update status
                    ball.status = FINISHED
                    ball.setAutoDraw(False)
    


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
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            if not sendTrigger:
                # send trigger to port
                eeg_trigger = trigger_mapping[f'{sum(cueslist)}|{choice_jar}']
                serialPort.write(bytes(eeg_trigger, 'utf8'))
                thisExp.addData('cue_trigger', globalClock.getTime())
                sendTrigger = True

    # --- Ending Routine "cue" ---
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            thisComponent.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.00000)
    
    thisExp.addData('cue.start', cueComponents[0].tStartRefresh)
    thisExp.addData('cue.stop', cueComponents[0].tStopRefresh)    
