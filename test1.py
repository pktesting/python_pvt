class Enemy:
    life = 3
    def attack(self):
        print ("ouch")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print ("I am dead ")
        else:
            print (str(self.life) + " life left")

'''to getting things from a class , we create an object
 here we make two objs  , both objs behave as unique '''
enemy1 = Enemy()
enemy2 = Enemy()


enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()



