from turtle import pd
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd

def load_uu(data):
    df = pd.read_csv(data)
    return df

def main():
    
    st.title("Kementrian Perdagangan")
    menu = ['HOME','PERMENDAG 18 th 2019','PERMENDAG 92 th 2020','Glosary','Search','About']
    
   
    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'PERMENDAG 18 th 2019':
        df = load_uu('data/Perdag 18 th 2019.csv')
        st.subheader("PERMENDAG 18 th 2019")
        st.caption("METODE PENGUJIAN, TATA CARA PENDAFTARAN, PENGAWASAN, PENGHENTIAN KEGIATAN PERDAGANGAN DAN PENARIKAN BARANG TERKAIT DENGAN KEAMANAN, KESELAMATAN, KESEHATAN, DAN LINGKUNGAN HIDUP")
        kitab_list = df['BAB'].unique().tolist()
        kitab_name = st.sidebar.selectbox('BAB',kitab_list)
        pasal = st.sidebar.number_input('Pasal',1)
        ayat = st.sidebar.number_input('Ayat',1)
        bible_df = df[df['BAB']== kitab_name]
        #st.dataframe(bible_df)
        try:
            selected_passage = bible_df[(bible_df['PASAL'] == pasal) & (bible_df['AYAT'] == ayat) ]
            #st.write(selected_passage)   
            passage_detail =" Pasal: {} Ayat: {}".format(pasal,ayat)
            st.code(passage_detail)         
            passage = "{} ".format(selected_passage['ISI'].values[0])
            st.info(passage)           
        except:
            st.warning('Book is out of range')
        
    elif choice == 'PERMENDAG 92 th 2020':
        df = load_uu('data/Perdag 92 th 2020.csv')
        st.subheader("PERMENDAG 92 th 2020")
        st.caption("PERATURAN MENTERI PERDAGANGAN TENTANG PERDAGANGAN ANTARPULAU.")
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
            st.info(passage)           
        except:
            st.warning('Book is out of range')     


    elif choice =='Glosary':
        st.subheader("Glosary")  
        df = load_uu('data/glosary2.csv')
        kitab_list = df['Glosary'].unique().tolist()
        kitab_name = st.sidebar.selectbox('Glosary',kitab_list)
        bible_df = df[df['Glosary']== kitab_name]
        dasar_list = df['Dasar'].unique().tolist()
        dasar_name = st.sidebar.selectbox('Dasar',dasar_list)
        dasar_df = df[df['Dasar']== dasar_name]
        #st.dataframe(bible_df)
        try:
            passage_detail ="{} {} ".format(dasar_df['Dasar'].values[0])
            st.code(passage_detail)
            selected_passage = bible_df[(bible_df['Glosary'] == kitab_name) & (dasar_df['Dasar'] ==dasar_name) ]
            #st.write(selected_passage)  
            passage = "{} ".format(selected_passage['ISI'].values[0])
            st.info(passage)           
        except:
            st.warning('Book is out of range')

    elif choice =='Search':
        st.subheader("Search Pasal")
        
       
    else :
        st.subheader('Create by Ignatius Arga')
        st.text('Ignatius.arga@gmail.com')


if __name__ == '__main__' :
    main()
