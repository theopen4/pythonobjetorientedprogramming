class Toolsbox:
    """difine one toolsbox"""
    def __init__(self):
        #init tools
        self.tools = []

        #add tool
    def add_tool(self,tool) :
        pass  

    def remove_tool(self,tool):
        #remove tools 
        pass


class Hammer:
    """define hammer"""
    def __init__(self,color="red") :
        #init colors
        self.color = color

    def paint(self,color):
        """paint hammer"""
        self.color = color
        pass

    def hammer_in(self,nail):
        """drive the nail"""
        pass

    def remove_nail(self,nail):
        """remove nail"""
        pass

        class screwdriver:
            """define screwdriver"""
            def __init__(self, size):
                # init size
                self.size = size

            def tighten_screw(self,screw):
                """tighten screw"""    
                pass
            def loosen_screw(self,screw):
                """loosen screw"""
                pass

class Crewn:
    """vis"""
    MAX_TIGHTNESS = 5
    def __init__(self) :
        """initialise le degre de  serage"""
        self.tightness = 0 

    def loosen(self):
        """loosen crewn"""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """tighten crewn"""
        if self.tightness < 0:
            self.tightness += 1

    def __str__(self):
        """retourne une forme visible de l objet"""
        return "the tighten screw is {}".format(self.tightness)   


        


        