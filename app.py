import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dronector Event",
    page_icon="🚁",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom,#f8fbff,#eef4ff);
}

.block-container{
    padding-top:0rem;
    max-width:1400px;
}

.title{
    color:#082a7a;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
    line-height:1.2;
}

.subtitle{
    color:#555;
    font-size:20px;
}

.follow-title{
    text-align:center;
    color:#082a7a;
    font-size:32px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:30px;
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
        font-size:28px;
        text-align:center;
    }

    .subtitle{
        font-size:16px;
        text-align:center;
    }

    .follow-title{
        font-size:26px;
    }

}

</style>
""", unsafe_allow_html=True)

st.image("logo.png", width=220)

st.markdown(
    """
    <div class='title'>
    Dronector Event Registration
    </div>

    <div class='subtitle'>
    Register below and stay connected with drone training,
    drone services and future events.
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,4,1])

components.iframe(
    "https://forms.gle/yxLAxgPCLw9zkhMw5",
    height=550,
    scrolling=True
)

st.markdown(
    "<div class='follow-title'>Follow Dronector</div>",
    unsafe_allow_html=True
)

st.markdown("""
<style>

.social-grid{
    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;
    margin-top:20px;
}

            .social-card{
    width:120px;
    height:120px;
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
    width:70px;
    height:70px;
    object-fit:contain;
}

</style>
""", unsafe_allow_html=True)

import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

facebook = img_to_base64("facebook.png")
instagram = img_to_base64("instagram.png")
tiktok = img_to_base64("tiktok.png")
youtube = img_to_base64("youtube.png")
xlogo = img_to_base64("x.png")
website = img_to_base64("website.png")

st.markdown(f"""
<div class="social-grid">

<a class="social-card"
href="https://www.facebook.com/dronector.academy"
target="_blank">
<img src="data:image/png;base64,{facebook}">
</a>

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
href="https://youtube.com/@dronector.academy?si=H7bpOQmoU0nhRtsJ"
target="_blank">
<img src="data:image/png;base64,{youtube}">
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

st.markdown(
    """
    <div class='footer'>
    © 2025 Dronector Limited | Empowering the future with drones
    </div>
    """,
    unsafe_allow_html=True
)
