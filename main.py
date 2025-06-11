import streamlit as st

# 🎨 앱 꾸미기용 CSS
st.markdown("""
    <style>
    .title {
        font-size:50px !important;
        text-align: center;
        color: #f63366;
        font-weight: bold;
    }
    .subtitle {
        font-size:24px !important;
        text-align: center;
        color: #6c6c6c;
    }
    .recommendation {
        font-size: 20px;
        padding: 20px;
        background-color: #ffe6f0;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 🌟 타이틀
st.markdown('<div class="title">🌈 MBTI로 보는 진로 추천 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI를 선택하고, 어울리는 직업을 알아보세요! 🚀</div>', unsafe_allow_html=True)

# 🎯 MBTI 유형 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🧠 MBTI 별 직업 추천 데이터
career_dict = {
    "INTJ": ["🔬 과학자", "📊 전략 컨설턴트", "👨‍💻 데이터 사이언티스트"],
    "INTP": ["🧪 연구원", "💻 소프트웨어 개발자", "🧠 AI 엔지니어"],
    "ENTJ": ["💼 CEO", "📈 경영 컨설턴트", "🧑‍⚖️ 기획자"],
    "ENTP": ["🎤 마케팅 전문가", "🚀 스타트업 창업자", "📱 UX 디자이너"],
    "INFJ": ["🌱 심리상담가", "📚 작가", "🧘‍♀️ 명상 코치"],
    "INFP": ["🎨 일러스트레이터", "✍️ 시나리오 작가", "📖 편집자"],
    "ENFJ": ["🎓 교육자", "💬 커뮤니케이션 코치", "🎭 연극 연출가"],
    "ENFP": ["🌍 사회운동가", "📹 유튜버", "🎉 이벤트 플래너"],
    "ISTJ": ["🧾 회계사", "⚖️ 법무사", "📦 물류 관리자"],
    "ISFJ": ["🏥 간호사", "📘 사서", "👨‍👩‍👧‍👦 사회복지사"],
    "ESTJ": ["🏢 관리자", "💼 인사담당자", "🧾 세무사"],
    "ESFJ": ["👩‍🏫 교사", "📣 홍보 담당자", "🛍️ 서비스 매니저"],
    "ISTP": ["🔧 정비사", "🚓 경찰관", "🧗‍♂️ 구조대원"],
    "ISFP": ["📷 사진작가", "🎨 예술가", "🌿 플로리스트"],
    "ESTP": ["💸 세일즈 전문가", "🎮 게임 디자이너", "🏎️ 레이서"],
    "ESFP": ["🎤 가수", "📺 방송인", "👗 패션 디자이너"]
}

# 📌 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 ✨", mbti_list)

if selected_mbti:
    st.markdown(f"## 당신의 MBTI는 {selected_mbti}! 😍")
    st.markdown('<div class="recommendation">🎯 어울리는 직업 추천:</div>', unsafe_allow_html=True)
    for job in career_dict[selected_mbti]:
        st.markdown(f"✅ {job}")

# 💫 푸터
st.markdown("---")
st.markdown("Made with ❤️ by 진로코치 AI")

