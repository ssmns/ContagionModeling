import matplotlib.pyplot as plt


def plotXYZ(file):
    f = open(file,'r')
    try:
        while True:
            plt.show(block=False)
            plt.plot([0,0,200,200,0],[0,200,200,0,0],'k',linewidth=1)
            plt.axis('off')
            plt.axis('equal')

            num = int(f.readline())
            f.readline()
            TPYl =[]
            Xl =[]
            Yl =[]
            Zl = []
            for i in range(num):
                STR = f.readline().split(' ')
                STR.remove('')
                STR.remove('')
                # print(STR)
                TPYl.append(int(STR[0]))
                Xl.append(float(STR[1]))
                Yl.append(float(STR[2]))
                Zl.append(float(STR[3]))


            for i in range(num):
                TPY = TPYl[i]
                X = Xl[i]
                Y = Yl[i]
                if TPY==0 :
                    plt.scatter(X,Y, s=30, c='black', alpha=0.2)
                    plt.scatter(X,Y, s=2, c='black')
                elif TPY ==1:
                    plt.scatter(X,Y, s=30, c='red', alpha=0.2)
                    plt.scatter(X,Y, s=2, c='red')
                elif TPY == 2:
                    plt.scatter(X,Y, s=30, c='green', alpha=0.2)
                    plt.scatter(X,Y, s=2, c='green')
                else:
                    pass

            plt.pause(0.001)
            plt.clf()
        # plt.show()
    except:
        pass
    


plotXYZ('data.xyz')
