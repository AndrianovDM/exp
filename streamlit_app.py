from distributiongtu import *

def Save_to_file_stage(stage, name , extension ):
    with pd.ExcelWriter((name + extension)) as writer:
        stage.to_excel(writer, sheet_name='sheet1', index=False,header=False,)

def count(counter, column, name, format, ke):
    if counter not in st.session_state:
        st.session_state[counter] = 0.00
    val = column.number_input((name), format = format, value = st.session_state[counter], key = ke)
    if val:
        st.session_state[counter] = st.session_state[ke]
    return st.session_state[counter]

def countRAH(num):
    ro_index, alpha_02_index, delta_H_index = [], [], []
    ro, alpha_02, delta_H = [], [], []
    for i in range(num):
        ro_index.append(f'ro_{i + 1}')
        alpha_02_index.append(f'alpha_02_{i + 1}')
        delta_H_index.append(f'delta_H_{i + 1}')

    for i in range(num):
        ro_index[i], alpha_02_index[i], delta_H_index[i] = st.columns(3)
    for i in range(num):
        ro.append(count(counter = f'ro{i}', column = ro_index[i], name = f"Степень реактивности ст. № {i+1}, -", format = "%f", ke = f'ro_{i + 1}'))
    for i in range(num):   
        alpha_02.append(count(counter = f'alpha_02{i}', column = alpha_02_index[i], name = f"Угол выхода ст. № {i+1}, град", format = "%f", ke = f'alpha_02_{i + 1}'))
    for i in range(num):  
        delta_H.append(count(counter = f'delta_H{i}', column = delta_H_index[i], name = f"Доля величины невязки ст. № {i+1}, -", format = "%f", ke = f'delta_H_{i + 1}'))
    return ro, alpha_02, delta_H

Panel = st.sidebar.radio('Этапы расчета ГТУ:', ["1. - Расчет состава топлива", 
                                                "2. - Расчет схемы ГТУ", 
                                                "3. - Расчет геометрии ГТУ", 
                                                "4. - Расчет параметров по ступеням"])

st.set_option('deprecation.showPyplotGlobalUse', False)

