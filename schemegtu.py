from fuel import *

def data_1(array , method = True):
    if method == 'compressor':
        data_1 = {'Газовая постоянная воздуха':'кДж/(кгК)',
                  'Температура на входе в компрессор': '℃', 
                  'Давление на входе в компрессор': 'Па',
                  'Энтальпия вохдуха на входе в компрессор': 'кДж/кг',
                  'Энтропия вохдуха на входе в компрессор': 'кДж/(кгК)',
                  'Теоретическая температура воздуха на выходе из компрессора': '℃',
                  'Теоретическая энтальпия на выходе из компрессора': 'кДж/кг',
                  'Теоретическая энтропия на выходе из компрессора': 'кДж/(кгК)',
                  'Действительная температура воздуха на выходе из компрессора': '℃',
                  'Давление на выходе из компрессора': 'Па',
                  'Действительная энтальпия воздуха на выходе из компрессора': 'кДж/кг',
                  'Действительная энтропия воздуха на выходе из компрессора': 'кДж/(кгК)',
                  'Степень сжатия в компрессоре': '-',
                  'Изоэнтропийный теплоперепад в компрессоре': 'кДж/кг',
                  'Действительный теплоперепад в компрессоре': 'кДж/кг',
                  'КПД компрессора': '-'}
        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    if method == 'turbine':
        data_1 = {'Коэф. избытка воздуха': '-',
                  'Газовая постоянная продуктов сгорания':'кДж/(кгК)',
                  'Температура на входе в турбину': '℃', 
                  'Давление на входе в турбину': 'Па',
                  'Энтальпия газов на входе в турбину': 'кДж/кг',
                  'Энтропия газов на входе в турбину': 'кДж/(кгК)',
                  'Теоретическая температура газов на выходе из турбины': '℃',
                  'Теоретическая энтальпия на выходе из турбины': 'кДж/кг',
                  'Теоретическая энтропия на выходе из турбины': 'кДж/(кгК)',
                  'Действительная температура газов на выходе из турбины': '℃',
                  'Давление на выходе из турбины': 'Па',
                  'Действительная энтальпия газов на выходе из турбины': 'кДж/кг',
                  'Действительная энтропия газов на выходе из турбины': 'кДж/(кгК)',
                  'Степень расширения в турбине': '-',
                  'Изоэнтропийный теплоперепад в турбине': 'кДж/кг',
                  'Действительный теплоперепад в турбине': 'кДж/кг',
                  'КПД турбины': '-'}
        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    if method == 'scheme':
        data_1 = {'Расход воздуха через компрессор': 'кг/c',
                  'Расход газов через турбину':'кг/c',
                  'Расход топлива':'кг/c',
                  'Удельная работа ГТУ на валу турбоагрегата':'кДж/(кг)',
                  'Электрическая мощность ГТУ':'Вт',
                  'Мощность компрессора':'Вт',
                  'Мощность турбины':'Вт',
                  'Электрический КПД ГТУ':'-',
                  'Коэффициент использования теплоты топлива':'-',
                  'Механический КПД турбины':'-',
                  'КПД электрического генератора':'-',
                  'Коэффициент полезной работы':'-',
                  'Коэффициент потерь давления':'-',
                  'Коэффициент утечек':'-'}
        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    if method == 'schemecool':
        data_1 = {'Расход воздуха на входе в компрессор охлаждаемой ГТУ': 'кг/c',
                  'Расход газов на выходе из турбины охлаждаемой ГТУ':'кг/c',
                  'Расход воздуха на входе в камеру сгорания охлаждаемой ГТУ':'кг/c',
                  'Расход топлива':'кг/c',
                  'Относительный расход воздуха на охлаждение': '-',
                  'Внутренняя работа ГТУ с охлаждаемой турбиной': 'кДж/(кг)',
                  'Электрическая мощность ГТУ':'Вт',
                  'Мощность компрессора охлаждаемой ГТУ':'Вт',
                  'Мощность турбины охлаждаемой ГТУ':'Вт',
                  'Электрический КПД охлаждаемой ГТУ':'-',
                  'Коэффициент использования теплоты топлива':'-',
                  'Механический КПД охлаждаемой турбины':'-',
                  'КПД электрического генератора':'-',
                  'Коэффициент полезной работы охлаждаемой ГТУ':'-',
                  'Коэффициент потерь давления':'-',
                  'Коэффициент утечек':'-'
                  }
        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    return df_merged

