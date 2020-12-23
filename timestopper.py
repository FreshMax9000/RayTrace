import time

class TimeStopper:

    def __init__(self):
        self._startTime = time.time()
        self._lastTimeCapture = time.time()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    """
    @property
    def startTime(self):
        
        return self._startTime
    """

    def getPassedTimeString(self, run, absoluteruns):
        timeForLatestCalc = time.time()- self._lastTimeCapture
        self._lastTimeCapture = time.time()
        returnString = "\nPixelRow took %d s."%(timeForLatestCalc)
        self.seconds += timeForLatestCalc
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        returnString += "\nAbsolute Time: %d h %d m and %d s."%(self.hours,self.minutes,self.seconds)
        estimatedseconds = (time.time()-self._startTime)*(absoluteruns/(run+1))
        returnString += "\nEstimated Absolutetime: %d m and %d s."%(estimatedseconds//60,estimatedseconds-(estimatedseconds//60)*60)
        return returnString
    


