class Batsman:
    def __init__(self, batsman1="", batsman2="", runs1="", runs2="", balls1="", balls2="", four1="", four2="", six1="", six2=""):
        self.bat1 = batsman1
        self.bat2 = batsman2
        self.run1 = runs1
        self.run2 = runs2
        self.ball1 = balls1
        self.ball2 = balls2
        self.f1 = four1
        self.f2 = four2
        self.six1 = six1
        self.six2 = six2

    def OneBatsman(self):
        disp1 = "{} {} ({})  4 X {} | 6 X {}".format(self.bat1, self.run1, self.ball1, self.f1, self.six1)
        return disp1

    def TwoBatsmen(self):
        disp1 = "{} {} ({})  4 X {} | 6 X {}                      ".format(self.bat1, self.run1, self.ball1, self.f1, self.six1)
        disp2 = "{} {} ({})  4 X {} | 6 X {}                      ".format(self.bat2, self.run2, self.ball2, self.f2, self.six2)
        return disp1, disp2   
    

class Bowler:

    def __init__(self, bowler1="", bowler2="", over1="", over2="", runsconceded1="", runsconceded2="", maiden1="",
                 maiden2="", wicket1="", wicket2=""):
        self.bow1 = bowler1
        self.bow2 = bowler2
        self.over1 = over1
        self.over2 = over2
        self.rn1 = runsconceded1
        self.rn2 = runsconceded2
        self.maid1 = maiden1
        self.maid2 = maiden2
        self.wick1 = wicket1
        self.wick2 = wicket2

    def OneBowler(self):
        dis1 = "{}  {}-{}-{}-{}".format(self.bow1, self.over1, self.maid1, self.rn1, self.wick1)
        return dis1

    def TwoBowler(self):
        dis1 = "{}  {}-{}-{}-{}               ".format(self.bow1, self.over1, self.maid1, self.rn1, self.wick1)
        dis2 = "{}  {}-{}-{}-{}               ".format(self.bow2, self.over2, self.maid2, self.rn2, self.wick2)
        return dis1, dis2


class Score:

    def __init__(self, score="", overs="", wickets=""):
        self.score = score
        self.over = overs
        self.wicket = wickets

    def total(self):
        Scoreboard = "{} / {} in {}      ".format(self.score, self.wicket, self.over)
        return Scoreboard
