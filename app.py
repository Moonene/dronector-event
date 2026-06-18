import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Freedom 250 Event",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom,#f8fbff,#eef4ff);
}

.block-container{
    padding-top:3rem;
    max-width:1400px;
}

.title{
    color:#082a7a;
    font-size:30px;
    font-weight:700;
    margin-bottom:10px;
    line-height:1.6;
    text-align:center;
    max-width:900px;
    margin-left:auto;
    margin-right:auto;
    padding-left:10px;
    padding-right:10px;
}

.follow-title{
    text-align:center;
    color:#082a7a;
    font-size:24px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:#666;
    margin-top:30px;
    padding-bottom:20px;
}

iframe{
    border-radius:15px;
}

@media (max-width: 768px){

.title{
    font-size:24px;
    text-align:center;
    line-height:1.4;
}

    .follow-title{
        font-size:26px;
    }

}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
<div style="text-align:center;">

<div class='title'>
Welcome to the Freedom 250 Drone Experience
</div>

<div style="
    color:#666;
    font-size:14px;
    line-height:1.5;
    max-width:800px;
    margin:auto;
    padding-left:10px;
    padding-right:10px;
">
Explore drone services, professional training and the future of aerial innovation.
</div>

</div>
""",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="height:20px;"></div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,4,1])

components.iframe(
    "https://docs.google.com/forms/d/e/1FAIpQLSfy2whqDYdGJhHgxragukTolS873h7wA1QaekyxnWlUcu_kkQ/viewform?embedded=true",
    height=600,
    scrolling=True
)

st.markdown("""
<style>

.social-grid{
    display:flex;
    justify-content:center;
    gap:8px;
    flex-wrap:wrap;
    margin-top:5px;
}

.social-card{
    width:90px;
    height:90px;
    background:white;
    border-radius:20px;
    padding:15px;
    text-decoration:none;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
    display:flex;
    align-items:center;
    justify-content:center;
    border:2px solid transparent;
}

.social-card:hover{
    transform:translateY(-5px);
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
    border-color:#082a7a;
}

.social-card img{
    width:50px;
    height:50px;
    object-fit:contain;
}

            @media (max-width: 768px){

    .social-grid{
        flex-wrap:nowrap;
        justify-content:center;
        gap:6px;
    }

    .social-card{
        width:65px;
        height:65px;
        padding:8px;
    }

    .social-card img{
        width:38px;
        height:38px;
    }

}

</style>
""", unsafe_allow_html=True)

import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = img_to_base64("logo.png")
instagram = img_to_base64("instagram.png")
tiktok = img_to_base64("tiktok.png")
xlogo = img_to_base64("x.png")
website = img_to_base64("website.png")

st.markdown(f"""
<style>

.stApp::before {{
    content:"";
    position:fixed;
    top:50%;
    left:50%;
    width:550px;
    height:550px;
    transform:translate(-50%, -50%);
    background:url("data:image/png;base64,{logo}") no-repeat center;
    background-size:contain;
    opacity:0.10;
    pointer-events:none;
    z-index:0;
}}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        text-align:center;
        color:#082a7a;
        font-size:24px;
        font-weight:700;
        margin-top:15px;
        margin-bottom:15px;
        letter-spacing:1px;
    ">
        FOLLOW US
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="social-grid">


<a class="social-card"
href="https://www.instagram.com/dronector.academy/"
target="_blank">
<img src="data:image/png;base64,{instagram}">
</a>

<a class="social-card"
href="https://www.tiktok.com/@dronector.ac?_r=1&_t=ZS-96vQAzSRnlc"
target="_blank">
<img src="data:image/png;base64,{tiktok}">
</a>


<a class="social-card"
href="https://x.com/dronector_ac?s=11"
target="_blank">
<img src="data:image/png;base64,{xlogo}">
</a>

<a class="social-card"
href="https://www.dronector.com/"
target="_blank">
<img src="data:image/png;base64,{website}">
</a>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        text-align:center;
        color:#082a7a;
        font-size:22px;
        font-weight:700;
        margin-top:20px;
        margin-bottom:20px;
    ">
        Download Our Brochure
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>

div[data-testid="stDownloadButton"] > button {
    background-color:#082a7a;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px 20px;
    font-size:16px;
    font-weight:600;
    width:100%;
}

div[data-testid="stDownloadButton"] > button:hover {
    background-color:#0b3aa5;
    color:white;
}

</style>
""", unsafe_allow_html=True)

with open("brochure.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download Brochure",
    data=PDFbyte,
    file_name="Freedom250_Brochure.pdf",
    mime="application/pdf",
    use_container_width=True
)



st.markdown(
    """
    <div class='footer'>
    © 2025 Dronector Limited | Empowering the future with drones
    </div>
    """,
    unsafe_allow_html=True
)