if Panel == "1. - Расчет состава топлива":
    st.title('Расчет состава топлива')
    st.header('Ввод исходных данных')
    st.session_state.fuel = None
    with st.form(key='my_form_1'):
        _CO_, _H_2_, _CH_2_, = st.columns(3)
        _H_2S_, _CO_2_, _O_2_= st.columns(3)
        _CH_4_, _C_2H_4_, _C_2H_6_, = st.columns(3)
        _C_3H_8_, _C_4H_10_ = st.columns(2)

        H_2S_ = count(counter = 'H_2S_', column = _H_2S_, name = "H_2S, %", format = "%f", ke = 'count1')
        CO_2_ = count(counter = 'CO_2_', column = _CO_2_, name = "CO_2, %", format = "%f", ke = 'count2')
        O_2_ = count(counter = 'O_2_', column = _O_2_, name = "O_2, %", format = "%f", ke = 'count3')
        CO_ = count(counter = 'CO_', column = _CO_, name = "CO, %", format = "%f", ke = 'count4')
        H_2_ = count(counter = 'H_2_', column = _H_2_, name = "H_2, %", format = "%f", ke = 'count5')
        CH_2_ = count(counter = 'CH_2_', column = _CH_2_, name = "CH_2, %", format = "%f", ke = 'count6')
        CH_4_ = count(counter = 'CH_4_', column = _CH_4_, name = "CH_4, %", format = "%f", ke = 'count7')
        C_2H_4_ = count(counter = 'C_2H_4_', column = _C_2H_4_, name = "C_2H_4, %", format = "%f", ke = 'count8')
        C_2H_6_ = count(counter = 'C_2H_6_', column = _C_2H_6_, name = "C_2H_6, %", format = "%f", ke = 'count9')
        C_3H_8_ = count(counter = 'C_3H_8_', column = _C_3H_8_, name = "C_3H_8, %", format = "%f", ke = 'count10')
        C_4H_10_ = count(counter = 'C_4H_10_', column = _C_4H_10_, name = "C_4H_10, %", format = "%f", ke = 'count11')
        st.write('H_2S = ', H_2S_, '; ', 'CO_2 = ',CO_2_, '; ', 'O_2 = ', O_2_, '; ', 'CO = ',CO_, '; ', 'H_2 = ', H_2_, '; ', 'CH_2 = ', CH_2_)
        st.write('C_2H_4 = ',C_2H_4_, '; ', 'CH_4 = ',CH_4_,'; ','C_2H_6 = ', C_2H_6_, '; ','C_3H_8 = ', C_3H_8_, '; ','C_4H_10 = ', C_4H_10_)

        if st.form_submit_button('Расчет'):
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
        fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
        st.session_state.fuel = fuel

        if st.form_submit_button('Показать таблицу параметров'): 
            st.header('Результаты расчета')
            st.table(table(temperature_C = st.session_state.fuel.get('temperature_C'), temperature_K = st.session_state.fuel.get('temperature_K'), u = st.session_state.fuel.get('u'), h = st.session_state.fuel.get('h'), s_0 = st.session_state.fuel.get('s_0'), Cp = st.session_state.fuel.get('Cp'), Cv = st.session_state.fuel.get('Cv'), k = st.session_state.fuel.get('k')))
        
        if st.form_submit_button('Показать графики параметров'):
            st.header('График распределения параметров')
            st.pyplot(visual_table(x = st.session_state.fuel.get('temperature_C'), y = st.session_state.fuel.get('h'), name_X = 't, град', name_Y = 'h, кДж/кг'))
            st.pyplot(visual_table(x = st.session_state.fuel.get('temperature_C'), y = st.session_state.fuel.get('s_0'), name_X = 't, град', name_Y = 'S, кДж/(кг*К)'))
            st.pyplot(visual_table(x = st.session_state.fuel.get('temperature_C'), y = st.session_state.fuel.get('Cp'), name_X = 't, град', name_Y = 'Cp, -'))
            st.pyplot(visual_table(x = st.session_state.fuel.get('temperature_C'), y = st.session_state.fuel.get('k'), name_X = 't, град', name_Y = 'k, -'))
        
        name = st.text_input(label = 'Название файла')
        if st.form_submit_button('Сохранить расчеты в Excel '):
            Save_to_file_stage(table(temperature_C = st.session_state.fuel.get('temperature_C'), temperature_K = st.session_state.fuel.get('temperature_K'), u = st.session_state.fuel.get('u'), h = st.session_state.fuel.get('h'), s_0 = st.session_state.fuel.get('s_0'), Cp = st.session_state.fuel.get('Cp'), Cv = st.session_state.fuel.get('Cv'), k = st.session_state.fuel.get('k')), name = name, extension ='.xlsx')

