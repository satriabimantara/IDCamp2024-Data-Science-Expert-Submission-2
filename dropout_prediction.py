import pickle
from pandas import DataFrame
import streamlit as st

# load pretrained best model
best_pipeline = pickle.load(open('best_model.pkl', 'rb'))['model']


# Title
st.title("Dropout Prediction App (Prototipe) using Machine Learning")

data = {'Marital_status': 'Single',
        'Application_mode': '2nd phase - general contingent',
        'Application_order': 'Sixth Order',
        'Course': 'Animation and Multimedia Design',
        'Daytime_evening_attendance': 'Daytime',
        'Previous_qualification': 'Secondary education',
        'Previous_qualification_grade': 122.0,
        'Nacionality': 'Portuguese',
        'Mothers_qualification': 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
        'Fathers_qualification': 'Other - 11th Year of Schooling',
        'Mothers_occupation': 'Personal Services, Security and Safety Workers and Sellers',
        'Fathers_occupation': 'Unskilled Workers',
        'Admission_grade': 127.3,
        'Displaced': 'Yes',
        'Educational_special_needs': 'No',
        'Debtor': 'No',
        'Tuition_fees_up_to_date': 'Yes',
        'Gender': 'Yes',
        'Scholarship_holder': 'No',
        'Age_at_enrollment': 20,
        'International': 'No',
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 8,
        'Curricular_units_1st_sem_approved': 5,
        'Curricular_units_1st_sem_grade': 11.8,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 8,
        'Curricular_units_2nd_sem_approved': 5,
        'Curricular_units_2nd_sem_grade': 11.6,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 10.8,
        'Inflation_rate': 1.4,
        'GDP': 1.74,
        }

# Komponen pertama: Academic Performance
with st.container():
    st.header("Student's Academic Performance", divider="gray")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Curricular units 1st semester")
        X1 = int(st.number_input("Credited", max_value=20, min_value=0,
                 key='X1', value=data['Curricular_units_1st_sem_credited']))
        data['Curricular_units_1st_sem_credited'] = X1

        X2 = int(st.number_input("Enrolled", max_value=26, min_value=0,
                 key='X2', value=data['Curricular_units_1st_sem_enrolled']))
        data['Curricular_units_1st_sem_enrolled'] = X2

        X3 = int(st.number_input("Evaluations",
                 max_value=45, min_value=0, key='X3', value=data['Curricular_units_1st_sem_evaluations']))
        data['Curricular_units_1st_sem_evaluations'] = X3

        X4 = int(st.number_input("Approved", max_value=26, min_value=0,
                 key='X4', value=data['Curricular_units_1st_sem_approved']))
        data['Curricular_units_1st_sem_approved'] = X4

        X5 = float(st.number_input(
            "Grade", max_value=18.75, min_value=0.0, key='X5', value=data['Curricular_units_1st_sem_grade']))
        data['Curricular_units_1st_sem_grade'] = X5

        X6 = int(st.number_input(
            "Without Evaluations", max_value=12, min_value=0, key='X6', value=data['Curricular_units_1st_sem_without_evaluations']))
        data['Curricular_units_1st_sem_without_evaluations'] = X6
    with col2:
        st.subheader("Curricular units 2nd semester")
        X7 = int(st.number_input("Credited", max_value=19, min_value=0,
                 key='X7', value=data['Curricular_units_2nd_sem_credited']))
        data['Curricular_units_2nd_sem_credited'] = X7

        X8 = int(st.number_input("Enrolled", max_value=23, min_value=0,
                 key='X8', value=data['Curricular_units_2nd_sem_enrolled']))
        data['Curricular_units_2nd_sem_enrolled'] = X8

        X9 = int(st.number_input("Evaluations",
                 max_value=33, min_value=0, key='X9', value=data['Curricular_units_2nd_sem_evaluations']))
        data['Curricular_units_2nd_sem_evaluations'] = X9

        X10 = int(st.number_input(
            "Approved", max_value=20, min_value=0, key='X10', value=data['Curricular_units_2nd_sem_approved']))
        data['Curricular_units_2nd_sem_approved'] = X10

        X11 = float(st.number_input(
            "Grade", max_value=18.571429, min_value=0.0, key='X11', value=data['Curricular_units_2nd_sem_grade']))
        data['Curricular_units_2nd_sem_grade'] = X11

        X12 = int(st.number_input(
            "Without Evaluations", max_value=12, min_value=0, key='X12', value=data['Curricular_units_2nd_sem_without_evaluations']))
        data['Curricular_units_2nd_sem_without_evaluations'] = X12


