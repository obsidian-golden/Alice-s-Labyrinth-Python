class BaseSkill:
    def __init__(self, name="", damage=0, accuracy=0, main=0, sub=0):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.main_type = main
        self.sub_type = sub
