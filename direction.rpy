

init python:

    #object that manages quests for the direction screen.
    class direction():
        def __init__(self):
            self.bg = "direction_bg"
            self.current = [cat(), slippers()] #list of ongoing missions. quest objects.
            self.completed = [dog()] #list of succeeded or failed missions. quest objects.

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
        def complete_quest(self, quest):
            self.get_current().remove(quest)
            self.get_completed().append(quest)



    ## -- QUEST -- ##
    #quests. individual missions.
    ## -- Progress Special Values -- ##
    # 0: first phase.
    # -1: succeeded.
    # -2: failed.
    class quest():
        def __init__(self):
            self.chapter = 0 #int. determines what chapter quest expires at the start of

            self.title = "" #quest title
            self.progress = 0 #int. allows next actions to be done for quest.
            self.flavour = [] #list of quest description paragraphs. corresponds to a value of progress.

        #getters
        def get_chapter(self):
            return self.chapter
        def get_title(self):
            return self.title
        def get_progress(self):
            return self.progress
        def get_flavour(self):
            return self.flavour

        #setters
        def set_progress(self, x):
            self.progress = x

    class slippers(quest):
        def __init__(self):
            self.chapter = 1 #int. determines what chapter quest expires at the start of

            self.title = "Find my slippers" #quest title
            self.progress = 0 #int. allows next actions to be done for quest.
            self.flavour = [] #list of quest description paragraphs. corresponds to a value of progress.

    class cat(quest):
        def __init__(self):
            self.chapter = 1 #int. determines what chapter quest expires at the start of

            self.title = "Find my cat" #quest title
            self.progress = 0 #int. allows next actions to be done for quest.
            self.flavour = [] #list of quest description paragraphs. corresponds to a value of progress.

    class dog(quest):
        def __init__(self):
            self.chapter = 1 #int. determines what chapter quest expires at the start of

            self.title = "Find my dog" #quest title
            self.progress = 0 #int. allows next actions to be done for quest.
            self.flavour = [] #list of quest description paragraphs. corresponds to a value of progress.

























##eof