if Panel == "2. - Расчет схемы ГТУ":
    st.title('Расчет схемы ГТУ')
    st.image(Image.open('B:\Postgraduate studies\ДИСЕРТАЦИЯ АСПИАРНТУРА\ProgrammGTU\SchemeGTU.png'))
    select_1 = st.selectbox('Выберите тип схемы ГТУ:', ('Расчет схемы без охлаждения', 'Расчет схемы с охлаждением'))
    st.header('Ввод исходных данных схемы ГТУ')
    st.session_state.count34 = None
    st.session_state.schemegtu = None
    if select_1 ==  'Расчет схемы без охлаждения':
        st.session_state.count34 = 'notcold'
        st.session_state.t_w_ = 0.0
        st.session_state.z_ = 0.0
        with st.form(key='my_form_2'):
            _t_a_, _P_a_,  _etta_is_k_= st.columns(3)
            _t_c_, _epsilon_, _etta_is_t_ = st.columns(3)
            _ele_power_, _pressure_loss_, _leak_rate_ = st.columns(3)
            _etta_c_c_, _etta_mch_, _etta_e_g_ =st.columns(3)

            t_a_ = count(counter = 't_a_', column = _t_a_, name = "Температура на входе в комп., ℃", format = "%f", ke = 'count12')
            P_a_ = count(counter = 'P_a_', column = _P_a_, name = "Давление на входе, Па", format = "%f", ke = 'count13')
            etta_is_k_ = count(counter = 'etta_is_k_', column = _etta_is_k_, name = "КПД компрессора, -", format = "%f", ke = 'count14')
            t_c_ = count(counter = 't_c_', column = _t_c_, name = "Температура на входе в турб., ℃", format = "%f", ke = 'count15')
            epsilon_ = count(counter = 'epsilon_', column = _epsilon_, name = "Степень сжатия в компрессоре, -", format = "%f", ke = 'count16')
            etta_is_t_ = count(counter = 'etta_is_t_', column = _etta_is_t_, name = "КПД турбины, -", format = "%f", ke = 'count17')  
            ele_power_ = count(counter = 'ele_power_', column = _ele_power_, name = "Электрическая мощность ГТУ, Вт", format = "%f", ke = 'count18')
            pressure_loss_ = count(counter = 'pressure_loss_', column = _pressure_loss_, name = "Коэффициент потерь давления, -", format = "%f", ke = 'count19')
            leak_rate_ = count(counter = 'leak_rate_', column = _leak_rate_, name = "Коэффициент утечек, -", format = "%f", ke = 'count20')
            etta_c_c_ = count(counter = 'etta_c_c_', column = _etta_c_c_, name = "Коэффициент теплоты топлива, -", format = "%f", ke = 'count21')
            etta_mch_ = count(counter = 'etta_mch_', column = _etta_mch_, name = "Механический КПД турбины, -", format = "%f", ke = 'count22')
            etta_e_g_ = count(counter = 'etta_e_g_', column = _etta_e_g_, name = "КПД генератора, -", format = "%f", ke = 'count23')


            st.write('t_a = ',t_a_, '; ','P_a = ',P_a_, '; ','etta_is_k = ',etta_is_k_, '; ', 't_c = ',t_c_, '; ', 'epsilon = ',epsilon_, '; ', 'etta_is_t = ',etta_is_t_)  
            st.write('ele_power = ',ele_power_,'; ','pressure_loss = ',pressure_loss_,'; ', 'leak_rate = ',leak_rate_)
            st.write( 'etta_c_c = ',etta_c_c_,'; ', 'etta_mch = ',etta_mch_,'; ', 'etta_e_g = ',etta_e_g_)
            
            if st.form_submit_button('Расчет '):
                fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
                st.session_state.fuel = fuel
                schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                                    t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                                    etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                                    etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
                st.session_state.schemegtu = schemegtu

                st.pyplot(BraitonPlot(point_a = st.session_state.schemegtu[3], point_b_ = st.session_state.schemegtu[4], point_b = st.session_state.schemegtu[5],point_c = st.session_state.schemegtu[6], point_d_ = st.session_state.schemegtu[7], point_d = st.session_state.schemegtu[8]))
                st.header('Результаты расчета компрессора')
                st.table(data_1(st.session_state.schemegtu[0], method = 'compressor'))
                st.header('Результаты расчета турбины')
                st.table(data_1(st.session_state.schemegtu[1], method = 'turbine')) 
                st.header('Экономические показатели ГТУ')
                st.table(data_1(st.session_state.schemegtu[2], method = 'scheme')) 

            if st.form_submit_button('Сохранить расчеты в Excel'):
                fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
                st.session_state.fuel = fuel
                schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                                    t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                                    etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                                    etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
                st.session_state.schemegtu = schemegtu

                Save_to_file_stage(data_1(schemegtu[0], method = 'compressor'), name = 'SchemeGTU(compressor)', extension ='.xlsx')
                Save_to_file_stage(data_1(schemegtu[1], method = 'turbine'), name = 'SchemeGTU(turbine)', extension ='.xlsx')
                Save_to_file_stage(data_1(schemegtu[2], method = 'scheme'), name = 'SchemeGTU(not cold)', extension ='.xlsx')

    if select_1 ==  'Расчет схемы с охлаждением':
        st.session_state.count34 = 'cold'
        with st.form(key='my_form_3'):
            _t_a_, _P_a_,  _etta_is_k_= st.columns(3)
            _t_c_, _epsilon_, _etta_is_t_ = st.columns(3)
            _ele_power_, _pressure_loss_, _leak_rate_ = st.columns(3)
            _etta_c_c_, _etta_mch_, _etta_e_g_ =st.columns(3)
            _t_w_, _z_ = st.columns(2)
            t_a_ = count(counter = 't_a_', column = _t_a_, name = "Температура на входе в комп., ℃", format = "%f", ke = 'count12')
            P_a_ = count(counter = 'P_a_', column = _P_a_, name = "Давление на входе, Па", format = "%f", ke = 'count13')
            etta_is_k_ = count(counter = 'etta_is_k_', column = _etta_is_k_, name = "КПД компрессора, -", format = "%f", ke = 'count14')
            t_c_ = count(counter = 't_c_', column = _t_c_, name = "Температура на входе в турб., ℃", format = "%f", ke = 'count15')
            epsilon_ = count(counter = 'epsilon_', column = _epsilon_, name = "Степень сжатия в компрессоре, -", format = "%f", ke = 'count16')
            etta_is_t_ = count(counter = 'etta_is_t_', column = _etta_is_t_, name = "КПД турбины, -", format = "%f", ke = 'count17')  
            ele_power_ = count(counter = 'ele_power_', column = _ele_power_, name = "Электрическая мощность ГТУ, Вт", format = "%f", ke = 'count18')
            pressure_loss_ = count(counter = 'pressure_loss_', column = _pressure_loss_, name = "Коэффициент потерь давления, -", format = "%f", ke = 'count19')
            leak_rate_ = count(counter = 'leak_rate_', column = _leak_rate_, name = "Коэффициент утечек, -", format = "%f", ke = 'count20')
            etta_c_c_ = count(counter = 'etta_c_c_', column = _etta_c_c_, name = "Коэффициент теплоты топлива, -", format = "%f", ke = 'count21')
            etta_mch_ = count(counter = 'etta_mch_', column = _etta_mch_, name = "Механический КПД турбины, -", format = "%f", ke = 'count22')
            etta_e_g_ = count(counter = 'etta_e_g_', column = _etta_e_g_, name = "КПД генератора, -", format = "%f", ke = 'count23')
            t_w_ = count(counter = 't_w_', column = _t_w_, name = "Допустимая температура металла лопаток, ℃", format = "%f", ke = 'count24')
            z_ = count(counter = 'z_', column = _z_, name = "Число ступеней газовой турбины, шт", format = "%f", ke = 'count25')

            st.write('t_a = ',t_a_, '; ','P_a = ',P_a_, '; ','etta_is_k = ',etta_is_k_, '; ', 't_c = ',t_c_, '; ', 'epsilon = ',epsilon_, '; ', 'etta_is_t = ',etta_is_t_)  
            st.write('ele_power = ',ele_power_,'; ','pressure_loss = ',pressure_loss_,'; ', 'leak_rate = ',leak_rate_)
            st.write( 'etta_c_c = ',etta_c_c_,'; ', 'etta_mch = ',etta_mch_,'; ', 'etta_e_g = ',etta_e_g_)
            st.write( 't_w = ',t_w_,'; ', 'z = ',z_)
            
            if st.form_submit_button('Расчет '):
                fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
                st.session_state.fuel = fuel
                schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                                    t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                                    etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                                    etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
                st.session_state.schemegtu = schemegtu

                st.pyplot(BraitonPlot(point_a = st.session_state.schemegtu[3], point_b_ = st.session_state.schemegtu[4], point_b = st.session_state.schemegtu[5],point_c = st.session_state.schemegtu[6], point_d_ = st.session_state.schemegtu[7], point_d = st.session_state.schemegtu[8]))
                st.header('Результаты расчета компрессора')
                st.table(data_1(st.session_state.schemegtu[0], method = 'compressor'))
                st.header('Результаты расчета турбины')
                st.table(data_1(st.session_state.schemegtu[1], method = 'turbine')) 
                st.header('Экономические показатели ГТУ')
                st.table(data_1(st.session_state.schemegtu[2], method = 'schemecool')) 

            if st.form_submit_button('Сохранить расчеты в Excel'):
                fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
                st.session_state.fuel = fuel
                schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                                    t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                                    etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                                    etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
                st.session_state.schemegtu = schemegtu
                Save_to_file_stage(data_1(schemegtu[0], method = 'compressor'), name = 'SchemeGTU(compressor)', extension ='.xlsx')
                Save_to_file_stage(data_1(schemegtu[1], method = 'turbine'), name = 'SchemeGTU(turbine)', extension ='.xlsx')
                Save_to_file_stage(data_1(schemegtu[2], method = 'scheme'), name = 'SchemeGTU(cold)', extension ='.xlsx')

