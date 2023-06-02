import scipy as sp
from math import *
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import make_interp_spline
from matplotlib.ticker import LinearLocator
from PIL import Image
import itertools
from scipy.interpolate import interp2d
from scipy.optimize import fsolve

def properties(temperature_C: list[int | float], 
               coefficient: list[int | float], 
               mu: int | float, 
               h_k: int | float, 
               s_k: int | float) -> dict[int | float]:
    
    R_const = 8.31451
    temperature_K = [round((temperature_C[i] + 273.15), 3) for i in range(len(temperature_C))]
    tau = [temperature_K[i] / 1000 for i in range(len(temperature_C))]
    R = R_const / mu
    Cp = [R * (((coefficient[0] * (tau[i])**0) + (coefficient[1] * (tau[i])**1) +
                (coefficient[2] * (tau[i])**2) + (coefficient[3] * (tau[i])**3) +
                (coefficient[4] * (tau[i])**4) + (coefficient[5] * (tau[i])**5) +
                (coefficient[6] * (tau[i])**6)) + ((coefficient[7] * (1 / tau[i])**1) +
                (coefficient[8] * (1 / tau[i])**2) + (coefficient[9] * (1 / tau[i])**3) +
                (coefficient[10] * (1 / tau[i])**4) + (coefficient[11] * (1 / tau[i])**5)+
                (coefficient[12] * (1 / tau[i])**6))) for i in range(len(tau))]

    h = [R * 1000 * ((((coefficient[0] / 1) * tau[i]**1) + ((coefficient[1] / 2) * tau[i]**2) +
                ((coefficient[2] / 3) * tau[i]**3) + ((coefficient[3] / 4) * tau[i]**4) +
                ((coefficient[4] / 5) * tau[i]**5) + ((coefficient[5] / 6) * tau[i]**6) +
                ((coefficient[6] / 7) * tau[i]**7)) + coefficient[7] * log(tau[i]) +
                (((coefficient[8] / (-1)) * (1 / tau[i])**1) + ((coefficient[9] / (-2)) * (1 / tau[i])**2) +
                ((coefficient[10] / (-3)) * (1 / tau[i])**3) + ((coefficient[11] / (-4)) * (1 / tau[i])**4) +
                ((coefficient[12] / (-5)) * (1 / tau[i])**5))) + h_k * R for i in range(len(temperature_K))]

    s_0 = [R * (coefficient[0] * log(tau[i]) + (((coefficient[1] * tau[i]**1) / 1) +
            ((coefficient[2] * tau[i]**2) / 2) + ((coefficient[3] * tau[i]**3) / 3) +
            ((coefficient[4] * tau[i]**4) / 4) + ((coefficient[5] * tau[i]**5) / 5) +
            ((coefficient[6] * tau[i]**6) / 6)) + (((coefficient[7] * (1 / tau[i])**(1)) / (-1)) +
            ((coefficient[8] * (1 / tau[i])**(2)) / (-2)) + ((coefficient[9] * (1 / tau[i])**(3)) / (-3)) + 
            ((coefficient[10] * (1 / tau[i])**(4)) / (-4)) + ((coefficient[11] * (1 / tau[i])**(5)) / (-5)) +
            ((coefficient[12] * (1 / tau[i])**(6)) / (-6)))) + s_k * R for i in range(len(temperature_K))]

    u=[h[i] - R * temperature_K[i] for i in range(len(temperature_K))]
    Cv=[Cp[i] - R for i in range(len(temperature_K))]
    k= [Cp[i] / Cv[i] for i in range(len(temperature_K))]
    return {'temperature_C': temperature_C, 'temperature_K': temperature_K, 'temperature_K': temperature_K, 'u':u, 'h':h, 's_0':s_0, 'Cp':Cp, 'Cv':Cv, 'k':k, 'R':R, 'mu':mu}

