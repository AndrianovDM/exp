import streamlit as st

def count(counter, column, name, format, ke):
    if counter not in st.session_state:
        st.session_state[counter] = 0.00
    val = column.number_input((name), format = format, value = st.session_state[counter], key = ke)
    if val:
        st.session_state[counter] = st.session_state[ke]
    return st.session_state[counter]

# def ro_count(num):
#     ro_index = [] 
#     ro = []
#     for i in range(num):
#         ro_index.append(f'Ro_{i}')
#     ro_index = st.columns(num)
#     for i in range(num):
#         ro.append(count(counter = f'Ro{i}', column = ro_index[i], name = f"ro_{i}, -", format = "%f", ke = f'ro{i}'))
#     return ro

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
                                                "2. - Расчет схемы ГТУ"])
if Panel == "1. - Расчет состава топлива":
    with st.form(key='my_form_1'):
    #     # [_CO_, _H_2_, _CH_2_] = st.columns(3)
    #     # CO_ = count(counter = 'CO_', column = _CO_, name = "CO, %", format = "%f", ke = 'count4')
    #     # H_2_ = count(counter = 'H_2_', column = _H_2_, name = "H_2, %", format = "%f", ke = 'count5')
    #     # CH_2_ = count(counter = 'CH_2_', column = _CH_2_, name = "CH_2, %", format = "%f", ke = 'count6')
        count = countRAH(5)
        st.session_state.ro = 0.0
        st.session_state.alpha = 0.0
        st.session_state.deltaH = 0.0
        if st.form_submit_button('Расчет'):
            st.session_state.ro = count[0]
            st.session_state.alpha = count[1]
            st.session_state.deltaH = count[2]
            st.write(st.session_state.ro, st.session_state.alpha, st.session_state.deltaH)

if Panel == "2. - Расчет схемы ГТУ":
    with st.form(key='my_form_2'):
        if st.form_submit_button('Расчет'):
            st.write(st.session_state.ro, st.session_state.alpha, st.session_state.deltaH)



# print(ro_count(4))