if Panel == "3. - Расчет геометрии ГТУ":
    st.title('Расчет геометрии ГТУ')
    st.header('Ввод исходных данных геометрии ГТУ')
    st.session_state.count33 = None
    st.session_state.geometrygtu = None
    with st.form(key='my_form_4'): 
        
        _K_s_, _K_r_, _radial_clearance_ = st.columns(3)
        _D_sr__h_2_z_, _number_of_steps_ = st.columns(2)
        _axial_speed_input_, _axial_speed_outlet_ = st.columns(2)

        K_s_ = count(counter = 'K_s_', column = _K_s_, name = "Коэффициент зазора сопловой, -", format = "%f", ke = 'count26')
        K_r_ = count(counter = 'K_r_', column = _K_r_, name = "Коэффициент зазора рабочей, -", format = "%f", ke = 'count27')
        radial_clearance_ = count(counter = 'radial_clearance_', column = _radial_clearance_, name = "Радиальный зазор ступени, м", format = "%f", ke = 'count28')
        D_sr__h_2_z_ = count(counter = 'D_sr__h_2_z_', column = _D_sr__h_2_z_, name = "Относительная высота лопатки последней ступени, -", format = "%f", ke = 'count29')
        number_of_steps_ = count(counter = 'number_of_steps_', column = _number_of_steps_, name = "Колличество ступеней в турбине, -", format = "%g", ke = 'count30')
        axial_speed_input_ = count(counter = 'axial_speed_input_', column = _axial_speed_input_, name = "Окружная скорость на входе в турбину, м/c", format = "%f", ke = 'count31')
        axial_speed_outlet_ = count(counter = 'axial_speed_outlet_', column = _axial_speed_outlet_, name = "Окружная скорость на выходе из турбины, м/c", format = "%f", ke = 'count32')
        st.write('K_s = ',K_s_, '; ','K_r = ',K_r_, '; ','radial_clearance = ',radial_clearance_,'; ','D_sr__h_2_z = ',D_sr__h_2_z_, '; ', 'n= ',number_of_steps_)  
        st.write('speed_input = ',axial_speed_input_,'; ', 'speed_outlet_ = ',axial_speed_outlet_,)
        
        type_1 = st.radio('Выберите тип геометрии ГТУ:', ('Dк = const','Dср = const','Dп = const'))

        if type_1 == 'Dк = const':
            st.session_state.count33 = 'root'
        
        if type_1 == 'Dср = const':
            st.session_state.count33 = 'medium'

        if type_1 == 'Dп = const':
            st.session_state.count33 = 'top'

        if st.form_submit_button('Расчет  '):
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
            st.session_state.fuel = fuel
            schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                        t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                        etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                        etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
            st.session_state.schemegtu = schemegtu            
            geometrygtu = geometry(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, number_of_steps = int(st.session_state.number_of_steps_), axial_speed_input = st.session_state.axial_speed_input_,
                axial_speed_outlet = st.session_state.axial_speed_outlet_,D_sr__h_2_z = st.session_state.D_sr__h_2_z_, 
                K_s = st.session_state.K_s_, K_r = st.session_state.K_r_, radial_clearance = st.session_state.radial_clearance_, method = st.session_state.count33)
            st.session_state.geometrygtu = geometrygtu

            st.pyplot(flow_pathPlot(st.session_state.geometrygtu))
            st.header('Введенные параметеры')
            st.table(data_2(st.session_state.geometrygtu[0], method = 'inlet'))
            st.header('Геометрия проточной части')
            st.table(data_2(st.session_state.geometrygtu[1], method = 'geometry')) 
            st.header('Разбивка проточной части')
            st.table(data_2(st.session_state.geometrygtu[3], method = 'geometrystep')) 

        if st.form_submit_button('Сохранить расчеты в Excel'):
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
            st.session_state.fuel = fuel
            schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                        t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                        etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                        etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
            st.session_state.schemegtu = schemegtu
            geometrygtu = geometry(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, number_of_steps = int(st.session_state.number_of_steps_), axial_speed_input = st.session_state.axial_speed_input_,
            axial_speed_outlet = st.session_state.axial_speed_outlet_,D_sr__h_2_z = st.session_state.D_sr__h_2_z_, 
            K_s = st.session_state.K_s_, K_r = st.session_state.K_r_, radial_clearance = st.session_state.radial_clearance_, method = st.session_state.count33)
            st.session_state.geometrygtu = geometrygtu    
            Save_to_file_stage(data_2(st.session_state.geometrygtu[0], method = 'inlet'), name = 'GeometryGTU(Inlet)', extension ='.xlsx')
            Save_to_file_stage(data_2(st.session_state.geometrygtu[1], method = 'geometry'), name = 'GeometryGTU(Geometry)', extension ='.xlsx')
            Save_to_file_stage(data_2(st.session_state.geometrygtu[3], method = 'geometrystep'), name = 'GeometryGTU(GeometryStep)', extension ='.xlsx')

