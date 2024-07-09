import matplotlib.pyplot as plt
import random as rd
import numpy as np

# Inputs
export_file_path="data.xyz"
population = 200
sick = 4 # percent
dt = 0.05 # time
Speed = 30 
Time = 50 # total time
Iteration = int(Time/dt)

plist = np.arange(population)
rd.shuffle(plist)





        


# init
pop = []
for i in range(population):
    pop.append(Person(rd.uniform(0,200),rd.uniform(0,200),rd.uniform(0,359)))
    pop[i].box(0,0,200,200)

saveXYZ(pop,'data.xyz')
# sick population 
for i in range(int(sick*population/100)):
    pop[plist[i]].stat=1



check = np.zeros([population,population])


SEl = np.zeros([Iteration])
REl = np.zeros([Iteration])
HEl = np.zeros([Iteration])
Vert = np.arange(Iteration)



for j in range(Iteration):
    # plt.subplot(2,1,1)
    SS =0
    RE =0
    HE =0
    for i in range(population):
        # pop[i].plot()
        pop[i].newPosition(Speed,dt)
        pop[i].updatestat()
        if pop[i].stat==1:
            SS+=1
        elif pop[i].stat==2:
            RE+=1
        else:
            HE+=1
    

    saveXYZ(pop,'data.xyz')
    # plt.show(block=False)
    # plt.plot([0,0,200,200,0],[0,200,200,0,0],'k',linewidth=1)
    # plt.title(j*dt)
    # plt.axis('off')
    # plt.axis('equal')
    
    SEl[j] =SS
    REl[j] =RE
    HEl[j] = HE



    # plt.subplot(2,1,2)
    # plt.bar(Vert,HEl, color='b', bottom =REl+SEl, width=1.8,label = 'Helth')
    # plt.bar(Vert,REl, color='g', bottom =SEl,width=1.8, label = 'Recover:'+str(RE))
    # plt.bar(Vert,SEl,color='r', width=1.8,label ='Sick:'+str(SS))
    # plt.legend()
    # plt.xticks(Ver, ('V1', 'V2', 'V3', 'V4', 'V5'))  



    # plt.pause(0.01)
    # plt.clf()

    if SS == 0:
        break
    for ii in range(population):
        for jj in range(ii):
            # print(ii,jj)
            pop[ii].neighber(pop[jj])

    


