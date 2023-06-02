from geometrygtu import *

def data_3(array , method = True):
    if method == 'kinematics':
        data_1 = {'Угол входа в 𝑖−ую ступень':'alpha_0_i',
                  'Угол выхода из 𝑖−ой ступени':'alpha_02_i',
                  'Степень реактивности 𝑖−ой ступени':'ro_st_i',
                  'Осевая составляющая скорости на выходе из рабочей решетки 𝑖−ой ступени':'C2a_i',
                  'Коэффициент расхода для 𝑖−ой ступени':'C2a_i_',
                  'Коэффициент нагруженности для 𝑖−ой ступени':'Y_st_i',
                  'Коэффициент нагрузки 𝑖−ой ступени':'mu_st_i',
                  'КПД 𝑖−ой ступени':'etta_st_i',
                  'Предварительная полезная работа (по параметрам торможения) расширения газа в i-ой ступени':'L_st_i__',
                  'Величина невязки 𝑖−ой ступени': 'delta_H_i',
                  'Полезная работа (по параметрам торможения) расширения газа в i-ой ступен': 'L_st_i_',
                  'Изоэнтропийный теплоперепад (по параметрам торможения) 𝑖−ой ступени':'Hs_st_i_'}

        df_1 = pd.DataFrame(list(data_1.items()),columns=['Параметры','Обозначение']) 
        df_2_ = pd.DataFrame(['град', 'град', '-', 'м/c', '-', '-', '-', '-', 'кДж/кг', 'кДж/кг', 'кДж/кг', 'кДж/кг'], columns = ['Разм'])
        df_2 = pd.DataFrame((array))
        df12_merged = df_1.join(df_2_, rsuffix='_right')
        df_merged = df12_merged.join(df_2, rsuffix='_right')
    if method == 'termod':
        data_1 = {'Температура (заторможенного потока) на входе СА i-ой ступени':'T0_i_',
                  'Температура (заторможенного потока) на выходе из РК i-ой ступени':'T2_i_',
                  'Статическая температура на выходе из РК i-ой ступени':'T2_i',
                  'Статическая (изоэнтропическая )температура на выходе из РК i-ой ступени':'T2s_i',
                  'Изонтропийная температура (заторможенного потока) на выходе из СА i-ой ступени':'T2s_i_',
                  'Давление (заторможенного потока) на входе в СА i-ой ступени':'P0_i_',
                  'Давление (заторможенного потока) на выходе из РК i-ой ступени':'P2_i_',
                  'Давление статическое на выходе из РК i-ой ступени':'P2_i',
                  'Газодинамическая функция q на выходе из РК i-ой ступени':'q_lamda_c2a_i',
                  'Газодинамическая функция lamda на выходе из РК i-ой ступени':'lamda_c2a_i',
                  'Газодинамическая функция PI на выходе из РК i-ой ступени':'PI_lamda_c2a_i',
                  'Газодинамическая функция tau на выходе из РК i-ой ступени':'tau_lamda_c2a_i',
                  'Изоэнтропийный теплоперепад 𝑖−ой ступени':'Hs_st_i'}

        df_1 = pd.DataFrame(list(data_1.items()),columns=['Параметры','Обозначение']) 
        df_2_ = pd.DataFrame(['К', 'К', 'К', 'К', 'К', 'Па', 'Па', 'Па', '-', '-', '-', '-', 'кДж/кг'], columns = ['Разм'])
        df_2 = pd.DataFrame((array))
        df12_merged = df_1.join(df_2_, rsuffix='_right')
        df_merged = df12_merged.join(df_2, rsuffix='_right')
        
    return df_merged

def I(T, fuel):
    return interpolate(fuel.get('h'), fuel.get('temperature_K'), T)

def T(h, fuel):
    return interpolate(fuel.get('temperature_K'), fuel.get('h'), h)

def k(T, fuel):
    return interpolate(fuel.get('k'), fuel.get('temperature_K'), T)  
    
def lamda(velocity, T, fuel, sch):
    return (velocity / sqrt((2e3 * k(T, fuel) * sch['R_g'] * T) / (k(T, fuel) + 1)))

def PI_lamda(lamda, T, fuel):
    return ((1 - (((k(T, fuel) - 1) / (k(T, fuel) + 1)) * lamda**2))**(k(T, fuel) / (k(T, fuel) - 1)))

