from functools import partial


class UI:
    def __init__(self, mode):
        self.mode = mode
        self.shell_mode(mode)

    def shell_mode(self, mode):
        if mode == "preprocessing":
            self.interactiveShell()

    def interactiveShell(self):
        running = True
        self.printManual()
        while running:
            val = input("Enter command (finish with 'q'): ")
            if val == "-lT":
                self.functionList.append(partial(self.lowerText))
            elif val == "-rP":
                self.functionList.append(partial(self.removePunctuation))
            elif val == "-rS":
                self.functionList.append(partial(self.removeSyntax))
            elif val == "-rSw":
                self.functionList.append(partial(self.removeStopWords))
            elif val == "-rN":
                self.functionList.append(partial(self.removeNumbers))
            elif val == "-rSc":
                self.functionList.append(partial(self.removeSingleChar))
            elif val == "-d":
                self.defaultSetting()
            elif val == "q":
                running = False
