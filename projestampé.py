from random import uniform
import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,atan,pi

def nombre_d_abeilles ():
    '''Cette fonction prend en argument le nombre de particule constituant l'essaim particulaire, elle permet de créer l'essaim.'''
    global ensembleparticule
    question=int(input("Entrez le nombre d'abeilles constituant l'essaim : "))
    nombredeparticule=question
    ensembleparticule=particule(nombredeparticule)

def definition_de_l_abeille (nombredeparticule):
    '''Cette fonction définit les caractéristiques initiales de chaque particule.'''
    eparticule=[]
    for k in range (0,nombredeparticule):
        a=uniform(0.5,10)
        b=uniform(0.5,30)
        vitessea=uniform(-1,1)
        vitesseb=uniform(-1,1)
        abest,avbest,bbest,bvbest=a,a,b,b
        caracteristiqueparticule=[k,a,b,vitessea,vitesseb,abest,bbest,avbest,bvbest]
        eparticule.append(caracteristiqueparticule)
    return eparticule
    
def calcul_de_la_force_dans_le_verin (ensembleparticule):
    '''Cette fonction permet de calculer la force exercée dans le vérin en fonction des longueurs a et b stockées par chaque particule.'''
    totalforce=[]
    for k in range(0,len(ensembleparticule)):
        if (ensembleparticule[k][2]*sin(pi/6))/(ensembleparticule[k][2]*cos(pi/6)-ensembleparticule[k][1])>0:
            theta=atan((ensembleparticule[k][2]*sin(pi/6))/(ensembleparticule[k][2]*cos(pi/6)-ensembleparticule[k][1]))
        else:
            theta=atan((ensembleparticule[k][2]*sin(pi/6))/(ensembleparticule[k][2]*cos(pi/6)-ensembleparticule[k][1]))+pi
        beta=theta-pi/6
        force=(80*9.81*30*cos(pi/6))/(ensembleparticule[k][2]*sin(beta))
        
        totalforce.append(force)
    return totalforce

def caracteristique_de_l_essaim (ensembleparticule): 
    '''Cette fonction a pour but de retourner les longueurs a et b de chaque particule (liste utilisée lors de l'affichage).'''
    atotal=[]
    btotal=[]
    ensembletoto=[]
    for k in range (0,len(ensembleparticule)):
        atotal.append(ensembleparticule[k][1])
        btotal.append(ensembleparticule[k][2])
    ensembletoto.append(atotal)
    ensembletoto.append(btotal)
    return [atotal,btotal]

def meilleure_voisine(k,ensembleparticule):
    caracteristiqueparticule=ensembleparticule[k]
    L=[]
    a=caracteristiqueparticule[1]
    b=caracteristiqueparticule[2]
    xbest=[0,0]
    Fbest=[1000000]
    for i in range (0,len(ensembleparticule)) :
        if abs(a-ensembleparticule[i][1]) <= 1:
            if abs(b-ensembleparticule[i][2]) <= 3:
                L+= [ensembleparticule[i]]
            else:
                1+1
        else:
            1+1
    for j in L :
        F=calcul_de_la_force_dans_le_verin([j])
        if F<Fbest :
            xbest=[j[5],j[6]]
            Fbest=F
        else :
            1+1
    ensembleparticule[k][7],ensembleparticule[k][8]=xbest[0],xbest[1]
    
def deplacement_de_l_abeille(k,ensembleparticule):
    r2=uniform(0,1)
    r3=uniform(0,1)
    v=np.array([ensembleparticule[k][3],ensembleparticule[k][4]])
    x=np.array([ensembleparticule[k][1],ensembleparticule[k][2]])
    xbest=np.array([ensembleparticule[k][5],ensembleparticule[k][6]])
    xvbest=np.array([ensembleparticule[k][7],ensembleparticule[k][8]])

    v=0.73*(0.1*v+2.05*r2*(xbest-x)+2.05*r3*(xvbest-x))
    x=x+v
    ensembleparticule[k]=[k,x[0],x[1],v[0],v[1],xbest[0],xbest[1],xvbest[0],xvbest[1]]

def la_meilleure_abeille(k,ensembleparticule):
    Fc=calculforce([ensembleparticule[k]])
    Fb=calculbestforce([ensembleparticule[k]])
    if Fc<Fb :
        ensembleparticule[k][5],ensembleparticule[k][6]=ensembleparticule[k][1],ensembleparticule[k][2]

def affichage_de_l_essaim():
    ensembletoto=listetoto(ensembleparticule)
    x=ensembletoto[0]
    y=ensembletoto[1]
    plt.plot(x,y,'x  ')
    plt.xlabel("Valeurs de a")
    plt.ylabel("Valeurs de b")
    plt.title("Recherche du minimum local")
    plt.show()

def essaim (ensembleparticule):
    for k in range (0,len(ensembleparticule)):
        a_la_recherche_des_abeilles_perdues(k,ensembleparticule)
        la_meilleure_abeille(k,ensembleparticule)
        meilleure_voisine(k,ensembleparticule)
        vitesse_maximale_autorisee_pour_les_abeilles()
        deplacement_de_l_abeille(k,ensembleparticule)
        
def vitesse_maximale_autorisee_pour_les_abeilles():
        for k in range (0,len(ensembleparticule)):
            if (ensembleparticule[k][3]**2+ensembleparticule[k][4]**2)**0.5>3:
                
                ensembleparticule[k][3]=(ensembleparticule[k][3])/abs(ensembleparticule[k][3])
                ensembleparticule[k][4]=(ensembleparticule[k][4])/abs(ensembleparticule[k][4])
                
def determinons_le_minimum_local():
    compteur=0
    for k in range (0,50):
        compteur+=1
        essaim (ensembleparticule)
        if compteur==1 or compteur==5:
            affichage_de_l_essaim()
    affichage_de_l_essaim()
    
def a_la_recherche_des_abeilles_perdues(k,ensembleparticule):
    new_a=uniform(0.5,10)
    new_b=uniform(0.5,30)
    if ensembleparticule[k][1]>10 or ensembleparticule[k][1]<0.5:
        ensembleparticule[k][1]=new_a
    elif ensembleparticule[k][2]<0.5 or ensembleparticule[k][2]>30:
        ensembleparticule[k][2]=new_b
        
def determinons_le_minimum_local():
    nombre_d_abeilles()
    compteur=0
    for k in range (0,50):
        compteur+=1
        essaim (ensembleparticule)
        if compteur==1 or compteur==5:
            affichage_de_l_essaim()
    affichage_de_l_essaim()
    resultat(ensembleparticule)
    
def resultat (ensembleparticule):
    '''Cette fonction retourne les valeurs a et b minimales comprisent dans l'intervalle souhaité ainsi que l'effort dans le vérin correspondant'''
    calcul=calculforce(ensembleparticule)
    listestockage=[]
    for k in range (0,len(ensembleparticule)):
        if ensembleparticule[k][1]>0.5 and ensembleparticule[k][1]<10 and ensembleparticule[k][2]>0.5 and ensembleparticule[k][2]<30:
            listestockage.append(ensembleparticule[k])
        else:
            1+1
    meilleureabeille=listestockage[0][0]
    for k in range (0,len(ensembleparticule)):
        if calcul[k]<calcul[meilleureabeille] and ensembleparticule[k][1]>0.5 and ensembleparticule[k][1]<10 and ensembleparticule[k][2]>0.5 and ensembleparticule[k][2]<30:
            meilleureabeille=k
        else:
            1+1
    resultat=[ensembleparticule[meilleureabeille][1],ensembleparticule[meilleureabeille][2],calcul[meilleureabeille]]
    print (resultat)