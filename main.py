import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import base64
from streamlit.components.v1 import html
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
     page_title="Ignatius Arga",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )


@st.cache 
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

def dasar_hukum() : 
        dh_menu = ['UU no 7 Th 2014','UU no 11 Th 2021','PP no 5 Th 2021','PP no 29 Th 2021','PERMENDAG 26 Th 2021','PERMENDAG 36 th 2018','PERMENDAG 92 th 2020']
        subchoice = st.sidebar.selectbox('UU,PP, Permendag',dh_menu)
        show_menu = ["Album", "PDF file"]
        pdfshow = st.sidebar.selectbox('DISPLAY',show_menu)
        if subchoice == 'UU no 7 Th 2014':
            st.caption('UU no 7 Th 2014')
            directory = r'pdf_files/UU Nomor 07 Tahun 2014.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/3315e561bb.html",width=1000, height=1000, scrolling=False)

        elif subchoice == 'UU no 11 Th 2021':
            st.caption('UU no 11 Th 2021')
            directory = r'pdf_files/UU Nomor 11 Tahun 2020.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/e143529c1d.html",width=1000, height=1000, scrolling=False)
        
        elif subchoice == 'PP no 5 Th 2021':
            st.caption('PP no 5 Th 2021')
            directory = r'pdf_files/PP Nomor 5 Tahun 2021.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/e0ed383263.html",width=1000, height=1000, scrolling=False)

        elif subchoice == 'PP no 29 Th 2021':
            st.caption('PP no 29 Th 2021')
            directory = r'pdf_files/PP Nomor 29 Tahun 2021.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/48e53ccbd1.html",width=1000, height=1000, scrolling=False)

        elif subchoice == 'PERMENDAG 26 Th 2021':
            st.caption('PERMENDAG 26 Tahun 2021')
            directory = r'pdf_files/Permendag 26 Tahun 2021.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/1890e2d401.html",width=1000, height=1000, scrolling=False)
          

        elif subchoice == 'PERMENDAG 36 th 2018':
            st.caption('PERMENDAG 36 th 2018')
            directory = r'pdf_files/Permendag 36 Tahun 2018.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/100836d9b9.html",width=1000, height=1000, scrolling=False)

        elif subchoice == 'PERMENDAG 92 th 2020':
            st.caption('PERMENDAG 92 th 2020')
            directory = r'pdf_files/Permendag 92 Tahun 2020.pdf'
            if pdfshow == "PDF file" :
                show_pdf(directory)
            else :
                components.iframe("https://heyzine.com/flip-book/56e302d2a4.html",width=1000, height=1000, scrolling=False)
        else :
            st.subheader('Create by Ignatius Arga')
            st.text('Ignatius.arga@gmail.com')

def project():
        vesselfinder = """ 
                        var width="100%";         // width in pixels or percentage
                        var height="300";         // height in pixels
                        var latitude="-1";     // center latitude (decimal degrees)
                        var longitude="117";    // center longitude (decimal degrees)
                        var zoom="5";             // initial zoom (between 3 and 18)
                        """
        vesselfinder_html = f"<script > {vesselfinder} </script>" f"<script type=text/javascript src=https://www.vesselfinder.com/aismap.js > </script>"
        marrinetrafic = """ 
                        width='100%';		// the width of the embedded map in pixels or percentage
                        height='450';		// the height of the embedded map in pixels or percentage
                        border='1';		// the width of the border around the map (zero means no border)
                        shownames='false';	// to display ship names on the map (true or false)
                        latitude='-1';	// the latitude of the center of the map, in decimal degrees
                        longitude='117';	// the longitude of the center of the map, in decimal degrees
                        zoom='5';		// the zoom level of the map (values between 2 and 17)
                        maptype='0';		// use 0 for Normal Map, 1 for Satellite
                        trackvessel='0';	// MMSI of a vessel (note: vessel will be displayed only if within range of the system) - overrides "zoom" option
                        fleet='';		// the registered email address of a user-defined fleet (user's default fleet is used) - overrides "zoom" option
                        """
        marrinetrafic_html = f"<script > {vesselfinder} </script>" f"<script type=text/javascript src=https://www.vesselfinder.com/aismap.js > </script>" f"<script > {marrinetrafic} </script>" f"<script type=text/javascript src=//www.marinetraffic.com/js/embed.js > </script>"
        # Execute your app
        
        st.markdown("<h2 style='text-align: center; color: grey;'>Vessel Finder & Marine Trafic</h2>", unsafe_allow_html=True)
        html(marrinetrafic_html,width=1600, height=6000, scrolling=False)

def glosary():
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

def search():
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
def main():
    #st.markdown("<h1 style='text-align: center; color: black;'>Kementrian Perdagangan</h1>", unsafe_allow_html=True)
    image = Image.open('images/download.png')
    st.image(image)

    selected = option_menu (
        menu_title = None,
        options = ['HOME','DASAR HUKUM','PROJECT','GLOSARY','SEARCH','CONTACT'] ,
        icons = ["house","hammer", "book","globe","search" ,"envelope"],
        menu_icon= "cast",
        default_index=0,  
        orientation= "horizontal",
        )
    if selected == "HOME":
        st.markdown("<h1 style='text-align: center; color: black;'>HOME</h1>", unsafe_allow_html=True)
    if selected == "DASAR HUKUM":
        dasar_hukum()
    if selected == "PROJECT":       
        project()
    if selected == "GLOSARY":       
        glosary()
    if selected == "SEARCH":       
        search()
    if selected == "CONTACT":
        st.markdown("<h2 style='text-align: center; color: black;'>Author</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'>Ignatius Arga Wicaksono</h3>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>198803162022031001</h4>", unsafe_allow_html=True)



if __name__ == '__main__' :
    main()