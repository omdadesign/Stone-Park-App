import streamlit as st

# إعدادات الهوية البصرية لـ Stone Park
st.set_page_config(page_title="Stone Park Studio", page_icon="🏛️")

# تخصيص الألوان (الذهبي والرمادي)
st.markdown("""
    <style>
    .stApp { background-color: #F4F4F4; } 
    .stButton>button { 
        background-color: #C5A059; color: white; border-radius: 20px; 
        border: none; font-weight: bold; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1A1A1A; color: #C5A059; }
    .main-title { color: #1A1A1A; text-align: center; font-family: 'serif'; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🏛️ Stone Park Greeting Generator</h1>", unsafe_allow_html=True)

# القسم الأول: اختيار نوع الرخام (الخلفية)
st.subheader("1. اختر نوع الرخام أو الجرانيت")
stone_type = st.select_slider("", options=["White Statuario", "Black Marquina", "Gold Granite", "Grey Marble"])

# القسم الثاني: النص والعبارات الجاهزة (Presets)
st.subheader("2. نص التهنئة")
col_p1, col_p2, col_p3 = st.columns(3)

if col_p1.button("عيد سعيد"): st.session_state.text = "عيد سعيد وكل عام وأنتم بخير"
if col_p2.button("تقبل الله"): st.session_state.text = "تقبل الله طاعتكم وصالح أعمالكم"
if col_p3.button("Happy Eid"): st.session_state.text = "Wishing you a blessed and joyful Eid"

final_text = st.text_area("عدل النص هنا:", value=st.session_state.get('text', 'تهنئكم بحلول عيد الفطر المبارك...'))

# القسم الثالث: السحب والإفلات (Drag & Drop)
st.subheader("3. إضافة صورة ريفرنس (اختياري)")
uploaded_file = st.file_uploader("اسحب صورتك هنا لدمجها مع الرخام", type=['png', 'jpg', 'jpeg'])

# زر التوليد النهائي
if st.button("✨ إنشاء التهنئة الفاخرة"):
    st.balloons()
    st.info("قم بنسخ هذا الوصف ولصقه في Gemini للحصول على الصورة بدقة 4K:")
    
    # توليد "برومبت" تلقائي بناءً على خيارات المستخدم
    generated_prompt = f"Create a 4K luxury Eid card with {stone_type} background, gold frames, 3D Stone Park logo, a plate of Kahk, and this text: {final_text}. Add URL: stonepark-marble.com"
    st.code(generated_prompt)
    
    st.warning("بما أننا لا نستخدم API، انسخ الكود أعلاه وضعه في محادثة AI Studio المجهزة مسبقاً.")

st.markdown("<br><hr><center>Design by Stone Park Intelligence © 2026</center>", unsafe_allow_html=True)
