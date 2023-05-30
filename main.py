import streamlit as st
import utils as utl
import os
from PIL import Image
import pandas as pd
import numpy as np

# from views import home,about,results,voting,profile,register

st.set_page_config(layout="wide", page_title='E-Voting')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

screen = st.empty()
votedata = pd.read_csv(os.path.join(os.path.dirname(__file__), 'assets', 'votes.txt'), sep=",")
user = pd.read_csv(os.path.join(os.path.dirname(__file__), 'assets', 'voteuser.txt'), sep=",")

global nama
def main(regist):
    with screen.container():
        with st.form("Registration"):
            st.subheader("Silakan masukkan data diri.")
            id_no = st.text_input("No Kartu Tanda Penduduk")
            nama = st.text_input("Nama lengkap sesuai KTP", max_chars=50)
            email = st.text_input("Email")
            no_telp = st.text_input("Nomor telepon")
            submit = st.form_submit_button("Daftar")
    if submit:
        regist += 1
        inputuser = id_no + "," + nama + "," + email + "," + no_telp
        with open(os.path.join(os.path.dirname(__file__), 'assets', 'database_user.txt'), 'a') as d:
            d.write("\n" + inputuser)
        navigation(1)

def navigation(i):
    global nama
    route = utl.get_current_route()
    if route == "home":
        home()
    elif route == "about":
        about()
    elif route == "voting":
        voting()
    elif route == "results":
        results()
    elif route == "profile":
        profile()
    elif route == None:
        if i == 0:
            nama = register()
            i+=1
        else:
            home()

def register():
    with screen.container():
        screen.title("Registration Page")
        with screen.form("Registration"):
            st.subheader("Silakan masukkan data diri.")
            id_no = st.text_input("No Kartu Tanda Penduduk")
            nama = st.text_input("Nama lengkap sesuai KTP", max_chars=50)
            email = st.text_input("Email")
            no_telp = st.text_input("Nomor telepon")

            submit = st.form_submit_button("Daftar")

        if submit:
            inputuser = id_no + "," + nama + "," + email + "," + no_telp
            with open(os.path.join(os.path.dirname(__file__), 'assets', 'database_user.txt'), 'a') as d:
                d.write("\n" + inputuser)
            screen.empty()
            home()
            return
    return nama


def home():
    bawaslulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'bawaslu.png'))
    kpulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'KPU_Logo.png'))
    logo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'logo.png'))
    calon1 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon1.png'))
    calon2 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon2.png'))
    calon3 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon3.png'))
    calon4 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon4.png'))
    with st.sidebar:
        st.image(logo)
    with screen.container():
        col1, col2, col3, col4 = st.columns([2, 3, 3, 1])
        with col1:
            st.image(bawaslulogo)
        with col2:
            st.empty()
        with col3:
            st.empty()
        with col4:
            st.image(kpulogo.resize((100,100)))
        st.markdown("---")
        st.markdown("**<p style='font-size:20px;text-align:center'> MARI KITA SUKSESKAN<br>"
                    "PEMILU SERENTAK TAHUN 2024 YANG AMAN DAN DAMAI<br>"
                    "TETAP MENJAGA SEMANGAT PERSATUAN DAN KESATUAN UNTUK MEWUJUDKAN<br>"
                    "PEMILU YANG DEMOKRATIS DAN BERMARTABAT</p>**", unsafe_allow_html=True)
        st.markdown("---")
        col1a, col3a, col5a, col7a = st.columns([1,1,1,1],gap="large")
        with col1a:
            st.image(calon1, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 1 </p>", unsafe_allow_html=True)
        with col3a:
            st.image(calon2, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 2 </p>", unsafe_allow_html=True)
        with col5a:
            st.image(calon3, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 3 </p>", unsafe_allow_html=True)
        with col7a:
            st.image(calon4, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 4 </p>", unsafe_allow_html=True)


def about():
    with screen.container():
        bawaslulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'bawaslu.png'))
        kpulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'KPU_Logo.png')).resize(
            (100, 100))
        banner = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', '18112020142133.png'))
        col1, col2, col3, col4 = st.columns([2, 3, 3, 1])
        with col1:
            st.image(bawaslulogo)
        with col2:
            st.empty()
        with col3:
            st.empty()
        with col4:
            st.image(kpulogo)
        st.markdown("---")
        st.image(banner, width=1350)
        st.markdown("<p style='font-size:20px;text-align: justify; text-justify: inter-word;padding-top:50px'>Pemilu adalah kependekan dari Pemilihan Umum, yaitu proses pemilihan wakil rakyat dan/atau"
                    " kepala negara dalam sebuah negara secara langsung atau tidak langsung melalui hak suara rakyat"
                    " yang telah memenuhi syarat sebagai pemilih. Pemilu bertujuan untuk memilih dan menentukan wakil"
                    " rakyat atau kepala negara yang akan mewakili kepentingan masyarakat calam mengambil keputusan"
                    " politik dan menyelesaikan masalah-masalah di negara tersebut. Pemilu dilakukan secara berkala"
                    " sesuai dengan ketentuan perundang-undangan yang berlaku, dan dikuti oleh partai politik atau"
                    " calon independen yang memenuhi persyaratan yang ditetapkan. Di Inconesia, pemilu diadakan"
                    " secara umum setiap lima tahun sekali, dan melibatkan rakyat dalam memilih anggota legislatif,"
                    " presiden, dan wakil presiden.</p>", unsafe_allow_html=True)


