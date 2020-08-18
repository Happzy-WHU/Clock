from datetime import datetime,time
class stage:

    timeStack=[]
    isLate=True
    isEarly=True
    isAbsent=True

    def check(self,t_hour):
        self.timeStack.append(t_hour)

    def judgeThree1(self,t_hour):
        if len(self.timeStack)==0:
            self.isLate=False
            self.isEarly=False
            self.isAbsent=True

        else:
            for o in self.timeStack:
                if o<=8:
                    self.isLate=False
                if o>=11 and o<12:
                    self.isEarly=False

    def judgeThree2(self, t_hour):
        if len(self.timeStack)==0:
            self.isLate = False
            self.isEarly = False
            self.isAbsent = True

        else:
            for o in self.timeStack:
                if o >= 17 and o<18:
                    self.isEarly = False
                if o < 14:
                    self.isLate = False





