
class Bucket:

    def __init__(self):
        self.MAXSIZEX = 6
        self.MAXSIZEY = 5
        #import pentomino list

    def generatePentomino(self):
        return random.sample(pentominoDict, 1)



class Town:

    def __init__(self):
        self.MAXSIZEX = 40
        self.MAXSIZEY = 40

    def generateStreet(self):
        pass

    def generateDeliveryLocation(self):
        pass

    def deliverToLocation(self):
        pass



def init():
    pass

def start():
    pass

def run():
    pass

if __name__ == "__main__":
    init()
    s = start()
    run()