def q_lamda(lamda, T, fuel):
    return (lamda * (((k(T, fuel) + 1) / 2)**(1 / (k(T, fuel) - 1))) * ((1 - (((k(T, fuel) - 1) / (k(T, fuel) + 1)) * lamda**2))**(k(T, fuel) / (k(T) - 1))))

def tau_lamda(lamda, T, fuel):
    return(1 - ((k(T, fuel) - 1) / (k(T, fuel) + 1)) * (lamda)**2)

def m_(T, fuel, sch):
    return (sqrt((k(T, fuel) / sch[1]['R_g'] *  10**(-3)) * (2 / (k(T, fuel) + 1))**((k(T, fuel) + 1) / (k(T, fuel) - 1))))

def MusatkinY_st(c_2a, ro, alpha2):
    if 0 < c_2a <= 0.65: #При C_a=0.5
        y = [60,70,80,90,100,110] #Величина alfa_2
        x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] #ρ_cр
        z = [[0.44,0.46,0.485,0.512,0.545,0.588,0.628],
              [0.462,0.485,0.512,0.545,0.585,0.636,0.7],   #Y_ст
              [0.485,0.512,0.545,0.588,0.635,0.692,0.772],
              [0.512,0.542,0.578,0.6,0.6783,0.7427,0.844],
              [0.538,0.575,0.615,0.678,0.723,0.7947,0.916],
              [0.57,0.608,0.656,0.7157,0.7683,0.847,0.988]]
        f = interp2d(x, y, z, kind='cubic')
        z = f(ro, alpha2)

    elif 0.65 < c_2a <= 0.95: #При C_a=0.8
        y = [60,70,80,90,100,110] #Величина alfa_2
        x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] #ρ_cр
        z = [[0.411,0.43,0.45,0.472,0.494,0.518,0.554],
              [0.44,0.465,0.488,0.52,0.548,0.584,0.63],   #Y_ст
              [0.474,0.51,0.54,0.578,0.615,0.665,0.706],
              [0.514,0.555,0.595,0.645,0.7,0.736,0.782],
              [0.558,0.606,0.658,0.698,0.7605,0.8095,0.858],
              [0.612,0.658,0.7031,0.7557,0.829,0.883,0.934]]
        f = interp2d(x, y, z, kind='cubic')
        z = f(ro, alpha2)
    else:    #При C_a=1.1
        y0 = [60,70,80,90,100] #Величина alfa_2
        x0 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] #ρ_cр
        z0 = [[0.368,0.4,0.42,0.438,0.455,0.478,0.5],
            [0.418,0.444,0.466,0.49,0.52,0.55,0.582],   #Y_ст
            [0.464,0.5,0.532,0.564,0.598,0.644,0.69],
            [0.516,0.568,0.6,0.64,0.684,0.723,0.7807],
            [0.576,0.645,0.68,0.703,0.7555,0.8063,0.8757]]
        f = interp2d(x0, y0, z0, kind='cubic')
        z = f(ro, alpha2)
    return z[0]

def polyfit2d(x, y, z, order=3):
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    for k, (i,j) in enumerate(ij):
        G[:,k] = x**i * y**j
    m, _, _, _ = np.linalg.lstsq(G, z)
    return m