# Komponen kedua: Demographics
with st.container():
    st.header("Student's Demographics", divider="gray")
    col1, col2 = st.columns([3, 1])
    with col1:
        X13 = st.selectbox(
            "Nacionality",
            ('Portuguese',
             'Brazilian',
             'Santomean',
             'Cape Verdean',
             'Spanish',
             'Guinean',
             'Ukrainian',
             'Moldova (Republic of)',
             'Italian',
             'Russian',
             'Romanian',
             'Mozambican',
             'Angolan',
             'Mexican',
             'German',
             'English',
             'Dutch',
             'Cuban',
             'Colombian',
             'Turkish',
             'Lithuanian'),
        )
        data['Nacionality'] = X13
    with col2:
        X14 = st.selectbox(
            'International',
            ('Yes', 'No')
        )
        data['International'] = X14

# Komponen ketiga: Socio-economic factors
with st.container():
    st.header("Socio-economic factors", divider="gray")
    X15 = st.selectbox(
        'Tuition fees up to date',
        ('Yes', 'No')
    )
    data['Tuition_fees_up_to_date'] = X15

    col2, col3, col4 = st.columns([3, 3, 3])
    with col2:
        X16 = float(st.number_input(
            "Unemployment rate", max_value=16.20, min_value=7.6, key='X16'))
        data['Unemployment_rate'] = X16
    with col3:
        X17 = float(st.number_input(
            "Inflation rate", max_value=3.7, min_value=-0.8, key='X17'))
        data['Inflation_rate'] = X17
    with col4:
        X18 = float(st.number_input(
            "Inflation rate", max_value=3.51, min_value=-4.06, key='X18'))
        data['GDP'] = X18