@st.cache
def gas(_H_2S: int | float,
        _CO_2: int | float,
        _O_2: int | float,
        _CO: int | float,
        _H_2: int | float,
        _CH_2: int | float,
        _CH_4: int | float,
        _C_2H_4: int | float,
        _C_2H_6: int | float,
        _C_3H_8: int | float,
        _C_4H_10: int | float, temperature_C:list[int | float]) -> dict[int | float]:
        
        _N_2_atm = 100-_H_2S - _CO_2 - _O_2 - _CO - _H_2 - _CH_2 - _CH_4 - _C_2H_4 - _C_2H_6 - _C_3H_8 - _C_4H_10
        temperature_K = [round((temperature_C[i]+273.15),3) for i in range(len(temperature_C))]
        R_const = 8.31451
        excess_air_ratio_in_flue_gases = 1
        d_t = 47.5
        d_air = 8

        heat_of_combustion = 358.2 * _CH_4 + 637.46 * _C_2H_6 + 860.05 * _C_3H_8 + 107.98 * _H_2 + 126.36 * _CO
        stoichiometric_air_flow = ((1 / 21) * (0.5 * _H_2 + 0.5 * _CO + 2 * _CH_2 + 2 * _CH_4 + 3.5 * _C_2H_6 + 5 * _C_3H_8 + 6.5 * _C_4H_10 + 1.5 * _H_2S - _O_2))
        theoretical_volumes_ro_2 = 0.01 * (_CO_2 + _CO + _H_2S + _CH_4 + _CH_2 + 2 * _C_2H_6 + 3 * _C_3H_8 + 4 * _C_4H_10)
        theoretical_volumes_h20 = 0.01 * (_H_2 + 2 * _CH_2 + 2 * _C_2H_4 + _H_2S + 3 * _C_2H_6 + 4 * _C_3H_8 + 5 * _C_4H_10 + 0.124 * (d_t + excess_air_ratio_in_flue_gases * stoichiometric_air_flow * d_air))
        theoretical_volumes_N_2 = 0.79 * stoichiometric_air_flow + 0.01 * _N_2_atm
        full_volumes = theoretical_volumes_ro_2 + theoretical_volumes_N_2 + theoretical_volumes_h20
        r_ro_2 = (theoretical_volumes_ro_2 / full_volumes)
        r_h20 = (theoretical_volumes_h20 / full_volumes)
        r_N_2 = (theoretical_volumes_N_2 / full_volumes)
        
        enthalpy_CO2 = CO_2.get('h')
        enthalpy_H20 = H2O.get('h')
        enthalpy_N2 = N_2_atm.get('h')
        h = [(r_ro_2 * enthalpy_CO2[i] + r_h20 * enthalpy_H20[i] + r_N_2 * enthalpy_N2[i]) for i in range(len(temperature_C))]
       
        heat_capacity_CO2 = CO_2.get('Cp')
        heat_capacity_N2 = N_2_atm.get('Cp')
        heat_capacity_H20 = H2O.get('Cp')
        Cp = [r_ro_2 * heat_capacity_CO2[i] + r_h20 * heat_capacity_H20[i] + r_N_2 * heat_capacity_N2[i] for i in range(len(temperature_C))]
        
        entropy_CO2 = CO_2.get('s_0')
        entropy_N2 = N_2_atm.get('s_0')
        entropy_H20 = H2O.get('s_0')
        s_0 = [r_ro_2 * entropy_CO2[i] + r_h20 * entropy_H20[i] + r_N_2 * entropy_N2[i] for i in range(len(temperature_C))] 

        mu = (mu_CO_2 * r_ro_2 + mu_H2O * r_h20 + mu_N_2_atm * r_N_2)
        R = R_const / mu
        u = [h[i] - R * temperature_K[i] for i in range(len(temperature_K))]
        Cv = [Cp[i] - R for i in range(len(temperature_K))]
        k = [Cp[i] / Cv[i] for i in range(len(temperature_K))]

        return {'temperature_C':temperature_C, 'temperature_K':temperature_K, 'temperature_K':temperature_K, 
                'u':u, 'h':h, 's_0':s_0, 'Cp':Cp, 'Cv':Cv, 'k':k, 'R':R, 'mu':mu,
                'heat_of_combustion':heat_of_combustion,
                'stoichiometric_air_flow':stoichiometric_air_flow}

