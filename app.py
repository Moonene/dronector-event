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
    font-size:32px;
    font-weight:700;
    margin-bottom:6px;
    line-height:1.2;
}

.subtitle{
    color:#666;
    font-size:14px;
    line-height:1.4;
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

st.image("logo.png", width=140)

st.markdown(
    """
    <div class='title'>
    Dronector Event Registration
    </div>

  <div class='subtitle'>
Register below to stay connected with Dronector.
</div>
    """,
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,4,1])

components.iframe(
    "https://forms.gle/yxLAxgPCLw9zkhMw5",
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

instagram = img_to_base64("instagram.png")
tiktok = img_to_base64("tiktok.png")
xlogo = img_to_base64("x.png")
website = img_to_base64("website.png")

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

.brochure-button{
    text-align:center;
    margin-top:20px;
}

.brochure-button a{
    display:inline-block;
    background:#082a7a;
    color:white !important;
    text-decoration:none !important;
    padding:18px 40px;
    border-radius:18px;
    font-size:20px;
    font-weight:600;
    box-shadow:0 6px 18px rgba(8,42,122,0.25);
}

.brochure-button a:hover{
    background:#0b3aa5;
}

</style>

<div class="brochure-button">
    <a href="https://www.canva.com/design/DAF-o8D_h80/aV1hOl-sl1U1vcsLpnwHEA/view?utm_content=DAF-o8D_h80&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd43734cfaa"
       target="_blank">
       📄 View Dronector Brochure
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a class="brochure-card"
href="https://www.canva.com/design/DAF-o8D_h80/aV1hOl-sl1U1vcsLpnwHEA/view?utm_content=DAF-o8D_h80&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd43734cfaa"
target="_blank">


</a>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class='footer'>
    © 2025 Dronector Limited | Empowering the future with drones
    </div>
    """,
    unsafe_allow_html=True
)