def voting():
    with screen.container():
        logo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'logo.png'))
        calon1 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon1.png'))
        calon2 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon2.png'))
        calon3 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon3.png'))
        calon4 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon4.png'))
        with st.sidebar:
            st.image(logo)
            nik = st.text_input("NIK")
            name = st.text_input("Nama Lengkap")
            vote = st.button("Submit")
        st.markdown("**<p style='font-size:20px;text-align:center'> MARI KITA SUKSESKAN<br>"
                    "PEMILU SERENTAK TAHUN 2024 YANG AMAN DAN DAMAI<br>"
                    "TETAP MENJAGA SEMANGAT PERSATUAN DAN KESATUAN UNTUK MEWUJUDKAN<br>"
                    "PEMILU YANG DEMOKRATIS DAN BERMARTABAT</p>**", unsafe_allow_html=True)
        st.markdown("---")
        col1a, col3a, col5a, col7a = st.columns([1, 1, 1, 1], gap="large")
        with col1a:
            st.image(calon1, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 1 </p>", unsafe_allow_html=True)
        with col3a:
            st.image(calon2, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 2 </p>", unsafe_allow_html=True)
        with col5a:
            st.image(calon3, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 3 </p>", unsafe_allow_html=True)
        with col7a:
            st.image(calon4, use_column_width= "always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 4 </p>", unsafe_allow_html=True)
        st.markdown("""
            <style>
            [role=radiogroup]{
                gap: 12rem;
                padding-left:5rem;
                align-items: space-evenly
            }
            
            [role=button]{
                align-self=center}
            </style>
            """, unsafe_allow_html=True)

        choice = st.radio("", ("Calon 1", "Calon 2", "Calon 3", "Calon 4"), horizontal=True)
        if vote:
            if choice=="Calon 1":
                votedata['jumlah'][votedata['calon']=='calon1'] = votedata['jumlah'][votedata['calon']=='calon1']+1
            elif choice=="Calon 2":
                votedata['jumlah'][votedata['calon'] == 'calon2'] = votedata['jumlah'][votedata['calon'] == 'calon2'] + 1
            elif choice=="Calon 3":
                votedata['jumlah'][votedata['calon'] == 'calon3'] = votedata['jumlah'][votedata['calon'] == 'calon3'] + 1
            elif choice=="Calon 4":
                votedata['jumlah'][votedata['calon'] == 'calon4'] = votedata['jumlah'][votedata['calon'] == 'calon4'] + 1
            st.markdown("<p style='font-size:2rem; text-align:center'> Terima kasih sudah memilih!</p>", unsafe_allow_html=True)
            votedata.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'votes.txt'), index=None, sep=',', mode='w')
        # choice = st.radio("", ("Calon 1", "Calon 2", "Calon 3", "Calon 4"), horizontal=True)

        # if vote and choice:
        #     if choice == "Calon 1":
        #         votedata['jumlah'][votedata['calon'] == 'calon1'] = votedata['jumlah'][votedata['calon'] == 'calon1'] + 1
        #     elif choice == "Calon 2":
        #         votedata['jumlah'][votedata['calon'] == 'calon2'] = votedata['jumlah'][votedata['calon'] == 'calon2'] + 1
        #     elif choice == "Calon 3":
        #         votedata['jumlah'][votedata['calon'] == 'calon3'] = votedata['jumlah'][votedata['calon'] == 'calon3'] + 1
        #     elif choice == "Calon 4":
        #         votedata['jumlah'][votedata['calon'] == 'calon4'] = votedata['jumlah'][votedata['calon'] == 'calon4'] + 1

        #     st.markdown("<p style='font-size:2rem; text-align:center'>Terima kasih sudah memilih!</p>", unsafe_allow_html=True)
        #     votedata.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'votes.txt'), index=None, sep=',', mode='w')
        #     vote = False
        # else:
        #     st.markdown("<p style='font-size:2rem; text-align:center'>Anda sudah melakukan pemilihan.</p>", unsafe_allow_html=True)

# def voting():
#     with screen.container():
#         logo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'logo.png'))
#         calon1 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon1.png'))
#         calon2 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon2.png'))
#         calon3 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon3.png'))
#         calon4 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon4.png'))
#         with st.sidebar:
#             st.image(logo)
#             nik = st.text_input("NIK")
#             name = st.text_input("Nama Lengkap")
#             vote = st.button("Submit")
#         st.markdown("**<p style='font-size:20px;text-align:center'> MARI KITA SUKSESKAN<br>"
#                     "PEMILU SERENTAK TAHUN 2024 YANG AMAN DAN DAMAI<br>"
#                     "TETAP MENJAGA SEMANGAT PERSATUAN DAN KESATUAN UNTUK MEWUJUDKAN<br>"
#                     "PEMILU YANG DEMOKRATIS DAN BERMARTABAT</p>**", unsafe_allow_html=True)
#         st.markdown("---")
#         col1a, col3a, col5a, col7a = st.columns([1, 1, 1, 1], gap="large")
#         with col1a:
#             st.image(calon1, use_column_width= "always")
#             st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 1 </p>", unsafe_allow_html=True)
#         with col3a:
#             st.image(calon2, use_column_width= "always")
#             st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 2 </p>", unsafe_allow_html=True)
#         with col5a:
#             st.image(calon3, use_column_width= "always")
#             st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 3 </p>", unsafe_allow_html=True)
#         with col7a:
#             st.image(calon4, use_column_width= "always")
#             st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 4 </p>", unsafe_allow_html=True)
#         st.markdown("""
#             <style>
#             [role=radiogroup]{
#                 gap: 12rem;
#                 padding-left:5rem;
#                 align-items: space-evenly
#             }
            
#             [role=button]{
#                 align-self=center}
#             </style>
#             """, unsafe_allow_html=True)

#         if vote and choice:
#             if votedata[(votedata['nik'] == nik) & (votedata['nama'] == name)].empty:
#                 choice = st.radio("", ("Calon 1", "Calon 2", "Calon 3", "Calon 4"), horizontal=True)
#                 if choice == "Calon 1":
#                     votedata['jumlah'][votedata['calon'] == 'calon1'] += 1
#                 elif choice == "Calon 2":
#                     votedata['jumlah'][votedata['calon'] == 'calon2'] += 1
#                 elif choice == "Calon 3":
#                     votedata['jumlah'][votedata['calon'] == 'calon3'] += 1
#                 elif choice == "Calon 4":
#                     votedata['jumlah'][votedata['calon'] == 'calon4'] += 1

#                 st.markdown("<p style='font-size:2rem; text-align:center'>Terima kasih sudah memilih!</p>", unsafe_allow_html=True)
#                 votedata.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'votes.txt'), index=None, sep=',', mode='w')
#                 vote = False
#             else:
#                 st.markdown("<p style='font-size:2rem; text-align:center'>Anda sudah melakukan pemilihan.</p>", unsafe_allow_html=True)
#         else:
#             st.markdown("<p style='font-size:2rem; text-align:center'>Anda sudah melakukan pemilihan.</p>", unsafe_allow_html=True)



def results():
    with screen.container():
        calon1 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon1.png'))
        calon2 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon2.png'))
        calon3 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon3.png'))
        calon4 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'calon4.png'))
        votedata = pd.read_csv(os.path.join(os.path.dirname(__file__), 'assets', 'votes.txt'), sep=",")
        st.title("Results Page")
        st.markdown("---")
        st.bar_chart(votedata, x="calon", y="jumlah")
        perc1= votedata['jumlah'][votedata['calon']=="calon1"]/sum(votedata['jumlah'])*100
        perc2 = votedata['jumlah'][votedata['calon'] == "calon2"] / sum(votedata['jumlah']) * 100
        perc3 = votedata['jumlah'][votedata['calon'] == "calon3"] / sum(votedata['jumlah']) * 100
        perc4 = votedata['jumlah'][votedata['calon'] == "calon4"] / sum(votedata['jumlah']) * 100

        col1a, col2a, col3a, col4a = st.columns([1, 1, 1, 1], gap="large")
        with col1a:
            st.image(calon1, use_column_width="always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 1 </p>", unsafe_allow_html=True)
        with col2a:
            st.image(calon2, use_column_width="always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 2 </p>", unsafe_allow_html=True)
        with col3a:
            st.image(calon3, use_column_width="always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 3 </p>", unsafe_allow_html=True)
        with col4a:
            st.image(calon4, use_column_width="always")
            st.markdown("<p style='text-align:center;font-size:20px'> CAPRES & CAWAPRES 4 </p>", unsafe_allow_html=True)