def BraitonPlot(point_a, point_b_ =0, point_b =0, point_c =0, point_d_=0, point_d=0):
    plt.style.use('seaborn-ticks') # задание стиля окна
    fig = plt.figure(figsize=(15,10)) # параметры окна
    ax = plt.axes()

    ax.yaxis.set_major_locator(LinearLocator(15)) # разбиение оси
    ax.xaxis.set_major_locator(LinearLocator(15))

    ha, hb, hb_, hc, hd, hd_ = point_a['h_a'], point_b['h_b'], point_b_['h_b_'],point_c['h_c'], point_d['h_d'], point_d_['h_d_']
    ta, tb, tb_, tc, td, td_  = point_a['t_a'], point_b['t_b'], point_b_['t_b_'], point_c['t_c'], point_d['t_d'], point_d_['t_d_']
    Pa, Pb = point_a['P_a'], point_b['P_b']

    plt.tick_params(axis='both', which='major', labelsize=15, 
                    direction = 'inout', length=10, pad = 15) # настройка обозначений значений
    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'major', color = '#aaa', linewidth = 0.8) # настройка сетки
    plt.grid (which = 'minor', color = '#aaa', ls = ':')

    fig.suptitle('Цикл Брайтона для простой схемы ГТУ', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
    plt.xlabel('S, кДж/(кгК)', fontsize=20, loc = 'center')
    plt.ylabel('h, кДж/кг',fontsize=20,loc = 'center')

    x_1 = np.array([point_b_['S_b_'], point_b['S_b'], point_c['S_c']])
    y_1 = np.array([point_b_['h_b_'], point_b['h_b'], point_c['h_c']])
    xnew_1 = np.linspace (x_1. min (), x_1. max (), 100 )
    spl_1 = make_interp_spline (x_1, y_1, k= 2 )
    y_smooth_1 = spl_1(xnew_1)
 
    x_2 = np.array([point_a['S_a'], point_d_['S_d_'], point_d['S_d']])
    y_2 = np.array([point_a['h_a'], point_d_['h_d_'], point_d['h_d']])
    xnew_2 = np.linspace(x_2. min (), x_2. max (), 300 )
    spl_2 = make_interp_spline (x_2, y_2, k= 2 )
    y_smooth_2 = spl_2(xnew_2)

    Hk, = plt.plot([point_a['S_a'], point_b_['S_b_']], [point_a['h_a'], point_b_['h_b_']], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')  
    Ht, = plt.plot([point_c['S_c'], point_d_['S_d_']], [point_c['h_c'], point_d_['h_d_']], color='r',marker='o',ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')  
    Hk_, = plt.plot([point_a['S_a'], point_b['S_b']], [point_a['h_a'], point_b['h_b']], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=2, linestyle='--')
    Ht_, = plt.plot([point_c['S_c'], point_d['S_d']], [point_c['h_c'], point_d['h_d']], color='r',marker='o',ms = 8, markerfacecolor='w',linewidth=2, linestyle='--')
    
    plt.plot (xnew_1, y_smooth_1, color='r',linewidth=3, linestyle='-')
    plt.plot (xnew_2, y_smooth_2, color='b',linewidth=3, linestyle='-')

    plt.annotate(f'$T_a = {round((ta+273.15),2)} К$', xy=(point_a['S_a'], point_a['h_a']), xytext=(point_a['S_a'] - 0.005, point_a['h_a']- 40), fontsize = 15)
    plt.annotate(f'$T_b^\prime = {round((tb+273.15),2)} К$', xy=(point_b['S_b'], point_b['h_b']), xytext=(point_b['S_b'] + 0.0001, point_b['h_b']- 40), fontsize = 15)
    plt.annotate(f'$T_b = {round((tb_+273.15),2)} К$', xy=(point_b_['S_b_'], point_b_['h_b_']), xytext=(point_b_['S_b_'] - 0.005, point_b_['h_b_']+ 25), fontsize = 15)
    
    plt.annotate(f'$T_c = {round((tc+273.15),2)} К$', xy=(point_c['S_c'], point_c['h_c']), xytext=(point_c['S_c'] - 0.025, point_c['h_c']+ 25), fontsize = 15)
    plt.annotate(f'$T_d^\prime = {round((td+273.15),2)} К$', xy=(point_d['S_d'], point_d['h_d']), xytext=(point_d['S_d'] - 0.025, point_d['h_d'] - 60), fontsize = 15)
    plt.annotate(f'$T_d = {round((td_+273.15),2)} К$', xy=(point_d_['S_d_'], point_d_['h_d_']), xytext=(point_d_['S_d_'] - 0.025, point_d_['h_d_'] - 70), fontsize = 15)
    
    ax.legend((Hk, Hk_, Ht, Ht_, Hk, Ht), [r'$H_к(теорет.) = ' f'{round((hb_ - ha), 2)} ' ' кДж/кг$', 
                                   r'$H_к(действит.) = ' f'{round((hb - ha), 2)} ' ' кДж/кг$',
                                   r'$H_т(теорет.) = ' f'{round((hc - hd_), 2)} ' ' кДж/кг$',
                                   r'$H_т(действит.) = ' f'{round((hc - hd), 2)} ' ' кДж/кг$',
                                   r'$P_a = P_d= ' f'{round(Pa/10e2, 2)} ' ' кПа$',
                                   r'$P_b = P_c= ' f'{round(Pb/10e2, 3)} ' ' кПа$'],
                                    fontsize = 15, frameon=True, framealpha=True)
    
    plt.show()

@st.cache
def compressor(t_a, P_a, epsilon, etta_is_k):
    h_a = interpolate(air.get('h'),air.get('temperature_C'), t_a)
    S_a = interpolate(air.get('s_0'),air.get('temperature_C'), t_a)
    S_b_ = S_a + air.get('R')*log(epsilon)
    t_b_ = interpolate(air.get('temperature_C'),air.get('s_0'), S_b_)
    h_b_ = interpolate(air.get('h'),air.get('temperature_C'), t_b_)
    Hk_0_iz = h_b_ - h_a
    h_b = (h_a + (Hk_0_iz / etta_is_k))
    t_b = interpolate(air.get('temperature_C'),air.get('h'), h_b)
    S_b = interpolate(air.get('s_0'),air.get('temperature_C'), t_b)
    H_k = (h_b - h_a) 
    P_b = P_a * epsilon

    return {'R_v':air.get('R'),'t_a':t_a, 'P_a':P_a, 'h_a':h_a, 'S_a':S_b_, 
            't_b_':t_b_, 'h_b_':h_b_, 'S_b_':S_b_,
            't_b':t_b, 'P_b':P_b, 'h_b':h_b, 'S_b':S_b, 
            'epsilon':epsilon, 'Hk_0_iz':Hk_0_iz, 'H_k':H_k, 'etta_is_k':etta_is_k}

@st.cache
def turbine(fuel, t_c, epsilon, etta_c_c, etta_is_t, coefficient_pressure_loss, h_b, P_b):
    sigmma = coefficient_pressure_loss * epsilon
    h_air = interpolate(air.get('h'), air.get('temperature_C'), t_c)
    h_ccp = interpolate(fuel.get('h'), fuel.get('temperature_C'), t_c)
    excess_air_ratio_in_flue_gases = (fuel.get('heat_of_combustion') * etta_c_c + fuel.get('stoichiometric_air_flow') * h_air - ( 1 + fuel.get('stoichiometric_air_flow')) *h_ccp) / (fuel.get('stoichiometric_air_flow') * (h_air - h_b))
    g_products_of_combustion = (1 + fuel.get('stoichiometric_air_flow')) / (1 + fuel.get('stoichiometric_air_flow') * excess_air_ratio_in_flue_gases)    
    g_air = 1 - g_products_of_combustion
    h_c = g_products_of_combustion * h_ccp + g_air * h_air
    S_c = g_products_of_combustion * interpolate(fuel.get('s_0'), fuel.get('temperature_C'), t_c) + g_air * interpolate(air.get('s_0'), air.get('temperature_C'), t_c)
    q = (fuel.get('mu') * fuel.get('stoichiometric_air_flow')) / (air.get('mu') * (1 + fuel.get('stoichiometric_air_flow')))
    r_air = q * (excess_air_ratio_in_flue_gases - 1) / (1 + q * (excess_air_ratio_in_flue_gases - 1))
    mu_ccp = air.get('mu') * r_air + fuel.get('mu') * (1 - r_air)
    R_g = 8.314 / mu_ccp
    S_d_ = S_c - R_g * log(sigmma)
    
    s = [g_products_of_combustion * fuel.get('s_0')[i] + g_air * air.get('s_0')[i] for i in range(len(air.get('temperature_C')))]
    entropy_, residuals, rank, sv, rcond = np.polyfit(s, air.get('temperature_C') , 7, full = True)
    t = sp.poly1d(entropy_)
    t_d_ = t(S_d_)

    h = [g_products_of_combustion * fuel.get('h')[i] + g_air * air.get('h')[i] for i in range(len(air.get('temperature_C')))]
    temperature_, residuals, rank, sv, rcond = np.polyfit(air.get('temperature_C'), h, 7, full=True)
    enthalpy = sp.poly1d(temperature_)
    enthalpy_, residuals, rank, sv, rcond = np.polyfit(h, air.get('temperature_C'), 7, full=True)
    temperature = sp.poly1d(enthalpy_)
    h_d_ = enthalpy(t_d_)

    Ht_0_iz = (h_c - h_d_)
    h_d = (h_c -(Ht_0_iz * etta_is_t))
    t_d = temperature(h_d)
    S_d = g_products_of_combustion * interpolate(fuel.get('s_0'), fuel.get('temperature_C'), t_d) + g_air * interpolate(air.get('s_0'), air.get('temperature_C'), t_d)
    q = (fuel.get('mu') * fuel.get('stoichiometric_air_flow')) / (air.get('mu') * (1 + fuel.get('stoichiometric_air_flow')))
    H_t = (Ht_0_iz * etta_is_t)
    P_c = P_b
    P_d = P_c / sigmma

    return {'excess_air_ratio_in_flue_gases':excess_air_ratio_in_flue_gases,'R_g':R_g,
            't_c':t_c, 'P_c':P_c, 'h_c':h_c, 'S_c':S_d_,
            't_d_':t_d_, 'h_d_':h_d_, 'S_d_':S_d_,
            't_d':t_d, 'P_d':P_d, 'h_d': h_d, 'S_d':S_d,
             'sigmma':sigmma,'Ht_0_iz':Ht_0_iz, 'H_t':H_t, 'etta_is_t':etta_is_t, 
             }

@st.cache
def scheme(fuel, ele_power, t_c, t_a, P_a, epsilon, coefficient_pressure_loss, 
           etta_c_c, etta_mch, etta_e_g, etta_is_t, etta_is_k, leak_rate, t_w = None,z = None, method = 'notcold'):
    c = compressor(t_a, P_a, epsilon, etta_is_k)
    t = turbine(fuel, t_c, epsilon, etta_c_c, etta_is_t,coefficient_pressure_loss, h_b = c.get('h_b'), P_b = c.get('P_b'))
    b = (t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow') * (1 + leak_rate)) / (1 + t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow'))
    H_e = (t['H_t'] * etta_mch - b * c['H_k'])
    G_t = ele_power / (H_e * etta_e_g * 10e2)
    G_k = (G_t * b)
    fuel_consumption = (G_t / (1 + t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow')))
    N_t = (G_t * t['H_t']) * 10e2
    N_k = (G_k * c['H_k']) * 10e2
    efficiency_factor = ((N_t - N_k) / N_t)
    etta_ele = (G_t * H_e * etta_e_g) / (fuel_consumption * fuel.get('heat_of_combustion'))

    point_a = {'t_a':t_a, 'P_a':c['P_a'], 'h_a':c['h_a'], 'S_a':c['S_a']}
    point_b_ = {'t_b_':c['t_b_'], 'P_b':c['P_b'], 'h_b_':c['h_b_'], 'S_b_':c['S_b_']}
    point_b = {'t_b':c['t_b'], 'P_b':c['P_b'], 'h_b':c['h_b'], 'S_b':c['S_b']}

    point_c = {'t_c':t['t_c'], 'P_c':t['P_c'], 'h_c':t['h_c'], 'S_c':t['S_c']}
    point_d_ = {'t_d_':t['t_d_'], 'P_d':t['P_d'], 'h_d_':t['h_d_'], 'S_d_':t['S_d_']}
    point_d = {'t_d':t['t_d'], 'P_d':t['P_d'], 'h_d':t['h_d'], 'S_d':t['S_d']}

    if method == 'notcold':
        sc = {'G_k':G_k, 'G_t':G_t, 'fuel_consumption':fuel_consumption, 'H_e':H_e,
            'N_e':ele_power, 'N_k':N_k, 'N_t':N_t, 'etta_ele':etta_ele,'etta_c_c':etta_c_c, 
            'etta_mch':etta_mch, 'etta_e_g':etta_e_g, 'efficiency_factor':efficiency_factor,
            'coefficient_pressure_loss':coefficient_pressure_loss, 'leak_rate':leak_rate}
        
        return c, t, sc, point_a, point_b_, point_b, point_c, point_d_, point_d
    
    if method == 'cold':
        g_air = 0.02 + (0.32 * 10**(-3)) * (t['t_c'] - t_w)
        T_2_cool = (t['t_c']+ 273.15) - ((1 / z)* (t['H_t']/(t['h_c']/t['t_c']))) - 273.15
        gamma = ((1 - efficiency_factor)/ efficiency_factor) - ((z - 1)/(z * efficiency_factor) * ((c['t_b']+ 273.15)/(T_2_cool + 273.15))) + 0.6/ (z * efficiency_factor) 
        H = t['H_t'] - b * c['H_k']
        H_cool = H * (1 - gamma * g_air)
        etta_mch_ = 1 - ((1 - etta_mch) / efficiency_factor)
        G_t_ = ele_power / (H_cool * etta_mch_ * etta_e_g * 10e2)
        fuel_consumption_cool = (G_t_ / (1 + t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow')))
        G_c_cool = ((t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow')) / (1 + t['excess_air_ratio_in_flue_gases'] * fuel.get('stoichiometric_air_flow'))) * G_t_
        G_k_cool = G_t_ * (b + g_air)
        G_t_cool = G_t_ * (1 + g_air)
        N_t_cool = (G_t_cool * t['H_t']) * 10e2
        N_k_cool = (G_k_cool * c['H_k']) * 10e2
        etta_ele_cool = etta_ele * (1 - gamma * g_air)
        efficiency_factor_cool = ((N_t_cool - N_k_cool) / N_t_cool)

        sc = {'G_k':G_k_cool, 'G_t':G_t_cool, 'G_c':G_c_cool, 'fuel_consumption':fuel_consumption_cool, 'g_air':g_air, 'H_cool':H_cool,
        'N_e':ele_power, 'N_k':N_k_cool, 'N_t':N_t_cool, 'etta_ele':etta_ele_cool,'etta_c_c':etta_c_c, 
        'etta_mch':etta_mch_, 'etta_e_g':etta_e_g, 'efficiency_factor':efficiency_factor_cool,
        'coefficient_pressure_loss':coefficient_pressure_loss, 'leak_rate':leak_rate}
        
        return c, t, sc, point_a, point_b_, point_b, point_c, point_d_, point_d 

    
# fuel = gas(_H_2S = 0, _CO_2 = 0.06, _O_2 = 0, _CO = 0, _H_2 = 0, _CH_2 = 0,
#         _CH_4 = 99.0, _C_2H_4 = 0, _C_2H_6 = 0.1, _C_3H_8 = 0.03,_C_4H_10 = 0.04, 
#         temperature_C = temperature_Cels)

# schemegtu = scheme(fuel = fuel, ele_power = 153*10e5, t_c = 1060,
#                                 t_a = 15, P_a = 100.5*10e2, epsilon = 10.9, coefficient_pressure_loss = 0.97,
#                                 etta_c_c = 0.995, etta_mch = 0.995, etta_e_g = 0.982,
#                                 etta_is_t = 0.89, etta_is_k = 0.87, leak_rate = 0.005, t_w = 850, z = 4, method = 'notcold')

# print(data(schemegtu[0], method = 'compressor'))
# print(data(schemegtu[1], method = 'turbine'))
# print(data(schemegtu[2], method = 'scheme'))

# BraitonPlot(point_a = schemegtu[3], point_b_ = schemegtu[4], point_b = schemegtu[5],
#             point_c = schemegtu[6], point_d_ = schemegtu[7], point_d = schemegtu[8])