def table(temperature_C: list[int | float], 
          temperature_K: list[int | float], 
          u: list[int | float], h: list[int | float], 
          s_0: list[int | float], 
          Cp: list[int | float], 
          Cv: list[int | float], 
          k: list[int | float]):  
     
    data = pd.DataFrame({ 't':pd.Series(np.round((temperature_C),2),index=range(1,len(temperature_C)+1,1)),
                              'T':pd.Series(np.round((temperature_K),2),index=range(1,len(temperature_K)+1,1)),
                              'u':pd.Series(np.round((u),1),index=range(1,len(u)+1,1)),
                              'h':pd.Series(np.round((h),1),index=range(1,len(h)+1,1)),
                              's°':pd.Series(np.round((s_0),3),index=range(1,len(s_0)+1,1)),
                            # #   'lg(pi_0)':pd.Series(self.lg_Pi,index=range(1,len(self.lg_Pi)+1,1)),
                            # #   'pi_0':pd.Series(self._Pi,index=range(1,len(self._Pi)+1,1)),
                              'C_p':pd.Series(np.round((Cp),4),index=range(1,len(Cp)+1,1)),
                              'C_v':pd.Series(np.round((Cv),4),index=range(1,len(Cv)+1,1)),
                              'k':pd.Series(np.round((k),4),index=range(1,len(k)+1,1))},
                            columns=['t','T','u','h','s°','C_p','C_v','k'])
    return data

def interpolate(function: list[int | float], 
                parametr: list[int | float], 
                x: int | float) -> int | float:
    
    parametr, residuals, rank, sv, rcond = np.polyfit(parametr, function, 18, full=True)
    function = sp.poly1d(parametr)
    return function(x)

def visual_table(x, y, name_X, name_Y):
    plt.style.use('seaborn-whitegrid') 
    fig= plt.figure()
    ax=plt.axes()     
    for i in range(len(x)): 
        plt.plot(x, y, color='#1f77b4',marker='o',linestyle='-',label=r'$h$')  
        plt.xlabel(f'{name_X}', fontsize=40)
        plt.ylabel(f'{name_Y}',fontsize=40)
        mpl.rcParams['font.size'] = 14
        fig.set_figwidth(15)
        fig.set_figheight(10)
        plt.tick_params(axis='both', which='major', labelsize=30)
        plt.show()

# temperature_Cels = np.linspace(-70,2180,9004)
temperature_Cels = np.linspace(-70,2180,50)

coefficient_N_2 = [-9.2984251, 20.007476, -16.763488, 8.6903787, -2.7510686, 0.48793873, -0.037167758, 4.0387289, -0.30781129, -0.19090602, 0.06465393, -0.0082736889, 0.00039772373]
mu_N_2 = 28.01314
h_N_2 = 0.6424442807318471 * 10**4
s_N_2 = 0.1735176521821870 * 10**2

coefficient_O_2 = [17.190127, -11.550976, 7.005699600000001, -2.8621429, 0.79318027, -0.13392554, 0.010209171999999999, -8.967597000000001, 3.3796419, -0.76513147, 0.10340806, -0.0077090528, 0.00024408174]
mu_O_2 = 31.9988
h_O_2 = -0.6367575813150352 * 10**4
s_O_2 = 0.3061627323177847 * 10**2

coefficient_C_O = [5.8627934, 3.4431821, -4.8382992, 3.0512615, -1.065302, 0.1992689, -0.015612248, -4.8401749, 3.0051631, -0.97260373, 0.17723571, -0.017272462, 0.00070218924] 
mu_C_O = 28.0104
h_C_O = -0.3273548397297125 * 10**3
s_C_O = 0.2277544216280227 * 10**2

