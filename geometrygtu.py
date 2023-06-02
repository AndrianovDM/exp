from schemegtu import *

def data_2(array , method = True):
    if method == 'inlet':
        data_1 = {'Колличество ступеней в турбине':'-',
                  'Окружная скорость на входе в турбину':'м/c',
                  'Окружная скорость на выходе из турбины':'м/c',
                  'Относительная высота лопатки последней ступени':'-',
                  'Коэффициент зазора для сопловой решетки':'-',
                  'Коэффициент зазора для рабочей решетки':'-',
                  'Радиальный зазора для ступени':'м'}
        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    if method == 'geometry':
        data_1 = {'Приведенная скорость потока на входе в турбину':'-',
                'Приведенная скорость потока на выходе из турбины': '-',
                'Удельный приведенный расход на входе в турбину':'-',
                'Удельный приведенный расход на выходе из турбины':'-',
                'Кольцевая площадь на входе в турбину':'м2',
                'Кольцевая площадь на выходе из турбины':'м2',
                'Корневой диаметр на входе в турбину':'м',
                'Корневой диаметр на выходе из турбины':'м',
                'Средний диаметр на входе в турбину':'м',
                'Средний диаметр на выходе из турбины':'м',
                'Периферийный диаметр на входе в турбину':'м',
                'Периферийный диаметр на выходе из турбины':'м',
                'Высота лопаток на входе в турбину':'м',
                'Высота лопаток на выходе из турбины':'м'}

        df_merged = pd.DataFrame(list(data_1.items()),columns=['Параметры','Размерность']).join(pd.DataFrame((array.items()),columns=['Обозначение', 'Значение']), rsuffix='_right')  

    if method == 'geometrystep':

        data_1 = {'Разбивка проточной части турбины':'number_of_steps',
                  'Кольцевые площади на входе в сопловую решетку 𝑖−ой ступени':'F_1_inl_i','Кольцевые площади на выходе из сопловой решетки 𝑖−ой ступени':'F_1_out_i',
                  'Кольцевые площади на входе в рабочую решетку 𝑖−ой ступени':'F_2_inl_i','Кольцевые площади на выходе из рабочей решетки 𝑖−ой ступени':'F_2_out_i',  
                  'Корневой диаметр на входе в сопловую решетку 𝑖−ой ступени':'Dk_sopl_inl_i','Корневой диаметр на выходе из сопловой решетки 𝑖−ой ступени':'Dk_sopl_out_i',
                  'Корневой диаметр на входе в рабочую решетку 𝑖−ой ступени':'Dk_rab_inl_i','Корневой диаметр на выходе из рабочей решетки 𝑖−ой ступени':'Dk_rab_out_i',
                  'Средний диаметр на входе в сопловую решетку 𝑖−ой ступени':'Dsr_sopl_inl_i', 'Средний диаметр на выходе из сопловой решетки 𝑖−ой ступени':'Dsr_sopl_out_i',
                  'Средний диаметр на входе в рабочую решетку 𝑖−ой ступени':'Dsr_rab_inl_i', 'Средний диаметр на выходе из рабочей решетки 𝑖−ой ступени':'Dsr_rab_out_i',
                  'Переферийный диаметр на входе в сопловую решетку 𝑖−ой ступени':'Dp_sopl_inl_i', 'Переферийный диаметр на выходе из сопловой решетки 𝑖−ой ступени':'Dp_sopl_out_i',
                  'Переферийный диаметр на входе в рабочую решетку 𝑖−ой ступени':'Dp_rab_inl_i','Переферийный диаметр на выходе из рабочей решетки 𝑖−ой ступени':'Dp_rab_out_i',
                  'Высота сопловой лопатки на входе 𝑖−ой ступени':'h_sopl_inl_i', 'Высота сопловой лопатки на выходе 𝑖−ой ступени':'h_sopl_out_i',
                  'Высота рабочей лопатки на входе 𝑖−ой ступени':'h_rab_inl_i', 'Высота рабочей лопатки на выходе 𝑖−ой ступени':'h_rab_out_i',
                  'Отношение среднего диаметра к высоте РЛ 𝑖−ой ступени':'d_i',
                  'Ширина венца для СА':'S_sopl_i','Ширина венца для РК':'S_rab_i',
                  'Осевой зазор':'delta_s_i','Радиальный зазор':'delta_r_i',
                  'Угол раскрытия проточной части':'gamma'}

        df_1 = pd.DataFrame(list(data_1.items()),columns=['Параметры','Обозначение']) 
        df_2_ = pd.DataFrame(['-', 'м2', 'м2', 'м2', 'м2', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', 'м', '-','м', 'м', 'м', 'м','град'], columns = ['Разм'])
        df_2 = pd.DataFrame((array))
        df12_merged = df_1.join(df_2_, rsuffix='_right')
        df_merged = df12_merged.join(df_2, rsuffix='_right')

    return df_merged

def flow_pathPlot(dict):

    plt.style.use('seaborn-ticks') # задание стиля окна
    fig = plt.figure(figsize = (20,10)) # параметры окна
    ax = plt.axes()
    plt.tick_params(axis='both', which='major', labelsize=20, 
    direction = 'inout', length = 10, pad = 15) # настройка обозначений значений
    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'major', color = 'black', linewidth = 0.8) # настройка сетки
    plt.grid (which = 'minor', color = '#aaa', ls = ':')
    fig.suptitle('Геометрия проточной части ГТУ', size = 35, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
    plt.xlabel('L, м', fontsize = 25, loc = 'center')
    plt.ylabel('R, м',fontsize = 25,loc = 'center')  
    
    
    L = [0]
    j = 1
    for i in range(dict[0]['number_of_steps']):
        if i < dict[0]['number_of_steps']-1:
            L.append(L[j-1] + dict[2]['S_rab_i'][i] + 2 * dict[2]['delta_s_i'][i] + dict[2]['S_sopl_i'][i])
            j = j + 1
        else:
            L.append(L[j-1] + dict[2]['S_rab_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_sopl_i'][i])
            j = j + 1
    fp_vt, residuals, rank, sv, rcond = np.polyfit(L, dict[2]['d_vt_t'], 5, full = True)
    f_vt = sp.poly1d(fp_vt)
    fp_k, residuals, rank, sv, rcond = np.polyfit(L, dict[2]['d_k_t'], 5, full = True)
    f_k = sp.poly1d(fp_k)
    l = np.arange(L[0], L[dict[0]['number_of_steps']], 0.0001)
    D_vt = f_vt(l)
    D_k = f_k(l)
    Dp, = plt.plot(l, D_vt, color='b',linewidth=3, linestyle='-')
    Dk, = plt.plot(l, D_k, color='r',linewidth=3, linestyle='-')

    for i in range(dict[0]['number_of_steps']):
        plt.plot([L[i], L[i]], 
        [f_vt(L[i]), f_k(L[i])], color='black',linewidth = 4, linestyle='-')      
        plt.plot([L[i] + dict[2]['S_sopl_i'][i], L[i] + dict[2]['S_sopl_i'][i]], 
        [f_vt(L[i] + dict[2]['S_sopl_i'][i]), f_k(L[i] + dict[2]['S_sopl_i'][i])], color='black',linewidth = 4, linestyle='-')
        plt.plot([L[i], (L[i] + dict[2]['S_sopl_i'][i])], 
        [f_k(L[i]), f_k(L[i]+ dict[2]['S_sopl_i'][i])], color='black',linewidth = 4, linestyle='-')
        plt.plot([L[i], (L[i] + dict[2]['S_sopl_i'][i])], 
        [f_vt(L[i]), f_vt(L[i] + dict[2]['S_sopl_i'][i])], color='black',linewidth = 4, linestyle='-') 

        Dsr_sopl, = plt.plot([L[i], L[i] + dict[2]['S_sopl_i'][i]], 
        [dict[2]['Dsr_sopl_out_i'][i] / 2, dict[2]['Dsr_sopl_out_i'][i] / 2], color='black',linewidth = 2, linestyle='--')

        sopl, = plt.fill('s_x', "s_y", 'b',
        data={'s_x': [L[i], L[i], (L[i] + dict[2]['S_sopl_i'][i]), (L[i] + dict[2]['S_sopl_i'][i])],
              's_y': [f_k(L[i]), f_vt(L[i]), f_vt(L[i] + dict[2]['S_sopl_i'][i]), f_k(L[i] + dict[2]['S_sopl_i'][i])]})


        plt.plot([(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])], 
        [f_vt(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_k(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])], color='black',linewidth = 4, linestyle='-')               
        plt.plot([L[i] + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i], L[i] + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]],
        [f_vt(L[i] + dict[2]['S_rab_i'][i]  + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_k(L[i] + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])], color='black',linewidth = 4, linestyle='-')
        
        plt.plot([(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_rab_i'][i])], 
        [f_k(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_k(L[i]  + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])], color='black',linewidth = 4, linestyle='-')
        plt.plot([(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_rab_i'][i])], 
        [f_vt(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_vt(L[i]  + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])], color='black',linewidth = 4, linestyle='-')

        Dsr_rab, = plt.plot([L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i], L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_rab_i'][i]], 
        [dict[2]['Dsr_rab_out_i'][i] / 2, dict[2]['Dsr_rab_out_i'][i] / 2], color='black',linewidth = 2, linestyle='--')
        
        rab, = plt.fill('r_x', "r_y", 'r',
        data={'r_x': [(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_rab_i'][i]), (L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i] + dict[2]['S_rab_i'][i])],
              'r_y': [f_k(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_vt(L[i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_vt(L[i]  + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i]), f_k(L[i]  + dict[2]['S_rab_i'][i] + dict[2]['S_sopl_i'][i] + dict[2]['delta_s_i'][i])]})

    method = dict[2]['method']
    if method == 'root':
        ax.legend((sopl, rab, Dk), [r'$Сопловая$ $решетка$',
                                r'$Рабочая$ $решетка$',
                                r'$R_{корневой} = const$'],
                                fontsize = 20, frameon=True, framealpha=True)
    if method == 'medium':
        ax.legend((sopl, rab, Dsr_sopl), [r'$Сопловая$ $решетка$',
                                r'$Рабочая$ $решетка$',
                                r'$R_{средний} = const$'],
                                fontsize = 20, frameon=True, framealpha=True)

    if method == 'top':
        ax.legend((sopl, rab, Dp), [r'$Сопловая$ $решетка$',
                                r'$Рабочая$ $решетка$',
                                r'$R_{периферийный} = const$'],
                                fontsize = 20, frameon=True, framealpha=True)       
    plt.show()

# @st.cache
def geometry(fuel, sch, number_of_steps, axial_speed_input, axial_speed_outlet, 
             D_sr__h_2_z, K_s, K_r, radial_clearance, method = None):
        
        '''

        method - метод расчета геометрии канала

        root - постоянство корневого диаметра
        
        medium - постоянство среднего диаметра

        top- постоянство периферийного диаметра
    

        '''  
        
        lambda_0 = (axial_speed_input / sqrt((2 * interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) * sch[1]['R_g'] * (sch[1]['t_c'] + 273.15) * 1000) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) + 1)))
        lambda_z = (axial_speed_outlet / sqrt((2 * interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) * sch[1]['R_g'] * (sch[1]['t_d'] + 273.15) * 1000) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) + 1)))
        q_0 = (lambda_0 * ((1 - ((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) - 1) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) + 1)) * lambda_0**2)** (1 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) - 1))) * ((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) + 1) / 2)**(1 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) - 1)))
        q_z = (lambda_z * ((1 - ((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) - 1) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) + 1)) * lambda_z**2)** (1 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) - 1))) * ((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) + 1) / 2)**(1 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) - 1)))
        F_0 = (sch[2]['G_t'] * sqrt (sch[1]['t_c'] + 273.15) / (sch[1]['P_c'] * q_0 * sqrt((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) / sch[1]['R_g'] * 10**(-3)) * (2 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) + 1))**((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) + 1) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_c']) - 1)))))
        F2_z = (sch[2]['G_t'] * sqrt(sch[1]['t_d'] + 273.15) / (sch[1]['P_d'] * q_z * sqrt((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) / sch[1]['R_g'] * 10**(-3)) * (2 / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) + 1))**((interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) + 1) / (interpolate(fuel.get('k'), fuel.get('temperature_C'), sch[1]['t_d']) - 1))))) 

        height_2_z = (sqrt(F2_z / (pi * D_sr__h_2_z)))
        D_sr_z = (height_2_z * D_sr__h_2_z)
        D_k_z = (D_sr_z - height_2_z)
        D_p_z = (D_sr_z + height_2_z) 
        height_0 = ((sqrt(D_k_z**2 + 4 * F_0 / pi) - D_k_z) / 2)

        if method == 'root':
            D_k_1 = D_k_z
            D_sr_1 = (D_k_1 + height_0)  
            D_p_1 = (D_k_1 + 2 * height_0)

        if method == 'medium':
            D_k_1 = (D_sr_z - height_0)
            D_sr_1 = D_sr_z
            D_p_1 = (D_sr_z + height_0)

        if method == 'top':
            D_p_1 = (D_p_z)
            D_sr_1 = (D_p_1 - height_0)
            D_k_1 = (D_p_z - 2 * height_0)

        n_steps = [(i) / (number_of_steps) for i in range(number_of_steps + 1)]
        n_steps_dell = np.delete(n_steps, number_of_steps - number_of_steps)
        delta_F_t_i = [np.round((2.94 * (n_steps[i]**1.753) * np.exp(-1.0693 * n_steps[i])),4) for i in range(number_of_steps + 1)]
        delta_F_t_i = np.delete(delta_F_t_i, number_of_steps)
        delta_F_t_i = np.append(delta_F_t_i, 1)
        delta_F_tr_i = np.delete(delta_F_t_i, number_of_steps - number_of_steps)
        F_2_i = [(delta_F_tr_i[i] * (F2_z - F_0) + F_0) for i in range(number_of_steps)]

        if method == 'root':
            height_i = [((sqrt(D_k_z**2 + 4 * F_2_i[i] / pi) - D_k_z) / 2) for i in range(number_of_steps)]
            D_k_i = [D_k_z for i in range(number_of_steps)]
            D_sr_i = [(D_k_i[i] + height_i[i]) for i in range(number_of_steps)]
            D_p_i = [(D_k_i[i] + 2 * height_i[i]) for i in range(number_of_steps)]
            d_k_t = [D_k_i[i] / 2 for i in range(number_of_steps)]
            d_k_t.append(D_k_z / 2)
            d_vt_t = np.insert([(D_k_i[i] + 2 * height_i[i]) / 2 for i in range(number_of_steps)], number_of_steps - number_of_steps, (D_k_z + 2 * height_0) / 2)
        
        if method == 'medium':
            height_i = [((sqrt(D_k_z**2 + 4 * F_2_i[i] / pi) - D_k_z) / 2) for i in range(number_of_steps)]
            D_sr_i = [D_sr_z for i in range(number_of_steps)]
            D_k_i = [D_sr_i[i] - height_i[i] for i in range(number_of_steps)]
            D_p_i = [(D_k_i[i] + 2 * height_i[i]) for i in range(number_of_steps)]  
            d_vt_t = [(D_sr_i[i] + height_i[i]) / 2 for i in range(number_of_steps)]
            d_vt_t = np.insert(d_vt_t, number_of_steps - number_of_steps, D_p_1 / 2)
            d_k_t = [(D_sr_i[i] - height_i[i]) / 2 for i in range(number_of_steps)]
            d_k_t = np.insert(d_k_t, number_of_steps - number_of_steps, D_k_1 / 2)

        if method == 'top':  
            height_i = [((sqrt(D_k_z**2 + 4 * F_2_i[i] / pi) - D_k_z) / 2) for i in range(number_of_steps)]
            D_p_i = [D_p_z for i in range(number_of_steps)]
            D_sr_i = [(D_p_i[i] - height_i[i]) for i in range(number_of_steps)]
            D_k_i = [D_sr_i[i] - height_i[i] for i in range(number_of_steps)]
            d_vt_t = [D_p_i[i] / 2 for i in range(number_of_steps)]
            d_vt_t.append(D_p_z / 2)
            d_k_t = np.insert([(D_p_i[i] - 2 * height_i[i]) / 2 for i in range(number_of_steps)], number_of_steps - number_of_steps, (D_p_1 - 2 * height_0) / 2)

        S_sopl_i = [(K_s * D_sr_i[i]) for i in range(number_of_steps)]
        S_rab_i = [(K_r * D_sr_i[i]) for i in range(number_of_steps)]
        delta_s_i = [0.3 * S_rab_i[i] for i in range(number_of_steps)]
        delta_r_i = [radial_clearance for i in range(number_of_steps)]

        L = [0]
        j = 1
        for i in range(number_of_steps):
            if i < number_of_steps-1:
                L.append(L[j-1] + S_sopl_i[i] + 2 * delta_s_i[i] + S_rab_i[i])
                j = j + 1
            else:
                L.append(L[j-1] + S_sopl_i[i] + delta_s_i[i] + S_rab_i[i])
                j = j + 1         
        fp_vt, residuals, rank, sv, rcond = np.polyfit(L, d_vt_t, 5, full = True)
        f_vt = sp.poly1d(fp_vt)
        fp_k, residuals, rank, sv, rcond = np.polyfit(L, d_k_t, 5, full = True)
        f_k = sp.poly1d(fp_k)
        l = np.arange(L[1], L[number_of_steps], 0.001)
        D_vt = f_vt(l)
        D_k = f_k(l)

        F_1_inl_i = [pi * (f_vt(L[i]) * 2)**2 / 4 - pi * (f_k(L[i]) * 2)**2 / 4 for i in range(number_of_steps)]            
        F_1_out_i = [pi * (f_vt(L[i] + S_sopl_i[i]) * 2)**2 / 4 - pi * (f_k(L[i] + S_sopl_i[i]) * 2)**2 / 4 for i in range(number_of_steps)]          
        F_2_inl_i = [pi * (f_vt(L[i] + S_sopl_i[i] + delta_s_i[i]) * 2)**2 / 4 - pi * ((f_k(L[i] + S_sopl_i[i] + delta_s_i[i]))*2)**2 / 4 for i in range(number_of_steps)]
        F_2_out_i = [pi * (f_vt(L[i] + S_sopl_i[i] + delta_s_i[i] + S_rab_i[i]) * 2)**2 / 4 - pi * ((f_k(L[i] + S_sopl_i[i] + delta_s_i[i] + S_rab_i[i]))*2)**2 / 4 for i in range(number_of_steps)]        
        Dk_sopl_inl_i = [f_k(L[i]) * 2 for i in range(number_of_steps)]
        Dk_sopl_out_i = [f_k(L[i] + S_sopl_i[i]) * 2 for i in range(number_of_steps)]   
        Dk_rab_inl_i = [f_k(L[i] + S_sopl_i[i] + delta_s_i[i]) * 2 for i in range(number_of_steps)]
        Dk_rab_out_i = [f_k(L[i] + S_sopl_i[i] + delta_s_i[i] + S_rab_i[i]) * 2 for i in range(number_of_steps)]
        Dp_sopl_inl_i = [f_vt(L[i]) * 2 for i in range(number_of_steps)]
        Dp_sopl_out_i = [f_vt(L[i] + S_sopl_i[i]) * 2 for i in range(number_of_steps)]   
        Dp_rab_inl_i =  [f_vt(L[i] + S_sopl_i[i] + delta_s_i[i]) * 2 for i in range(number_of_steps)]
        Dp_rab_out_i = [f_vt(L[i] + S_sopl_i[i] + delta_s_i[i] + S_rab_i[i]) * 2 for i in range(number_of_steps)]
        Dsr_sopl_inl_i = [(Dk_sopl_inl_i[i] + Dp_sopl_inl_i[i]) / 2 for i in range(number_of_steps)]
        Dsr_sopl_out_i = [(Dk_sopl_out_i[i] + Dp_sopl_out_i[i]) / 2 for i in range(number_of_steps)]
        Dsr_rab_inl_i = [(Dk_rab_inl_i[i] + Dp_rab_inl_i[i]) / 2 for i in range(number_of_steps)]
        Dsr_rab_out_i = [(Dk_rab_out_i[i] + Dp_rab_out_i[i]) / 2 for i in range(number_of_steps)]
        h_sopl_inl_i = [(Dp_sopl_inl_i[i] - Dk_sopl_inl_i[i]) / 2 for i in range(number_of_steps)]
        h_sopl_out_i = [(Dp_sopl_out_i[i] - Dk_sopl_out_i[i]) / 2 for i in range(number_of_steps)]
        h_rab_inl_i = [(Dp_rab_inl_i[i] - Dk_rab_inl_i[i]) / 2 for i in range(number_of_steps)]
        h_rab_out_i = [(Dp_rab_out_i[i] - Dk_rab_out_i[i]) / 2 for i in range(number_of_steps)]
        gamma = [degrees(atan(((height_2_z + delta_r_i[i] - height_0) / ((number_of_steps * ((S_sopl_i[i] + S_rab_i[i] + (2 * number_of_steps - 1) * delta_s_i[i]))))))) for i in range(number_of_steps)]      
        d_i = [(Dsr_rab_out_i[i] / h_rab_out_i[i]) for i in range(number_of_steps)] 

        return ({'number_of_steps':number_of_steps, 'axial_speed_input':axial_speed_input, 'axial_speed_outlet':axial_speed_outlet,
                    'D_sr__h_2_z':D_sr__h_2_z, 'K_s': K_s, 'K_r': K_r, 'radial_clearance': radial_clearance},     
                    {'lambda_0': lambda_0, 'lambda_z':lambda_z, 'q_0': q_0, 'q_z':q_z, 
                    'F_0':F_0, 'F2_z':F2_z, 'D_k_1': D_k_1, 'D_k_z':D_k_z,
                    'D_sr_1': D_sr_1, 'D_sr_z':D_sr_z, 'D_p_1':D_p_1, 'D_p_z':D_p_z,
                    'height_0':height_0, 'height_2_z':height_2_z},                    
                    {'n_steps_dell':n_steps_dell,'F_1_inl_i':F_1_inl_i,'F_1_out_i':F_1_out_i,'F_2_inl_i':F_2_inl_i, 'F_2_out_i':F_2_out_i,
                    'Dk_sopl_inl_i':Dk_sopl_inl_i, 'Dk_sopl_out_i':Dk_sopl_out_i, 'Dk_rab_inl_i': Dk_rab_inl_i, 'Dk_rab_out_i': Dk_rab_out_i,
                    'Dsr_sopl_inl_i':Dsr_sopl_inl_i,'Dsr_sopl_out_i':Dsr_sopl_out_i, 'Dsr_rab_inl_i': Dsr_rab_inl_i, 'Dsr_rab_out_i': Dsr_rab_out_i,
                    'Dp_sopl_inl_i':Dp_sopl_inl_i, 'Dp_sopl_out_i':Dp_sopl_out_i, 'Dp_rab_inl_i': Dp_rab_inl_i, 'Dp_rab_out_i': Dp_rab_out_i,
                    'h_sopl_inl_i':h_sopl_inl_i, 'h_sopl_out_i':h_sopl_out_i, 'h_rab_inl_i': h_rab_inl_i, 'h_rab_out_i': h_rab_out_i,
                    'd_i':d_i, 'S_sopl_i':S_sopl_i, 'S_rab_i':S_rab_i, 'delta_s_i':delta_s_i, 'delta_r_i':delta_r_i,
                    'gamma':gamma, 'd_vt_t':d_vt_t, 'd_k_t':d_k_t, 'method':method},
                    [n_steps_dell, F_1_inl_i, F_1_out_i, F_2_inl_i, F_2_out_i,
                    Dk_sopl_inl_i, Dk_sopl_out_i, Dk_rab_inl_i, Dk_rab_out_i,
                    Dsr_sopl_inl_i, Dsr_sopl_out_i, Dsr_rab_inl_i, Dsr_rab_out_i,
                    Dp_sopl_inl_i, Dp_sopl_out_i, Dp_rab_inl_i, Dp_rab_out_i,
                    h_sopl_inl_i, h_sopl_out_i, h_rab_inl_i, h_rab_out_i,
                    d_i, S_sopl_i, S_rab_i, delta_s_i, delta_r_i, gamma])