# Komponen keempat: family backgrounds
with st.container():
    st.header("Family backgrounds", divider="gray")
    col1, col2 = st.columns([6, 6])
    with col1:
        X19 = st.selectbox(
            "Mother Qualification", ('Secondary Education - 12th Year of Schooling or Eq.',
                                     'Basic education 1st cycle (4th/5th year) or equiv.',
                                     'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
                                     'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
                                     'Higher Education - Degree',
                                     'Unknown',
                                     "Higher Education - Bachelor's Degree",
                                     "Higher Education - Master's",
                                     'Other - 11th Year of Schooling',
                                     'Higher Education - Doctorate',
                                     'Higher education - degree (1st cycle)',
                                     'Technological specialization course',
                                     '12th Year of Schooling - Not Completed',
                                     'Specialized higher studies course',
                                     'Professional higher technical course',
                                     'Frequency of Higher Education',
                                     'Higher Education - Master (2nd cycle)',
                                     '9th Year of Schooling - Not Completed',
                                     '8th year of schooling',
                                     "Can't read or write",
                                     '11th Year of Schooling - Not Completed',
                                     '7th Year (Old)',
                                     'Can read without having a 4th year of schooling',
                                     '10th Year of Schooling',
                                     'Higher Education - Doctorate (3rd cycle)',
                                     '7th year of schooling',
                                     'Technical-professional course',
                                     '2nd cycle of the general high school course',
                                     'General commerce course'))
        data['Mothers_qualification'] = X19
    with col2:
        X20 = st.selectbox(
            "Mother Occupation", ('Unskilled Workers',
                                  'Administrative staff',
                                  'Personal Services, Security and Safety Workers and Sellers',
                                  'Intermediate Level Technicians and Professions',
                                  'Specialists in Intellectual and Scientific Activities',
                                  'Skilled Workers in Industry, Construction and Craftsmen',
                                  'Student',
                                  'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
                                  'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
                                  'Other Situation',
                                  'Installation and Machine Operators and Assembly Workers',
                                  'Cleaning workers',
                                  '(blank)',
                                  'Meal preparation assistants',
                                  'Office workers, secretaries in general and data processing operators',
                                  'Teachers',
                                  'Other administrative support staff',
                                  'Unskilled workers in agriculture, animal production, fisheries and forestry',
                                  'Workers in food processing, woodworking, clothing and other industries and crafts',
                                  'Intermediate level technicians from legal, social, sports, cultural and similar services',
                                  'Armed Forces Professions',
                                  'Unskilled workers in extractive industry, construction, manufacturing and transport',
                                  'Personal service workers',
                                  'Technicians and professionals, of intermediate level of health',
                                  'Data, accounting, statistical, financial services and registry-related operators',
                                  'Sellers',
                                  'Health professionals',
                                  'Personal care workers and the like',
                                  'Skilled construction workers and the like, except electricians',
                                  'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
                                  'Specialists in information and communication technologies (ICT)',
                                  'Intermediate level science and engineering technicians and professions'))
        data['Mothers_occupation'] = X20

    col3, col4 = st.columns([6, 6])
    with col3:
        X21 = st.selectbox(
            "Father Qualification", ('Basic education 1st cycle (4th/5th year) or equiv.',
                                     'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
                                     'Secondary Education - 12th Year of Schooling or Eq.',
                                     'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
                                     'Higher Education - Degree',
                                     'Unknown',
                                     "Higher Education - Bachelor's Degree",
                                     "Higher Education - Master's",
                                     'Other - 11th Year of Schooling',
                                     'Technological specialization course',
                                     'Higher Education - Doctorate',
                                     '7th Year (Old)',
                                     'Can read without having a 4th year of schooling',
                                     '12th Year of Schooling - Not Completed',
                                     'Higher education - degree (1st cycle)',
                                     'Technical-professional course',
                                     '10th Year of Schooling',
                                     '8th year of schooling',
                                     '9th Year of Schooling - Not Completed',
                                     'Higher Education - Master (2nd cycle)',
                                     'Specialized higher studies course',
                                     '7th year of schooling',
                                     "Can't read or write",
                                     '11th Year of Schooling - Not Completed',
                                     'Frequency of Higher Education',
                                     'Higher Education - Doctorate (3rd cycle)',
                                     'General commerce course',
                                     'Complementary High School Course',
                                     'Professional higher technical course',
                                     'Complementary High School Course - not concluded',
                                     'Supplementary Accounting and Administration',
                                     '2nd year complementary high school course',
                                     '2nd cycle of the general high school course',
                                     'General Course of Administration and Commerce'))
        data['Fathers_qualification'] = X21
    with col4:
        X22 = st.selectbox(
            "Father Occupation", ('Unskilled Workers',
                                  'Skilled Workers in Industry, Construction and Craftsmen',
                                  'Personal Services, Security and Safety Workers and Sellers',
                                  'Administrative staff',
                                  'Intermediate Level Technicians and Professions',
                                  'Installation and Machine Operators and Assembly Workers',
                                  'Armed Forces Professions',
                                  'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
                                  'Specialists in Intellectual and Scientific Activities',
                                  'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
                                  'Student',
                                  'Other Situation',
                                  '(blank)',
                                  'Unskilled workers in extractive industry, construction, manufacturing and transport',
                                  'Skilled construction workers and the like, except electricians',
                                  'Other administrative support staff',
                                  'Unskilled workers in agriculture, animal production, fisheries and forestry',
                                  'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
                                  'Workers in food processing, woodworking, clothing and other industries and crafts',
                                  'Other Armed Forces personnel',
                                  'Fixed plant and machine operators',
                                  'Vehicle drivers and mobile equipment operators',
                                  'Information and communication technology technicians',
                                  'Teachers',
                                  'Sellers',
                                  'Armed Forces Sergeants',
                                  'Assembly workers',
                                  'Skilled workers in metallurgy, metalworking and similar',
                                  'Directors of administrative and commercial services',
                                  'Health professionals',
                                  'Meal preparation assistants',
                                  'Personal service workers',
                                  'Protection and security services personnel',
                                  'Market-oriented farmers and skilled agricultural and animal production workers',
                                  'Armed Forces Officers',
                                  'Office workers, secretaries in general and data processing operators',
                                  'Technicians and professionals, of intermediate level of health',
                                  'Hotel, catering, trade and other services directors',
                                  'Street vendors (except food) and street service providers',
                                  'Specialists in the physical sciences, mathematics, engineering and related techniques',
                                  'Specialists in finance, accounting, administrative organization, public and commercial relations',
                                  'Data, accounting, statistical, financial services and registry-related operators',
                                  'Personal care workers and the like',
                                  'Skilled workers in electricity and electronics',
                                  'Intermediate level technicians from legal, social, sports, cultural and similar services',
                                  'Intermediate level science and engineering technicians and professions'))
        data['Fathers_occupation'] = X22