coefficient_CO_2 = [ -1.8188731, 12.903022, -9.6634864, 4.2251879, -1.042164, 0.12683515, -0.0049939675, 2.4950242, -0.8272375, 0.15372481, -0.015861243, 0.0008601715, -0.19222165*10**(-4)]
mu_CO_2 = 44.0098
h_CO_2 = 0.2108207002517842 * 10**4
s_CO_2 = 0.2527352695389967 * 10**2

coefficient_H2O = [ 31.040960123603497, -39.1422080460869, 37.9695277233575, -21.837491095228398, 7.42251494566339, -1.3817892960947, 0.108807067571454, -12.0771176848589, 3.39105078851732, -0.5845209799550599, 0.058993084648808196, -0.00312970001415882, 6.57460740981757e-05]
mu_H2O = 18.0152
h_H2O = -0.1249994285621061 * 10**5
s_H2O = 0.4326899518164680 * 10**2

coefficient_SO2 = [ 12.9839174, -7.097552299999999, 5.4433743, -2.6855652, 0.83220003, -0.14690738, 0.011260596000000001, -2.8695081, -0.21889887, 0.35974571, -0.092149906, 0.0099973132, -0.00039568472]
mu_SO2 = 64.059
h_SO2 = -0.5389772534731859 * 10**4
s_SO2 = 0.3897098691715381 * 10**2

coefficient_air = [-3.62171168554944, 13.1878685737717, -11.61002657829, 6.1800155085671, -1.97996023924462, 0.352570060264284, -0.026853107411115, 1.26880226994069, 0.46926061357441606, -0.309569582156729, 0.072153490824886, -0.00807371553566351, 0.00036155006617758797]
mu_air = 28.96431986
h_air = 0.3675992368817275*10**4
s_air = 0.2074880396190873*10**2

coefficient_N_2_atm = [-9.15141475338944, 19.7612585131717, -16.55656033537, 8.5827173265771, -2.71684951509762, 0.481843413354284, -0.0367013882440646, 3.98857888363069, -0.304018225402584, -0.188527932068729, 0.063849312595586, -0.00817063504476351, 0.000392763515964088]
mu_N_2_atm = 28.15922054
h_N_2_atm = 0.6344544217996919 * 10**4
s_N_2_atm = 0.1747674345446363 * 10**2

coefficient_NO = [17.512975, -10.232606, 5.309077, -1.756358, 0.34469268, -0.033561691, 0.0009074848199999999, -10.716017, 4.7147653, -1.2288023, 0.18787565, -0.015404103999999998, 0.00051348154]
mu_NO = 30.0061
h_NO = -0.5853505325108175 * 10**4
s_NO = 0.2925094859807305 * 10**2

coefficient_NO_2 = [22.897799, -15.733398000000001, 10.595965999999999, -4.722968, 1.3348353, -0.21315607, 0.014608561, -10.408705, 3.0661019, -0.49285332, 0.037617693, -0.0005705258, -4.6213031e-05]
mu_NO_2 = 46.0055
h_NO_2 = -0.9618276388197241 * 10**4
s_NO_2 = 0.3812145868004694 * 10**2

coefficient_H_2 = [26.8742461056112, -32.8599322826549, 29.2580798999686, -15.90752702904, 5.22699862384258, -0.9561045371638819, 0.0748714373539927, -10.677876893089898, 3.07099601416186, -0.506366407292404, 0.0343582478595844, 0.00116044276488724, -0.000207509179117432]
mu_H_2 = 2.0158
h_H_2 = -0.1078168899791991*10**5 
s_H_2 = 0.3309399567910378*10**2