# fuel = gas(_H_2S = 0, _CO_2 = 0.06, _O_2 = 0, _CO = 0, _H_2 = 0, _CH_2 = 0,
#         _CH_4 = 99.0, _C_2H_4 = 0, _C_2H_6 = 0.1, _C_3H_8 = 0.03,_C_4H_10 = 0.04, 
#         temperature_C = temperature_Cels)

# schemegtu = scheme(fuel = fuel, ele_power = 153*10e5, t_c = 1060,
#                                 t_a = 15, P_a = 100.5*10e2, epsilon = 10.9, coefficient_pressure_loss = 0.97,
#                                 etta_c_c = 0.995, etta_mch = 0.995, etta_e_g = 0.982,
#                                 etta_is_t = 0.89, etta_is_k = 0.87, leak_rate = 0.005, t_w = 850, z = 4, method = 'notcold')

# geometrygtu = geometry(fuel = fuel, sch = schemegtu, number_of_steps = 4, axial_speed_input = 180, axial_speed_outlet = 252,
#              D_sr__h_2_z = 3.5, K_s = 0.065, K_r = 0.06, radial_clearance = 0.0008, method = 'root')

# print(data_2(geometrygtu[0], method='inlet'))
# print(data_2(geometrygtu[1], method='geometry'))
# print(data_2(geometrygtu[3], method = 'geometrystep'))
# flow_pathPlot(geometrygtu)




