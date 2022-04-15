import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import base64

def load_uu(data):
    df = pd.read_csv(data)
    return df

def show_passage(a):
        df = a
        pasal_list = df['PASAL'].unique().tolist()
        pasal_name = st.sidebar.selectbox('PASAL',pasal_list)
        ayat = st.sidebar.number_input('AYAT',1)
        bible_df = df[df['PASAL']== pasal_name]
        #st.dataframe(bible_df)
        try:
            selected_passage = bible_df[(bible_df['PASAL'] == pasal_name) & (bible_df['AYAT'] == ayat) ]
            #st.write(selected_passage)   
            passage_detail =" Pasal: {} Ayat: {}".format(pasal_name,ayat)
            st.code(passage_detail)             
            passage = "{} ".format(selected_passage['ISI'].values[0])
            passage1 = "{} ".format(selected_passage['ISI1'].values[0])
            passage2 = "{} ".format(selected_passage['ISI2'].values[0])
            passage3 = "{} ".format(selected_passage['ISI3'].values[0])
            passage4 = "{} ".format(selected_passage['ISI4'].values[0])
            passage5 = "{} ".format(selected_passage['ISI5'].values[0])
            passage6 = "{} ".format(selected_passage['ISI6'].values[0])
            passage7 = "{} ".format(selected_passage['ISI7'].values[0])
            passage8 = "{} ".format(selected_passage['ISI8'].values[0])
            passage9 = "{} ".format(selected_passage['ISI9'].values[0])
            collect_passage ="{} \n {} \n {}\n {} \n {} \n {} \n {}\n {} \n {}".format(passage,passage1,passage2,passage3,passage4,passage5,passage6,passage7,passage8,passage9)
            st.info(collect_passage)   

        except:
            st.warning('Book is out of range')

def show_pdf(file_path):
     with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    
    st.title("Kementrian Perdagangan")
    menu = ['HOME','DASAR HUKUM','Glosary','Search','About'] 
    choice = st.sidebar.selectbox('Menu',menu)
    
    if choice == 'HOME' :
        st.subheader('Create by Ignatius Arga')
        st.text('Ignatius.arga@gmail.com')

    elif choice == 'DASAR HUKUM':
        dh_menu = ['UU no 7 Th 2014','UU no 11 Th 2021','PP no 5 Th 2021','PP no 29 Th 2021','PERMENDAG 26 Th 2021','PERMENDAG 36 th 2018','PERMENDAG 92 th 2020']
        subchoice = st.sidebar.selectbox('UU,PP, Permendag',dh_menu)
        if subchoice == 'UU no 7 Th 2014':
            st.caption('UU no 7 Th 2014')
            directory = r'pdf_files/UU Nomor 07 Tahun 2014.pdf'
            show_pdf(directory)

        elif subchoice == 'UU no 11 Th 2021':
            st.caption('UU no 11 Th 2021')
            directory = r'pdf_files/UU Nomor 11 Tahun 2020.pdf'
            show_pdf(directory)
        
        elif subchoice == 'PP no 5 Th 2021':
            st.caption('PP no 5 Th 2021')
            directory = r'pdf_files/PP Nomor 5 Tahun 2021.pdf'
            show_pdf(directory)

        elif subchoice == 'PP no 29 Th 2021':
            st.caption('PP no 29 Th 2021')
            directory = r'pdf_files/PP Nomor 29 Tahun 2021.pdf'
            show_pdf(directory)

        elif subchoice == 'PERMENDAG 26 Th 2021':
            st.caption('PERMENDAG 26 Tahun 2021')
            directory = r'pdf_files/Permendag 26 Tahun 2021.pdf'
            show_pdf(directory)

        elif subchoice == 'PERMENDAG 36 th 2018':
            st.caption('PERMENDAG 36 th 2018')
            directory = r'pdf_files/Permendag 36 Tahun 2018.pdf'
            show_pdf(directory)

        elif subchoice == 'PERMENDAG 92 th 2020':
            st.caption('PERMENDAG 92 th 2020')
            directory = r'pdf_files/Permendag 92 Tahun 2020.pdf'
            show_pdf(directory)
        else :
            st.subheader('Create by Ignatius Arga')
            st.text('Ignatius.arga@gmail.com')

    elif choice =='Glosary':
        st.subheader("Glosary")  
        df = load_uu('data/glosary2.csv')
        kitab_list = df['Glosary'].unique().tolist()
        kitab_name = st.sidebar.selectbox('Glosary',kitab_list)
        bible_df = df[df['Glosary']== kitab_name]
        dasar_list = df['Dasar'].unique().tolist()
        dasar = st.sidebar.selectbox('Dasar',dasar_list)
            #st.dataframe(bible_df)
        try:
            passage_detail ="{} ".format(dasar)
            st.code(passage_detail)
            selected_passage = bible_df[(bible_df['Glosary'] == kitab_name) & (bible_df['Dasar'] ==dasar) ]
                #st.write(selected_passage)  
            passage = "{} ".format(selected_passage['ISI'].values[0])
            st.info(passage)           
        except:
            st.warning('Book is out of range')

    elif choice =='Search':
        st.subheader("Search Pasal")
        sc_menu = ['PERMENDAG 18 th 2019','PERMENDAG 92 th 2020']
        subchoice = st.sidebar.selectbox('UU,PP, Permendag',sc_menu)
        if subchoice  == 'PERMENDAG 18 th 2019':
            df = load_uu('data/Perdag 18 th 2019.csv')
            st.subheader("PERMENDAG 18 th 2019")
            st.caption("METODE PENGUJIAN, TATA CARA PENDAFTARAN, PENGAWASAN, PENGHENTIAN KEGIATAN PERDAGANGAN DAN PENARIKAN BARANG TERKAIT DENGAN KEAMANAN, KESELAMATAN, KESEHATAN, DAN LINGKUNGAN HIDUP")
            show_passage(df)
            
        elif subchoice  == 'PERMENDAG 92 th 2020':
            df = load_uu('data/Perdag 92 th 2020.csv')
            st.subheader("PERMENDAG 92 th 2020")
            st.caption("PERATURAN MENTERI PERDAGANGAN TENTANG PERDAGANGAN ANTARPULAU.")
            show_passage(df)
        
       
    else :
        st.subheader('Create by Ignatius Arga')
        st.text('Ignatius.arga@gmail.com')


if __name__ == '__main__' :
    main()