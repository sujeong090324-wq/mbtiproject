# 🧩 MBTI 포켓몬 추천 웹앱 (Streamlit)

아래 코드를 `app.py`로 저장한 뒤, Streamlit Cloud에 업로드하면 돼!

```python
import streamlit as st
import random

st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

# -----------------------------
# 포켓몬 데이터
# -----------------------------
pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠⚡",
        "reason": "전략적이고 독립적인 당신은 강력한 지능형 포켓몬 뮤츠와 닮았어요!"
    },
    "INTP": {
        "name": "후딘",
        "emoji": "📚🔮",
        "reason": "호기심 많고 분석적인 당신은 IQ 5000의 후딘과 찰떡!"
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥👑",
        "reason": "카리스마 넘치고 리더십 강한 당신은 리자몽 스타일!"
    },
    "ENTP": {
        "name": "팬텀",
        "emoji": "😈🎭",
        "reason": "재치 있고 장난기 넘치는 당신은 팬텀과 잘 어울려요!"
    },
    "INFJ": {
        "name": "루기아",
        "emoji": "🌊🕊️",
        "reason": "신비롭고 깊은 감성을 가진 당신은 루기아 같은 존재예요."
    },
    "INFP": {
        "name": "이브이",
        "emoji": "🌸🦊",
        "reason": "따뜻하고 상상력 풍부한 당신은 사랑스러운 이브이와 딱 맞아요!"
    },
    "ENFJ": {
        "name": "가디안",
        "emoji": "💖✨",
        "reason": "다정하고 사람들을 챙기는 당신은 가디안 같은 힐러 타입!"
    },
    "ENFP": {
        "name": "피카츄",
        "emoji": "⚡🐭",
        "reason": "에너지 넘치고 모두를 즐겁게 하는 당신은 피카츄 그 자체!"
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "💧🛡️",
        "reason": "믿음직하고 책임감 강한 당신은 든든한 거북왕 스타일!"
    },
    "ISFJ": {
        "name": "해피너스",
        "emoji": "🥚💗",
        "reason": "배려심 깊고 따뜻한 당신은 해피너스와 닮았어요."
    },
    "ESTJ": {
        "name": "보스로라",
        "emoji": "⛓️💥",
        "reason": "강한 추진력과 책임감을 가진 당신은 보스로라 타입!"
    },
    "ESFJ": {
        "name": "푸크린",
        "emoji": "🎤🌟",
        "reason": "친화력 최고! 사람들과 함께할 때 빛나는 당신은 푸크린 같아요."
    },
    "ISTP": {
        "name": "루카리오",
        "emoji": "🥋🐺",
        "reason": "쿨하고 실전형인 당신은 루카리오와 완벽 매치!"
    },
    "ISFP": {
        "name": "나인테일",
        "emoji": "🦊🔥",
        "reason": "감성적이고 예술적인 분위기의 당신은 우아한 나인테일 스타일!"
    },
    "ESTP": {
        "name": "번치코",
        "emoji": "🔥🥊",
        "reason": "열정 넘치고 행동파인 당신은 번치코와 닮았어요!"
    },
    "ESFP": {
        "name": "파이리",
        "emoji": "🔥😄",
        "reason": "밝고 활발한 당신은 어디서든 분위기 메이커인 파이리!"
    }
}

# -----------------------------
# 제목
# -----------------------------
st.title("🎮 MBTI 포켓몬 추천기")
st.markdown("### ✨ 당신의 MBTI와 어울리는 포켓몬은?! ✨")
st.write("💡 MBTI를 선택하면 성격과 찰떡인 포켓몬을 추천해드려요!")

# -----------------------------
# MBTI 선택
# -----------------------------
mbti_list = list(pokemon_data.keys())
selected_mbti = st.selectbox(
    "🧩 당신의 MBTI를 골라주세요!",
    mbti_list
)

# -----------------------------
# 추천 버튼
# -----------------------------
if st.button("🔍 포켓몬 추천받기!"):
    result = pokemon_data[selected_mbti]

    st.balloons()

    st.markdown("---")
    st.markdown(f"# {result['emoji']} {result['name']}")

    st.success(f"🎉 {selected_mbti}인 당신에게 어울리는 포켓몬은 바로 **{result['name']}**!")

    st.write(result['reason'])

    lucky_message = random.choice([
        "🌟 오늘은 엄청난 모험이 기다리고 있을지도?!",
        "🍀 야생 포켓몬과 눈이 마주칠 것 같은 하루예요!",
        "⚡ 당신의 매력이 전기처럼 팍팍 터지는 중!",
        "🎒 몬스터볼 챙기고 떠나볼까요?",
        "💫 당신은 이미 포켓몬 세계의 주인공!"
    ])

    st.info(lucky_message)

# -----------------------------
# 하단 꾸미기
# -----------------------------
st.markdown("---")
st.caption("🫶 Made with Streamlit & Pokémon Love")
