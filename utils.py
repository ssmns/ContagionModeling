
def updatePos(x,vx,dt):
    return vx*dt+x


class Person:  
    # init method or constructor   
    def __init__(self, x , y , theta,stat = 0):  
        self.x = x 
        self.y = y
        if theta <0:
            theta = 360+theta
        else:
            pass
        self.thetad = theta
        theta = theta*np.pi/180
        self.vx = np.cos(theta)
        self.vy = np.sin(theta)
        self.theta = theta
        self.stat = stat
        self.timesick=0


    def box(self,x0,y0,xend,yend):
        self.x0 = x0
        self.y0 = y0
        self.xend = xend
        self.yend = yend


    def situation(self):
        xLength = [self.xend-self.x,self.x0-self.x,self.x0-self.x,self.xend-self.x]
        yLength = [self.yend-self.y,self.yend-self.y,self.y0-self.y,self.y0-self.y]
        angle   = [ 0 , 180 , 180 , 360]

        Angles=[]
        for i in range(len(xLength)):
            if yLength[i] != 0 :
                Angles.append(angle[i] + 180*np.arctan(xLength[i]/yLength[i])/np.pi)
            else :
                Angles.append(angle[i])

        self.ang = Angles
    
    def isInWalls(self,newx,newy):
        return (newx >= self.x0 and newx <= self.xend and newy >=self.y0 and newy <=self.yend)

    def neighber(self,other):
        R = np.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        if R<0.15:
            if (self.vx * other.vx) <0:
                self.vx = -self.vx
                other.vx = -other.vx
            else:
                pass

            if (self.vy * other.vy)<0:
                self.vy = -self.vy
                other.vy = -other.vy
            else:
                pass

        else:
            pass

        if (R < 1.0) and (self.stat == 1 or other.stat ==1):
            if (other.stat != 2 or self.stat !=2 ) :
                other.stat = 1
                self.stat  = 1
            else:
                pass
        else:
            pass



    def newPosition(self,V,dt):
        self.dt = dt
        newx = self.x+V*dt*self.vx
        newy = self.y+V*dt*self.vy
        # print(newx,newy)
        if self.isInWalls(newx,newy):
            self.x = newx
            self.y = newy
        elif newx >= self.xend or newx <= self.x0 :
            self.situation()
            self.vx = -self.vx
            self.x = self.x+V*dt*self.vx
        elif newy >= self.yend or newy <= self.y0 :
            self.vy = -self.vy
            self.y = self.y+V*dt*self.vy
        elif abs(newy)==abs(newx):
            self.vy = -self.vy
            self.vx = -self.vx
            self.x = self.x+V*dt*self.vx
            self.y = self.y+V*dt*self.vy
        else:
            pass

    
    def plot(self):
        if self.stat ==0 :
            plt.scatter(self.x,self.y, s=30, c='black', alpha=0.2)
            plt.scatter(self.x,self.y, s=2, c='black')
        elif self.stat ==1:
            plt.scatter(self.x,self.y, s=30, c='red', alpha=0.2)
            plt.scatter(self.x,self.y, s=2, c='red')
        elif self.stat == 2:
            plt.scatter(self.x,self.y, s=30, c='green', alpha=0.2)
            plt.scatter(self.x,self.y, s=2, c='green')

        else:
            pass
    def updatestat(self):
        if self.stat==1:
            self.timesick+=self.dt
        else:
            pass
        if self.timesick >= 14:
            self.stat =2
        else:
            pass




def saveXYZ(pop,file,option='a+'):
    f = open(file,option)
    f.write(str(len(pop))+'\n\n')
    for i in range(len(pop)):
        f.write(' %d  %f %f %f \n' % (pop[i].stat,pop[i].x,pop[i].y,0))
        # print(pop[i].x)
    f.close()