if Panel == "4. - Расчет параметров по ступеням":
    st.title('Расчет параметров i - ой ступени ГТУ')
    st.header('Ввод исходных данных i-ой ступени ГТУ')
    st.session_state.parametergtu = None
    st.session_state.ro_ = 0.0
    st.session_state.alpha_ = 0.0
    st.session_state.deltaH_ = 0.0 
    
    with st.form(key='my_form_5'): 
        param = countRAH(int(st.session_state.number_of_steps_))
        st.session_state.ro_ = param[0]
        st.session_state.alpha_ = param[1]
        st.session_state.deltaH_ = param[2]
        _periodicity_, _, = st.columns(2)
        periodicity_ = count(counter = 'periodicity_', column = _periodicity_, name = "Частота вращения ротора, 1/c", format = "%f", ke = 'count35')

        if st.form_submit_button('Расчет   '):
            st.image(Image.open('B:\Postgraduate studies\ДИСЕРТАЦИЯ АСПИАРНТУРА\ProgrammGTU\Smith_diagram.png'))
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
            st.session_state.fuel = fuel
            schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                        t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                        etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                        etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
            st.session_state.schemegtu = schemegtu            
            geometrygtu = geometry(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, number_of_steps = int(st.session_state.number_of_steps_), axial_speed_input = st.session_state.axial_speed_input_,
                axial_speed_outlet = st.session_state.axial_speed_outlet_,D_sr__h_2_z = st.session_state.D_sr__h_2_z_, 
                K_s = st.session_state.K_s_, K_r = st.session_state.K_r_, radial_clearance = st.session_state.radial_clearance_, method = st.session_state.count33)
            st.session_state.geometrygtu = geometrygtu
            parametergtu = parameters(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, geom = st.session_state.geometrygtu, ro_st_i = st.session_state.ro_, alpha_02_i = st.session_state.alpha_, delta_H = st.session_state.deltaH_, periodicity = st.session_state.periodicity_)
            st.session_state.parametergtu = parametergtu            
            st.header('Основные кимематические параметры i-ой ступен')
            st.table(data_3(st.session_state.parametergtu[2], method = 'kinematics'))
            st.header('Основные термодинамические параметры i-ой ступен')
            st.table(data_3(st.session_state.parametergtu[3], method = 'termod'))
        
        if st.form_submit_button('Показать графики параметров '):
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
            st.session_state.fuel = fuel
            schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                        t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                        etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                        etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
            st.session_state.schemegtu = schemegtu            
            geometrygtu = geometry(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, number_of_steps = int(st.session_state.number_of_steps_), axial_speed_input = st.session_state.axial_speed_input_,
                axial_speed_outlet = st.session_state.axial_speed_outlet_,D_sr__h_2_z = st.session_state.D_sr__h_2_z_, 
                K_s = st.session_state.K_s_, K_r = st.session_state.K_r_, radial_clearance = st.session_state.radial_clearance_, method = st.session_state.count33)
            st.session_state.geometrygtu = geometrygtu
            parametergtu = parameters(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, geom = st.session_state.geometrygtu, ro_st_i = st.session_state.ro_, alpha_02_i = st.session_state.alpha_, delta_H = st.session_state.deltaH_, periodicity = st.session_state.periodicity_)
            st.session_state.parametergtu = parametergtu 
            st.pyplot(table2(st.session_state.parametergtu, 'ro'))
            st.pyplot(table2(st.session_state.parametergtu, 'alpha'))
            st.pyplot(table2(st.session_state.parametergtu, 'velocity'))
            st.pyplot(table2(st.session_state.parametergtu, 'temperature'))
            st.pyplot(table2(st.session_state.parametergtu, 'pressure'))
            st.pyplot(table2(st.session_state.parametergtu, 'etta'))
            st.pyplot(table2(st.session_state.parametergtu, 'heatdrop'))
        
        if st.form_submit_button('Сохранить расчеты в Excel'):
            fuel = gas(_H_2S = st.session_state.H_2S_, _CO_2 = st.session_state.CO_2_, _O_2 = st.session_state.O_2_, _CO = st.session_state.CO_, _H_2 = st.session_state.H_2_, _CH_2 = st.session_state.CH_2_, _CH_4 = st.session_state.CH_4_, _C_2H_4 = st.session_state.C_2H_4_, _C_2H_6 = st.session_state.C_2H_6_, _C_3H_8 = st.session_state.C_3H_8_, _C_4H_10 = st.session_state.C_4H_10_, temperature_C = temperature_Cels)
            st.session_state.fuel = fuel
            schemegtu = scheme(fuel = st.session_state.fuel, ele_power = st.session_state.ele_power_, t_c = st.session_state.t_c_,
                        t_a = st.session_state.t_a_, P_a = st.session_state.P_a_, epsilon = st.session_state.epsilon_, coefficient_pressure_loss = st.session_state.pressure_loss_,
                        etta_c_c = st.session_state.etta_c_c_, etta_mch = st.session_state.etta_mch_, etta_e_g = st.session_state.etta_e_g_,
                        etta_is_t = st.session_state.etta_is_t_, etta_is_k = st.session_state.etta_is_k_, leak_rate = st.session_state.leak_rate_, t_w = st.session_state.t_w_, z = st.session_state.z_, method = st.session_state.count34)
            st.session_state.schemegtu = schemegtu
            geometrygtu = geometry(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, number_of_steps = int(st.session_state.number_of_steps_), axial_speed_input = st.session_state.axial_speed_input_,
            axial_speed_outlet = st.session_state.axial_speed_outlet_,D_sr__h_2_z = st.session_state.D_sr__h_2_z_, 
            K_s = st.session_state.K_s_, K_r = st.session_state.K_r_, radial_clearance = st.session_state.radial_clearance_, method = st.session_state.count33)
            st.session_state.geometrygtu = geometrygtu    
            parametergtu = parameters(fuel = st.session_state.fuel, sch = st.session_state.schemegtu, geom = st.session_state.geometrygtu, ro_st_i = st.session_state.ro_, alpha_02_i = st.session_state.alpha_, delta_H = st.session_state.deltaH_, periodicity = st.session_state.periodicity_)
            st.session_state.parametergtu = parametergtu            

            Save_to_file_stage(data_3(st.session_state.parametergtu[2], method = 'kinematics'), name = 'ParameterGTU(kinematics)', extension ='.xlsx')
            Save_to_file_stage(data_3(st.session_state.parametergtu[3], method = 'termod'), name = 'ParameterGTU(termod)', extension ='.xlsx')
