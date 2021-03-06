import numpy as np

x = np.array([73825 , 58825  , 55825 , 51025 , 52625 , 58625 , 51625 , 46425 , 47025, 44225,  42025 , 41625, 34425 , 36625 , 38225 , 41425, 40825, 43425, 47425, 54225, 50625, 56825, 59625, 54225, 49825, 45025, 37425, 34225, 34625, 33825, 32425, 30425, 26425, 22025, 24625, 24825, 26425, 29625, 26625, 33625, 33225, 41625, 46825, 47025, 55225, 59625, 64425, 67225, 69425, 66025, 66025, 60425, 57025, 54625, 53825, 48625, 42825, 42825, 42025, 36825, 29425, 29025, 29425, 31625, 34025, 30000, 26225, 14825, 13025, 14825, 18025, 18425, 18025, 17425, 13825, 8625 , 12225, 7225 , 10025, 5825 , 11625, 9025, 5625  , 4625, 4425  , 3825])
y = np.array([284125,246125  , 134125, 160125, 316125, 482125, 446125, 228125, 162125, 56125, 180125, 238125, 98125, 184125, 274125,374125,454125,490125,502125,554125,566125,608125,658125,654125,626125,574125,496125,442125,378125,318125,264125,186125,132125,132125,176125,212125,262125,344125,442125,532125,580125,658125,678125,714125,722125,714125,710125,728125,786125,806125,846125,840125,772125,812125,842125,850125,864125,786125,752125,840125,840125,742125,716125,676125,642125,600000,588125,142125,168125,222125,330125,396125,482125,568125,330125,336125,414125,412125,480125,496125,540125,556125,558125,694125,734125,802125])

anotasi = ["J", "A","B" ,"D" , "E" ,  "F","H"  ,"K"  ,"L"  ,"M"  ,"N"  ,"O"  ,"P"  ,"Q"  ,"R" ,"S","T","U","V","W","Z","A_1","B_1","C_1","D_1","E_1","F_1","G_1","H_1","I_1","J_1","K_1","L_1","M_1","N_1","O_1","P_1","Q_1","R_1","S_1","T_1","U_1","V_1","W_1","Z_1","A_2","B_2","C_2","D_2","E_2","F_2","G_2","H_2","I_2","J_2","K_2","L_2","M_2","N_2","O_2","P_2","Q_2","R_2","S_2","T_2","U_2","V_2","W_2","Z_2","A_3","B_3","C_3","D_3","E_3","F_3","G_3","H_3","I_3","J_3","K_3","L_3","M_3","N_3","O_3","P_3","Q_3"]
an_urut = ["J","A", "B", "M", "P","L_1", "M_1", "W_2", "Z_2", "A_3", "P_1", "B_3", "F_3", "G_3", "I_3", "H_3", "J_3", "K_3", "L_3", "M_3", "N_3", "O_3", "P_3", "Q_3", "E_3", "D_3", "C_3", "R_1", "Q_1", "I_1", "J_1","O_1", "N_1", "K_1", "Q", "N", "L", "D", "K", "O", "R", "S", "H_1", "G_1", "F_1", "S_1", "T_1", "V_2", "U_2", "T_2", "S_2", "R_2", "Q_2", "P_2", "O_2", "L_2", "K_2", "J_2", "G_2","F_2" , "E_2"       , "D_2", "C_2", "B_2", "A_2", "Z_1", "H_2", "I_2", "M_2", "N_2", "W_1", "V_1", "U_1", "D_1", "C_1", "B_1", "A_1", "W", "Z","E_1", "V", "U", "T", "F", "H", "E"]
print(len(anotasi), len(an_urut))

ori = [1, 2, 9, 12, 32, 33, 67, 68, 69, 36, 70, 74, 75, 77, 76, 78, 79, 80, 81, 82, 83, 84, 85, 73, 72, 71, 38, 37, 29, 30, 35, 34, 31, 13, 10, 8, 3, 7, 11, 14, 15, 28, 27, 26, 39, 40, 65, 66, 64, 63, 62, 61, 60, 59, 56, 55, 54, 51, 64, 60, 50, 48, 47, 2, 45, 44, 52, 53, 57, 58, 43, 42, 41, 24, 23, 38, 21, 19, 20, 25, 18, 17, 16, 5, 6, 4]
uji = [80,72,38,28,15,4,0,1,7,10,13,31,34,35,30,14,70,74,75,71,77,76,78,79,66,65,64,43,44,52,53,54,55,56,59,60,85,84,83,82,36,69,68,67,33,32,12,9,2,3,8,11,29,37,27,47,48,49,50,51,57,58,61,62,63,41,42,45,46,22,23,24,21,19,18,5,6,16,17,26,39,20,25,40,73,81]

weight = [0,1,2,9,12,32,33,67,68,69,36,70,74,75,71,76,38,72,80,81,82,73,66,40,39,79,78,77,37,29,30,35,31,13,10,3,8,34,7,11,14,15,6,5,18,25,65,64,41,63,83,84,85,60,59,56,55,54,50,51,53,49,48,47,46,45,44,52,57,58,61,62,43,42,22,23,24,21,20,19,26,17,16,27,28,4]
print('jumlah : ', len(weight))

print(len(ori), len(uji))

ekstrak = []
for i in range (len(x)):
    nomor  = an_urut[i]
    simpan = anotasi.index(nomor) 
    ekstrak.append(simpan)
print(ekstrak)

ekstrak_weight = []
for i in range (len(weight)):
    ambilindex = weight[i]
    dapatisi = anotasi[ambilindex]
    ekstrak_weight.append(dapatisi)
print('hasil ekstrak :: ' ,ekstrak_weight)




'''--------------------------------'''



#cek duplikat
arr = [80,72,38,28,15,4,0,1,7,10,13,34,31,35,30,14,70,74,75,71,77,76,78,79,66,65,64,43,44,52,53,54,55,56,59,60,85,84,83,82,36,69,68,67,33,32,12,9,2,3,8,11,29,37,27,47,48,49,50,51,57,58,61,62,63,41,42,45,46,22,23,24,21,19,18,5,6,16,17,26,39,20,25,40,73,81];     
     
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);    
