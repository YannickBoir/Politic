# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:46:51 2023

@author: yanni
"""

nb_postes = 7
dict_list = {
    "Gennaro"       : 15,
    "Bret"          : 5,
    "ecoexistons"   : 5
    }

nb_votants = 0
for key in dict_list :
    nb_votants = nb_votants + dict_list[key]
print("nombre de votants : " + str(nb_votants))
quotien_elec = nb_votants/nb_postes
print("Quotient électoral est : " + str(quotien_elec))

dict_result = dict()
nb_elu = 0
for key in dict_list :
    dict_result[key] = int(dict_list[key]/quotien_elec)
    nb_elu = nb_elu + int(dict_list[key]/quotien_elec)
j=1
print ('tour 1')
for key in dict_list :
    print(key + " : " + str(dict_result[key]))
while nb_elu < nb_postes :
    i=0
    tamp_key = ""
    for key in dict_list :
        if dict_list[key] - (dict_result[key] * quotien_elec) > i :
            i=dict_list[key] - (dict_result[key] * quotien_elec)
            tamp_key = key
        elif dict_list[key] - (dict_result[key] * quotien_elec) == i :
            if dict_list[key] > dict_list[tamp_key] :
                i=dict_list[key] - (dict_result[key] * quotien_elec)
                tamp_key = key
            elif dict_list[key] < dict_list[tamp_key] :
                i=dict_list[tamp_key] - (dict_result[tamp_key] * quotien_elec)
            else :
                tamp = input("Qui est le plus âgé entre le candidat numéro "+ str(dict_result[key]+1) + " de la liste "+key+ " et le candidat numéro "+str(dict_result[tamp_key]+1)+" de la liste "+tamp_key+" ? Tapez '1' pour "+key+" ou '2' pour " + tamp_key+'\n')
                tamp = int(tamp)
                while (tamp != 1 and tamp != 2) :
                    tamp = input("Erreur de saisie .. Merci de recommencer : Qui est le plus âgé entre le candidat numéro "+ str(dict_result[key]+1) + " de la liste "+key+ " et le candidat numéro "+str(dict_result[tamp_key]+1)+" de la liste "+tamp_key+" ? Tapez '1' pour "+key+" ou '2' pour " + tamp_key+'\n')
                if tamp == 1 :
                    i=dict_list[key] - (dict_result[key] * quotien_elec)
                    tamp_key = key
                else :
                    i=dict_list[tamp_key] - (dict_result[tamp_key] * quotien_elec)
                    tamp_key = tamp_key
    dict_result[tamp_key] = dict_result[tamp_key] + 1
    nb_elu = nb_elu + 1
    j = j+1
    print ('\ntour '+str(j))
    for key in dict_list :
        print(key + " : " + str(dict_result[key]))
        
print("\nresultat final")
for key in dict_list :
    print(key + " : " + str(dict_result[key]))