# Komponen kelima: backgrounds
with st.container():
    st.header("Student's backgrounds", divider="gray")
    col1, col2 = st.columns([6, 6])
    with col1:
        X23 = st.selectbox('Previous Qualification', ('Secondary education',
                                                      'Technological specialization course',
                                                      'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
                                                      'Higher education - degree',
                                                      'Other - 11th year of schooling',
                                                      'Higher education - degree (1st cycle)',
                                                      'Professional higher technical course',
                                                      "Higher education - bachelor's degree",
                                                      'Frequency of higher education',
                                                      '12th year of schooling - not completed',
                                                      "Higher education - master's",
                                                      'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
                                                      'Higher education - master (2nd cycle)',
                                                      '11th year of schooling - not completed',
                                                      '10th year of schooling - not completed',
                                                      'Higher education - doctorate',
                                                      '10th year of schooling'))
        data['Previous_qualification'] = X23
    with col2:
        X24 = float(st.number_input('Previous qualification grade',
                    max_value=190.0, min_value=95.0, key='X24'))
        data['Previous_qualification_grade'] = X24

    col3, col4 = st.columns([4, 1])
    with col3:
        X25 = float(st.number_input('Admission grade',
                    max_value=190.0, min_value=95.0, key='X25'))
        data['Admission_grade'] = X25
    with col4:
        X26 = st.selectbox('Scholarship holder', ('Yes', 'No'))
        data['Scholarship_holder'] = X26

# Komponen keenam: personal informations
with st.container():
    st.header("Student's personal information", divider='gray')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        X27 = st.selectbox('Marital Status', ('Yes', 'No'))
        data['Marital_status'] = X27
    with col2:
        X28 = st.selectbox('Displaced', ('Yes', 'No'))
        data['Displaced'] = X28
    with col3:
        X29 = st.selectbox('Educational Special Needs', ('Yes', 'No'))
        data['Educational_special_needs'] = X29
    with col4:
        X30 = st.selectbox('Debtor', ('Yes', 'No'))
        data['Debtor'] = X30

    col5, col6 = st.columns([6, 6])
    with col5:
        X31 = int(st.number_input('Age at enrollment',
                  max_value=70, min_value=17, key='X31'))
        data['Age_at_enrollment'] = X31
    with col6:
        X32 = st.selectbox('Gender', ('Male', 'Female'))
        data['Gender'] = X32

# Komponen ketujuh: application (academic path)
with st.container():
    st.header('Application (academic path)', divider="gray")
    col1, col2 = st.columns([6, 6])
    with col1:
        X33 = st.selectbox('Application Mode', ('2nd phase - general contingent',
                                                'International student (bachelor)',
                                                '1st phase - general contingent',
                                                'Over 23 years old',
                                                '3rd phase - general contingent',
                                                'Short cycle diploma holders',
                                                'Technological specialization diploma holders',
                                                'Change of institution/course',
                                                'Change of course',
                                                'Holders of other higher courses',
                                                'Transfer',
                                                '1st phase - special contingent (Madeira Island)',
                                                '1st phase - special contingent (Azores Island)',
                                                'Ordinance No. 612/93',
                                                'Ordinance No. 854-B/99',
                                                'Change of institution/course (International)',
                                                'Ordinance No. 533-A/99, item b2) (Different Plan)',
                                                'Ordinance No. 533-A/99, item b3 (Other Institution)'))
        data['Application_mode'] = X33
    with col2:
        X34 = st.selectbox('Application Order', ('Sixth Order',
                                                 'Second Order',
                                                 'Third Order',
                                                 'Fifth Order',
                                                 'Fourth Order',
                                                 'Seventh Order',
                                                 'Tenth Order',
                                                 'First Order'))
        data['Application_order'] = X34

    col3, col4 = st.columns([6, 6])
    with col3:
        X35 = st.selectbox('Course', ('Animation and Multimedia Design',
                                      'Tourism',
                                      'Communication Design',
                                      'Journalism and Communication',
                                      'Social Service (evening attendance)',
                                      'Management (evening attendance)',
                                      'Nursing',
                                      'Social Service',
                                      'Advertising and Marketing Management',
                                      'Basic Education',
                                      'Veterinary Nursing',
                                      'Equinculture',
                                      'Oral Hygiene',
                                      'Management',
                                      'Agronomy',
                                      'Biofuel Production Technologies',
                                      'Informatics Engineering'))
        data['Course'] = X35
    with col4:
        X36 = st.selectbox('Daytime/evening attendance',
                           ('Daytime', 'Evening'))
        data['Daytime_evening_attendance'] = X36

with st.container():
    if st.button('Predict', type='primary'):
        X_new_data = DataFrame([data])

        with st.expander("View the Inputted Data"):
            st.dataframe(data=X_new_data, width=800, height=10)

        # predict using pipeline
        y_pred = best_pipeline.predict(X_new_data)[0]

        # print predicted results
        st.write("Prediction: {}".format(y_pred))
