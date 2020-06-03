

init python:

    #object that manages quests for the direction screen.
    class Direction():
        def __init__(self):
            self.bg = "direction_bg"
            self.current = [Slippers()] #list of ongoing missions. quest objects.
            self.completed = [] #list of succeeded or failed missions. quest objects.

            self.last_viewed = self.current[0] #last viewed quest on the direction screens. quest object

        #getters
        def get_bg(self):
            return self.bg
        def get_current(self):
            return self.current
        def get_completed(self):
            return self.completed
        def get_last_viewed(self):
            return self.last_viewed

        #setters
        def set_last_viewed(self, quest):
            self.last_viewed = quest

        #useful functions
        def end_of_chapter(self, chapter):
            #expires quests
            for quest in self.get_current():
                if quest.get_chapter() == chapter:
                    quest.set_progress(-2)
        def add_quest(self, quest):
            self.get_current().append(quest)
        def complete_quest(self, quest, state):
            quest.set_progress(state)
            self.get_completed().append(quest)



    ## -- QUEST -- ##
    #quests. individual missions.
    ## -- Progress Special Values -- ##
    #  0: not started.
    #  1: just started.
    # -1: succeeded.
    # -2: failed.
    class Quest():
        def __init__(self):
            self.chapter = 0 #int. determines what chapter quest expires at the start of
            self.flag = 0 #int. unique quest identifier.

            self.teaser = "" #title that shows up in the quest selection tab.
            self.title = "" #quest title
            self.progress = 0 #int. allows next actions to be done for quest.
            self.steps = 0 #int. max value of progress.

            self.flavour = [] #list of quest description paragraphs. corresponds to a value of progress.
            self.requirement = [] #list of requirement descriptions one line things. corresponds to progress.

        #getters
        def get_chapter(self):
            return self.chapter
        def get_flag(self):
            return self.flag
        def get_teaser(self):
            return self.teaser
        def get_title(self):
            return self.title
        def get_progress(self):
            return self.progress
        def get_steps(self):
            return self.steps
        def get_flavour(self):
            return self.flavour
        def get_requirement(self):
            return self.requirement

        #setters
        def set_progress(self, x):
            self.progress = x

    class Slippers(Quest):
        def __init__(self):
            self.chapter = 1 #int. determines what chapter quest expires at the start of
            self.flag = 1 #int. unique quest identifier.

            self.teaser = "Slippers" #title that shows up in the quest selection tab.
            self.title = "The Case of the Missing Slippers" #quest title
            self.progress = 2 #int. allows next actions to be done for quest.
            self.steps = 0 #int. max value of progress.
            self.flavour = ["please find my slippers", "find them again"] #list of quest description paragraphs. corresponds to a value of progress.
            self.requirement = ["find the slippers", "again buddy"] #list of requirement descriptions one line things. corresponds to progress.



























##eof