def profile():
    with screen.container():
        bawaslulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'bawaslu.png'))
        kpulogo = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'KPU_Logo.png'))
        kpu1 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'kpu1.png'))
        kpu2 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'kpu2.png'))
        kpu3 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'kpu3.png'))
        kpu4 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'kpu4.png'))
        kpu5 = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'images', 'kpu5.png'))
        col1, col2, col3, col4 = st.columns([2, 3, 3, 1])
        with col1:
            st.image(bawaslulogo)
        with col2:
            st.empty()
        with col3:
            st.empty()
        with col4:
            st.image(kpulogo.resize((100, 100)))
        st.markdown("---")
        st.markdown("**<p style='font-size:25px;text-align:center'>Badan independen yang bertugas mengawasidan menegakkan<br>"
                    "hukum dalam pemilihan umum di Indonesia.<br>"
                    "Berkomitmen untuk mewujudkan pemilihan umum yang jujur, adil,<br>"
                    "dan transparan.</p>**", unsafe_allow_html=True)
        col1a, col2a, col3a = st.columns([2,5,2], gap="large")
        with col1a:
            st.image(kpu1, use_column_width= "always")
            st.image(kpu2, use_column_width= "always")
            st.image(kpu3, use_column_width= "always")
        with col2a:
            st.markdown("**<p style='font-size:20px;text-align:left, margin-top:50px'>Visi dan Misi</p>**", unsafe_allow_html=True)
            st.markdown("**<p style='font-size:18px;text-align:left'>Visi</p>**", unsafe_allow_html=True)
            st.markdown("<p style='font-size:18px; text-align:justify; text-justify: inter-word'>"
                        "Menjadi lembaga pengawas pemilu yang terpercaya</p>", unsafe_allow_html=True)
            st.markdown("**<p style='font-size:18px;text-align:left'>Misi</p>**", unsafe_allow_html=True)
            st.markdown("<ol style='list-style-type:decima'> <li style='font-size:18px; text-align:justify; text-justify: inter-word'>"
                        "Meningkatkan kualitas pencegahan dan pengawasan pemilu yang inovatif serta kepeloporan masyarakat dalam pengawasan partisipatif;</li>"
                        "<li style='font-size:18px; text-align:justify; text-justify: inter-word'>Meningkatkan kualitas penindakanpelanggaran dan penyelesaian sengketa proses pemilu yang progresif, cepat dan sederhana;</li>"
                        "<li style='font-size:18px; text-align:justify; text-justify: inter-word'>Meningkatkan kualitas produk hukum yang harmonis dan terintegrasi;</li>"
                        "<li style='font-size:18px; text-align:justify; text-justify: inter-word'>Memperkuat sistem teknologi informasi untuk mendukung kinerja pengawasan, penindakan serta penyelesaian sengketa pemilu terintegrasi, efektif, transparan dan aksesibel;</li>"
                        "<li style='font-size:18px; text-align:justify; text-justify: inter-word'>Mempercepat penguatan kelembagaan, dan SDM pengawas serta aparatur Sekretariat di seluruh jenjang kelembagaan pengawas pemilu, melalui penerapan tata kelola organisasi yang profesional dan berbasis teknologi informasi sesuai dengan prinsip tata-pemerintahan yang baik dan bersih.</li></ol>",
                        unsafe_allow_html=True)
        with col3a:
            st.image(kpu4, use_column_width= "always")
            st.image(kpu5, use_column_width= "always")


navigation(0)
