class BaseSkill:
    def __init__(self, name="", power=0, accuracy=0, main=0, sub=0):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.main_type = main
        self.sub_type = sub

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_accuracy(self):
        return self.accuracy

    def get_main_type(self):
        return self.main_type

    def get_sub_type(self):
        return self.sub_type