coefficient_Ar = [ 2.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mu_Ar = 39.948
h_Ar = -0.5146319506491182*10**(-1)
s_Ar = 0.2164843538294026*10**2

coefficient_Ne=[2.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mu_Ne=20.179
h_Ne=-0.5146319506491182*10**(-1) 
s_Ne=0.2062396130088371*10**2

N_2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_N_2, mu = mu_N_2, h_k = h_N_2, s_k = s_N_2)
O_2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_O_2, mu = mu_O_2, h_k = h_O_2, s_k = s_O_2)
C_O = properties(temperature_C = temperature_Cels, coefficient = coefficient_C_O, mu = mu_C_O, h_k = h_C_O, s_k = s_C_O)
CO_2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_CO_2, mu = mu_CO_2, h_k = h_CO_2, s_k = s_CO_2)
H2O = properties(temperature_C = temperature_Cels, coefficient = coefficient_H2O, mu = mu_H2O, h_k = h_H2O, s_k = s_H2O)
SO2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_SO2, mu = mu_SO2, h_k = h_SO2, s_k = s_SO2)
air = properties(temperature_C = temperature_Cels, coefficient = coefficient_air, mu = mu_air, h_k = h_air, s_k = s_air)
N_2_atm = properties(temperature_C = temperature_Cels, coefficient = coefficient_N_2_atm, mu = mu_N_2_atm, h_k = h_N_2_atm, s_k = s_N_2_atm)
NO = properties(temperature_C = temperature_Cels, coefficient = coefficient_NO, mu = mu_NO, h_k = h_NO, s_k = s_NO)
NO_2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_NO_2, mu = mu_NO_2, h_k = h_NO_2, s_k = s_NO_2)
H_2 = properties(temperature_C = temperature_Cels, coefficient = coefficient_H_2, mu = mu_H_2, h_k = h_H_2, s_k = s_H_2)
Ar = properties(temperature_C = temperature_Cels, coefficient = coefficient_Ar, mu = mu_Ar, h_k = h_Ar, s_k = s_Ar)
Ne = properties(temperature_C = temperature_Cels, coefficient = coefficient_Ne, mu = mu_Ne, h_k = h_Ne, s_k = s_Ne)

# fuel = gas(_H_2S = 0, _CO_2 = 0.06, _O_2 = 0, _CO = 0, _H_2 = 0, _CH_2 = 0,
#         _CH_4 = 99.0, _C_2H_4 = 0, _C_2H_6 = 0.1, _C_3H_8 = 0.03,_C_4H_10 = 0.04, 
#         temperature_C = temperature_Cels)

# print(fuel)

# print(interpolate(fuel.get('Cp'),fuel.get('temperature_C'), 1060))


# N_2_table = table(temperature_C = N_2.get('temperature_C'), temperature_K = N_2.get('temperature_K'),
#                   u = N_2.get('u'), h = N_2.get('h'), 
#                   s_0 = N_2.get('s_0'), Cp = N_2.get('Cp'), 
#                   Cv = N_2.get('Cv'), k = N_2.get('k'))

# O_2_table = table(temperature_C = O_2.get('temperature_C'), temperature_K = O_2.get('temperature_K'),
#                   u = O_2.get('u'), h = O_2.get('h'), 
#                   s_0 = O_2.get('s_0'), Cp = O_2.get('Cp'), 
#                   Cv = O_2.get('Cv'), k = O_2.get('k'))

# C_O_table = table(temperature_C = C_O.get('temperature_C'), temperature_K = C_O.get('temperature_K'),
#                   u = C_O.get('u'), h = C_O.get('h'), 
#                   s_0 = C_O.get('s_0'), Cp = C_O.get('Cp'), 
#                   Cv = C_O.get('Cv'), k = C_O.get('k'))

# CO_2_table = table(temperature_C = CO_2.get('temperature_C'), temperature_K = CO_2.get('temperature_K'),
#                   u = CO_2.get('u'), h = CO_2.get('h'), 
#                   s_0 = CO_2.get('s_0'), Cp = CO_2.get('Cp'), 
#                   Cv = CO_2.get('Cv'), k = CO_2.get('k'))