def polyval2d(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    p = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        p += a * x**i * y**j
    return p

def table2(arr, method):
    plt.style.use('seaborn-ticks') # задание стиля окна
    fig = plt.figure(figsize=(15,10)) # параметры окна
    ax = plt.axes()
    plt.tick_params(axis='both', which='major', labelsize=15, 
                    direction = 'inout', length=10, pad = 15) # настройка обозначений значений
    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'major', color = '#aaa', linewidth = 0.8) # настройка сетки
    plt.grid (which = 'minor', color = '#aaa', ls = ':')
    
    if method == 'temperature':
        fig.suptitle('Распределение температур i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('T, К',fontsize=20,loc = 'center')
        T0_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['T0_i_'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        T2_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['T2_i_'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        T2_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['T2_i'], color='black',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        T2s_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['T2s_i'], color='g',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        T2s_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['T2s_i_'], color='#800080',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        ax.legend((T0_i_, T2_i_, T2_i, T2s_i, T2s_i_), [r'$\overline {T_{0i}}$ - $Температура$ $на$ $входе$ $СА$',
                                                        r'$\overline {T_{2i}}$ - $Температура$ $на$ $выходе$ $из$ $РК$', 
                                                        r'$T_{2i}$ - $Статическая$ $температура$ $на$ $выходе$ $из$ $РК$', 
                                                        r'$T_{2si}$ - $Статическая$ $температура$ $на$ $выходе$ $из$ $РК$', 
                                                        r'$\overline {T_{2si}}$ - $Изонтропийная$ $температура$ $на$ $выходе$ $из$ $СА$'],
                                        fontsize = 15, frameon=True, framealpha=True)      
    if method == 'pressure':
        fig.suptitle('Распределение давлений i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('P, Па',fontsize=20,loc = 'center')
        P0_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['P0_i_'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        P2_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['P2_i_'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        P2_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['P2_i'], color='black',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 

        ax.legend((P0_i_, P2_i_, P2_i,), [r'$\overline {P_{0i}}$ - $Давление$ $на$ $входе$ $в$ $СА$',
                                          r'$\overline {P_{2i}}$ - $Давление$ $на$ $выходе$ $из$ $РК$', 
                                          r'$P_{2i}$ - $Давление$ $статическое$ $на$ $выходе$ $из$ $РК$'],
                                        fontsize = 15, frameon=True, framealpha=True)   
    if method == 'alpha':
        fig.suptitle(r'Распределение углов $\alpha$ i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('apha, град',fontsize=20,loc = 'center')
        alpha_0_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['alpha_0_i'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        alpha_02_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['alpha_02_i'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        ax.legend((alpha_0_i, alpha_02_i,), [r'$\alpha_{0i}$ - $Угол$ $входа$ $в$ $ступень$',
                                             r'$\alpha_{2i}$ - $Угол$ $выхода$ $из$ $ступени$'],
                                        fontsize = 15, frameon=True, framealpha=True)
    if method == 'velocity':    
        fig.suptitle(r'Распределение скорости $C_{2a}$ i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('C2a, м/c',fontsize=20,loc = 'center')
        C2a_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['C2a_i'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        ax.legend([C2a_i], [r'$C_{2ai}$ - $Осевая$ $составляющая$ $скорости$ $на$ $выходе$ $из$ $РК$'], fontsize = 15, frameon=True, framealpha=True)   
    if method == 'heatdrop':
        fig.suptitle(r'Распределение теплоперепадов i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('Lst, Hst, кДж/кг',fontsize=20,loc = 'center')
        L_st_i__, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['L_st_i__'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        delta_H_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['delta_H_i'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        L_st_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['L_st_i_'], color='g',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        Hs_st_i_, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['Hs_st_i_'], color='black',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
        Hs_st_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['Hs_st_i'], color='#800080',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-') 
       
        ax.legend([L_st_i__, delta_H_i, L_st_i_, Hs_st_i_, Hs_st_i], [r'$\overline {L}_{sti}^\prime$ - $Предварительная$ $полезная$ $работа$ $расширения$ $газа$',
                                          r'$\Delta H_i$ - $Величина$ $невязки$ $ступени$',
                                          r'$\overline {L_{sti}}$ - $Полезная$ $работа$ $расширения$ $газа$',
                                          r'$\overline {H_{s_{sti}}}$ - $Изоэнтропийный$ $теплоперепад$ $ступени$',
                                          r'$H_{s_{sti}}$ - $Изоэнтропийный$ $теплоперепад$ $ступени$'],
                                        fontsize = 15, frameon=False, framealpha=False)
    if method == 'ro':    
        fig.suptitle(r'Распределение степени реактивности $\rho$ i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('rho, -', fontsize=20, loc = 'center')
        ro_st_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['ro_st_i'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        ax.legend([ro_st_i], [r'$\rho$ - $Степень$ $реактивности$'], fontsize = 15, frameon=True, framealpha=True)        
    if method == 'etta':    
        fig.suptitle(r'Распределение КПД  $\eta$ i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('etta, -', fontsize=20, loc = 'center')
        etta_st_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[0]['etta_st_i'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        ax.legend([etta_st_i], [r'$\eta$ - $КПД$ $ступени$'], fontsize = 15, frameon=True, framealpha=True)       
    if method == 'gdinamyc':    
        fig.suptitle(r'Распределение газодинамических функций i-ой ступени', size = 30, weight = 1000,ha = 'center', va = 'center_baseline', style = 'italic')
        plt.xlabel('n - номер ступени, -', fontsize=20, loc = 'center')
        plt.ylabel('lamda,q, pi,tau, -', fontsize=20, loc = 'center')
        lamda_c2a_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['lamda_c2a_i'], color='r',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')        
        q_lamda_c2a_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['q_lamda_c2a_i'], color='b',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        PI_lamda_c2a_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['PI_lamda_c2a_i'], color='g',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        tau_lamda_c2a_i, = plt.plot(np.linspace(1, arr[0]['number_of_steps'], arr[0]['number_of_steps']), arr[1]['tau_lamda_c2a_i'], color='black',marker='o', ms = 8, markerfacecolor='w',linewidth=3, linestyle='-')
        ax.legend([lamda_c2a_i ,q_lamda_c2a_i, PI_lamda_c2a_i, tau_lamda_c2a_i], [r'$\lambda$',r'$q(\lambda)$', r'$\pi(\lambda)$',r'$\tau(\lambda)$'], fontsize = 15, frameon=True, framealpha=True)       
    plt.show()

x1 = np.array([0.4, 0.5, 0.6,0.7,0.720192308,0.7,0.4,0.5,0.6,0.7,0.720192308,0.8,0.814423077,0.8,0.4,0.5,0.6,0.7,
0.720192308,0.8,0.814423077,0.86,0.887884615,0.86,0.4,0.5,0.6,0.7,0.720192308,0.8,0.814423077,0.86,0.887884615,
0.9,0.959038462,0.9,0.4,0.5,0.6,0.7,0.720192308,0.8,0.86,0.887884615,0.9,0.959038462,1,1.021538462,1,0.959038462,
0.5,0.6,0.7,0.720192308,0.8,0.814423077,0.86,0.887884615,0.9,0.959038462,1,1.021538462,1.083076923,1.021538462,
0.6,0.7,0.720192308,0.8,0.814423077,0.86,0.887884615,0.9,0.959038462,1,1.021538462,1.083076923,1.1,0.7,0.720192308,
0.8,0.814423077,0.86,0.887884615,0.9,0.959038462,1,1.021538462,1.083076923,1.1])

y1 = np.array([1.029090909, 1.189090909, 1.301818182,0.898181818,1.090909091,1.261818182,1.134545455,1.341818182,1.516363636,
1.629090909,1.643636364,0.967272727,1.309090909,1.570909091,1.269090909,1.509090909,1.72,1.850909091,1.861818182,
1.829090909,1.770909091,0.978181818,1.374545455,1.643636364,1.385454545,1.661818182,1.898181818,2.043636364,2.058181818,
2.036363636,2.018181818,1.96,1.905454545,0.887272727,1.436363636,1.865454545,1.538181818,1.84,2.058181818,
2.210909091,2.225454545,2.236363636,2.210909091,2.189090909,2.163636364,2.04,1.872727273,1.483636364,1.101818182,
0.887272727,2.04,2.247272727,2.367272727,2.389090909,2.410909091,2.414545455,2.403636364,2.389090909,2.378181818,
2.290909091,2.218181818,2.145454545,1.629090909,0.974545455,2.44,2.589090909,2.607272727,2.647272727,2.654545455,
2.650909091,2.643636364,2.647272727,2.570909091,2.512727273,2.465454545,2.28,2.243636364,2.763636364,2.76,
2.796363636,2.807272727,2.821818182,2.818181818,2.807272727,2.778181818,2.741818182,2.709090909,2.570909091,2.549090909])

z1 = np.array([0.94,0.94,0.94,0.94,0.94,0.94,0.93,0.93,0.93,0.93,0.93,0.93,0.93,0.93,0.92,0.92,0.92,0.92,0.92,
0.92,0.92,0.92,0.92,0.92,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.91,0.9,0.9,0.9,
0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.89,
0.89,0.89,0.89,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.88,0.87,0.87,0.87,0.87,
0.87,0.87,0.87,0.87,0.87,0.87,0.87,0.87])

m = polyfit2d(x1, y1, z1)

@st.cache
def parameters(fuel, sch, geom, ro_st_i, alpha_02_i, delta_H, periodicity):
    U_sr_z = pi * ((geom[2]['Dsr_sopl_inl_i'][geom[0]['number_of_steps'] - 1] + geom[2]['Dsr_sopl_out_i'][geom[0]['number_of_steps'] - 1] + geom[2]['Dsr_sopl_out_i'][geom[0]['number_of_steps'] - 1] + geom[2]['Dsr_rab_out_i'][geom[0]['number_of_steps'] - 1]) / 4) * periodicity
    C_2a_z_= geom[0]['axial_speed_outlet'] / U_sr_z
    Y_st_z = MusatkinY_st(C_2a_z_, ro_st_i[geom[0]['number_of_steps'] - 1], alpha_02_i[geom[0]['number_of_steps'] - 1])
    D_sr = sum([geom[2]['Dsr_sopl_inl_i'][i] + geom[2]['Dsr_sopl_out_i'][i] +
    geom[2]['Dsr_sopl_out_i'][i] + geom[2]['Dsr_rab_out_i'][i] for i in range(geom[0]['number_of_steps'])]) / (4 * geom[0]['number_of_steps'])
    Y_t = (pi * D_sr * periodicity) / (2000 * sch[1]['H_t'] / geom[0]['number_of_steps'])**0.5
    delta_Y = abs((Y_st_z - Y_t) / Y_st_z * 100)
    mu_st_z = 1 / (2 * Y_st_z**2)
    alpha_0_i = [90] 
    alpha_0_i.extend(alpha_02_i[0:geom[0]['number_of_steps']]) 
    alpha_0_i = (alpha_0_i[0:geom[0]['number_of_steps']]) 
    C2a_i = np.linspace(geom[0]['axial_speed_input'], geom[0]['axial_speed_outlet'], geom[0]['number_of_steps'])
    C2a_i_ = np.array([C2a_i[i] / (pi * geom[2]['Dsr_rab_out_i'][i] * periodicity) for i in range(geom[0]['number_of_steps'])])
    Y_st_i = [MusatkinY_st(C2a_i_[i], ro_st_i[i], alpha_02_i[i]) for i in range(geom[0]['number_of_steps'])]
    mu_st_i = [ 1 / (2 * Y_st_i[i]**2) for i in range(geom[0]['number_of_steps'])]
    etta_st_i = np.array([polyval2d(C2a_i_[i], mu_st_i[i], m) for i in range(geom[0]['number_of_steps'])])
    L_st_i__= [(pi * ((geom[2]['Dsr_sopl_inl_i'][i] + geom[2]['Dsr_sopl_out_i'][i] + geom[2]['Dsr_sopl_out_i'][i] + geom[2]['Dsr_rab_out_i'][i]) / 4)
               * periodicity)**2 / (2000 * Y_st_i[i]**2) * etta_st_i[i] for i in range(geom[0]['number_of_steps'])]
    S_L = sum(L_st_i__)
    d_H = abs((sch[1]['H_t'] - S_L))   
    delta_H_i = [delta_H[i] * d_H  for i in range(geom[0]['number_of_steps'])]
    L_st_i_= [L_st_i__[i] + delta_H_i[i] for i in range(geom[0]['number_of_steps'])]
    Hs_st_i_ = [L_st_i_[i] / etta_st_i[i] for i in range(geom[0]['number_of_steps'])]
    
    I0_i_, T0_i_, P0_i_= [I((sch[1]['t_c'] + 273.15), fuel)], [(sch[1]['t_c'] + 273.15)],[sch[1]['P_c']]
    I2_i_, T2_i_, P2_i_=[],[],[]
    I2s_i_, T2s_i_=[],[]  
    for i in range(geom[0]['number_of_steps']):
        if i < geom[0]['number_of_steps'] - 1:
            I0_i_.append(I0_i_[i] - L_st_i_[i])
            T0_i_.append(T(I0_i_[i + 1], fuel))
        I2_i_.append(I0_i_[i] - L_st_i_[i])
        T2_i_.append(T(I2_i_[i], fuel))
        I2s_i_.append(I0_i_[i] - Hs_st_i_[i])
        T2s_i_.append(T(I2s_i_[i], fuel))
        if i< geom[0]['number_of_steps']-1:
            P0_i_.append(P0_i_[i] / ((T0_i_[i]) / (T2s_i_[i]))**(k(T0_i_[i], fuel) / (k(T0_i_[i],fuel) - 1)))
        P2_i_.append(P0_i_[i] / ((T0_i_[i]) / (T2s_i_[i]))**(k(T0_i_[i], fuel) / (k(T0_i_[i], fuel) - 1)))
    q_lamda_c2a_i = [(sch[2]['G_t'] * sqrt(T2_i_[i])) / (m_(T2_i_[i], fuel, sch) * P2_i_[i] * geom[2]['F_2_out_i'][i] * sin(radians(alpha_02_i[i]))) for i in range(geom[0]['number_of_steps'])]
    lamda_i=[]
    for n in q_lamda_c2a_i:
        def q(x):
            return x * (1 - (k(T2_i_[i], fuel) - 1) / (k(T2_i_[i], fuel) + 1) * x**2)**(1 / (k(T2_i_[i], fuel) - 1)) - n / ((k(T2_i_[i], fuel) + 1) / 2)**(1 / (k(T2_i_[i], fuel) - 1))
        lamda_i.append(fsolve(q,0.01)) 
    lamda_c2a_i = [i[0] for i in lamda_i]      
    PI_lamda_c2a_i = [PI_lamda(lamda_c2a_i[i], T2_i_[i], fuel) for i in range(geom[0]['number_of_steps'])]
    tau_lamda_c2a_i = [tau_lamda(lamda_c2a_i[i], T2_i_[i], fuel) for i in range(geom[0]['number_of_steps'])]
    P2_i = [P2_i_[i] * PI_lamda_c2a_i[i] for i in range(geom[0]['number_of_steps'])]
    T2_i = [T2_i_[i] * tau_lamda_c2a_i[i] for i in range(geom[0]['number_of_steps'])]
    T2s_i = [T0_i_[i] * (P2_i[i] / P0_i_[i])**((k(T0_i_[i], fuel) - 1) / (k(T0_i_[i], fuel))) for i in range(geom[0]['number_of_steps'])]
    Hs_st_i = [I(T0_i_[i], fuel) - I(T2s_i[i], fuel) for i in range(geom[0]['number_of_steps'])]

    return {'alpha_0_i':alpha_0_i, 'alpha_02_i':alpha_02_i, 'ro_st_i':ro_st_i, 'C2a_i':C2a_i, 'C2a_i_':C2a_i_,
            'Y_st_i':Y_st_i, 'mu_st_i':mu_st_i, 'etta_st_i':etta_st_i, 'L_st_i__':L_st_i__, 'delta_H_i':delta_H_i, 
            'L_st_i_':L_st_i_, 'Hs_st_i_':Hs_st_i_, 'number_of_steps':geom[0]['number_of_steps']}, {'T0_i_':T0_i_, 'T2_i_':T2_i_, 'T2_i':T2_i, 'T2s_i':T2s_i, 'T2s_i_':T2s_i_, 'P0_i_':P0_i_,
             'P2_i_':P2_i_, 'P2_i':P2_i, 'q_lamda_c2a_i':q_lamda_c2a_i, 'lamda_c2a_i':lamda_c2a_i, 'PI_lamda_c2a_i':PI_lamda_c2a_i,
             'tau_lamda_c2a_i':tau_lamda_c2a_i, 'Hs_st_i':Hs_st_i}, (alpha_0_i, alpha_02_i, ro_st_i, C2a_i, C2a_i_, Y_st_i, 
            mu_st_i, etta_st_i, L_st_i__, delta_H_i, L_st_i_, Hs_st_i_),(T0_i_, T2_i_, T2_i, T2s_i, T2s_i_, P0_i_, P2_i_, P2_i, q_lamda_c2a_i, lamda_c2a_i, PI_lamda_c2a_i, tau_lamda_c2a_i, Hs_st_i)

fuel = gas(_H_2S = 0, _CO_2 = 0.06, _O_2 = 0, _CO = 0, _H_2 = 0, _CH_2 = 0,
        _CH_4 = 99.0, _C_2H_4 = 0, _C_2H_6 = 0.1, _C_3H_8 = 0.03,_C_4H_10 = 0.04, 
        temperature_C = temperature_Cels)
schemegtu = scheme(fuel = fuel, ele_power = 153*10e5, t_c = 1060,
                                t_a = 15, P_a = 100.5*10e2, epsilon = 10.9, coefficient_pressure_loss = 0.97,
                                etta_c_c = 0.995, etta_mch = 0.995, etta_e_g = 0.982,
                                etta_is_t = 0.89, etta_is_k = 0.87, leak_rate = 0.005, t_w = 850, z = 4, method = 'notcold')
geometrygtu = geometry(fuel = fuel, sch = schemegtu, number_of_steps = 4, axial_speed_input = 180, axial_speed_outlet = 252,
             D_sr__h_2_z = 3.5, K_s = 0.065, K_r = 0.06, radial_clearance = 0.0008, method = 'root')

parametergtu = parameters(fuel = fuel, sch = schemegtu, geom = geometrygtu, ro_st_i = [0.3, 0.367, 0.433, 0.5], alpha_02_i = [70, 76.67, 83.33, 90], delta_H = [0.55, 0.35, 0.05, 0.05 ], periodicity = 50)

# print(data_3(parametergtu[2], 'kinematics'))
# print(data_3(parametergtu[3], 'termod'))
# table2(parametergtu, 'gdinamyc')