# H2O_table = table(temperature_C = H2O.get('temperature_C'), temperature_K = H2O.get('temperature_K'),
#                   u = H2O.get('u'), h = H2O.get('h'), 
#                   s_0 = H2O.get('s_0'), Cp = H2O.get('Cp'), 
#                   Cv = H2O.get('Cv'), k = H2O.get('k'))

# SO2_table = table(temperature_C = SO2.get('temperature_C'), temperature_K = SO2.get('temperature_K'),
#                   u = SO2.get('u'), h = SO2.get('h'), 
#                   s_0 = SO2.get('s_0'), Cp = SO2.get('Cp'), 
#                   Cv = SO2.get('Cv'), k = SO2.get('k'))

# air_table = table(temperature_C = air.get('temperature_C'), temperature_K = air.get('temperature_K'),
#                   u = air.get('u'), h = air.get('h'), 
#                   s_0 = air.get('s_0'), Cp = air.get('Cp'), 
#                   Cv = air.get('Cv'), k = air.get('k'))

# N_2_atm_table = table(temperature_C = N_2_atm.get('temperature_C'), temperature_K = N_2_atm.get('temperature_K'),
#                   u = N_2_atm.get('u'), h = N_2_atm.get('h'), 
#                   s_0 = N_2_atm.get('s_0'), Cp = N_2_atm.get('Cp'), 
#                   Cv = N_2_atm.get('Cv'), k = N_2_atm.get('k'))

# NO_table = table(temperature_C = NO.get('temperature_C'), temperature_K = NO.get('temperature_K'),
#                   u = NO.get('u'), h = NO.get('h'), 
#                   s_0 = NO.get('s_0'), Cp = NO.get('Cp'), 
#                   Cv = NO.get('Cv'), k = NO.get('k'))

# NO_2_table = table(temperature_C = NO_2.get('temperature_C'), temperature_K = NO_2.get('temperature_K'),
#                   u = NO_2.get('u'), h = NO_2.get('h'), 
#                   s_0 = NO_2.get('s_0'), Cp = NO_2.get('Cp'), 
#                   Cv = NO_2.get('Cv'), k = NO_2.get('k'))

# H_2_table = table(temperature_C = H_2.get('temperature_C'), temperature_K = H_2.get('temperature_K'),
#                   u = H_2.get('u'), h = H_2.get('h'), 
#                   s_0 = H_2.get('s_0'), Cp = H_2.get('Cp'), 
#                   Cv = H_2.get('Cv'), k = H_2.get('k'))

# Ar_table = table(temperature_C = Ar.get('temperature_C'), temperature_K = Ar.get('temperature_K'),
#                   u = Ar.get('u'), h = Ar.get('h'), 
#                   s_0 = Ar.get('s_0'), Cp = Ar.get('Cp'), 
#                   Cv = Ar.get('Cv'), k = Ar.get('k'))

# Ne_table = table(temperature_C = Ne.get('temperature_C'), temperature_K = Ne.get('temperature_K'),
#                   u = Ne.get('u'), h = Ne.get('h'), 
#                   s_0 = Ne.get('s_0'), Cp = Ne.get('Cp'), 
#                   Cv = Ne.get('Cv'), k = Ne.get('k'))

# fuel_table = table(temperature_C = fuel.get('temperature_C'), temperature_K = fuel.get('temperature_K'),
#                   u = fuel.get('u'), h = fuel.get('h'), 
#                   s_0 = fuel.get('s_0'), Cp = fuel.get('Cp'), 
#                   Cv = fuel.get('Cv'), k = fuel.get('k'))

# print(N_2_table)
# print(O_2_table)
# print(C_O_table)
# print(CO_2_table)
# print(H2O_table)
# print(SO2_table)
# print(air_table)
# print(N_2_atm_table)
# print(NO_table)
# print(NO_2_table)
# print(H_2_table)
# print(Ar_table)
# print(Ne_table)
# print(fuel_table)