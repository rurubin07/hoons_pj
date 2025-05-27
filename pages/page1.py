import streamlit as st
import random
import datetime

st.set_page_config(page_title="인생 추천 앱", layout="centered")

st.title("🎉 당신의 하루를 바꿔줄 랜덤 인생 추천 앱")
st.markdown("오늘 기분 전환이 필요한 당신을 위한 작은 선물입니다 🎁")

# 현재 시간
now = datetime.datetime.now()
st.write(f"🕒 현재 시각: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 명언 리스트
quotes = [
    "🌟 '삶이 있는 한 희망은 있다.' – 키케로",
    "🔥 '성공은 넘어지는 것이 아니라, 넘어질 때마다 일어서는 것이다.' – 넬슨 만델라",
    "💡 '가장 어두운 밤도 끝나고 해는 떠오른다.' – 빅토르 위고",
    "🌈 '행복은 방향이지 장소가 아니다.' – 시드니 J. 해리스"
]

# 유튜브 음악 추천
music_links = [
    ("힐링 피아노", "https://www.youtube.com/watch?v=2OEL4P1Rz04"),
    ("잔잔한 인디", "https://www.youtube.com/watch?v=wzK5FJbK1lA"),
    ("기분 좋아지는 팝", "https://www.youtube.com/watch?v=knW7-x7Y7RE"),
    ("집중 잘 되는 로파이", "https://www.youtube.com/watch?v=jfKfPfyJRdk")
]

# 밸런스 게임
balance_questions = [
    ("하루 종일 아무것도 안 하기", "하루 종일 바쁘게 일하기"),
    ("무한 야식 가능 vs 평생 다이어트 성공", "평생 다이어트 성공 vs 무한 야식 가능"),
    ("10억 받고 친구와 절교", "가난하지만 평생 우정 유지"),
]

# 챌린지 제안
challenges = [
    "📕 오늘 책 10페이지 읽기",
    "📧 연락 안 했던 친구에게 안부 메시지 보내기",
    "🚶‍♀️ 산책 15분 다녀오기",
    "🧘‍♂️ 3분 명상 해보기",
    "✍️ 오늘 감사한 일 3가지 적기"
]

st.subheader("1️⃣ 오늘의 명언")
st.success(random.choice(quotes))

st.subheader("2️⃣ 오늘의 추천 음악 🎵")
music = random.choice(music_links)
st.write(f"- **{music[0]}**")
st.video(music[1])

st.subheader("3️⃣ 지금 기분은 어떤가요?")
mood = st.radio("기분 선택", ["😊 좋음", "😐 그냥 그래요", "😣 우울해요", "😡 짜증나요"])

if mood == "😊 좋음":
    st.balloons()
    st.info("기분 좋을 때는 주변 사람에게 그 기분을 전해보세요!")
elif mood == "😐 그냥 그래요":
    st.write("조금 지루하다면, 음악과 함께 산책은 어때요?")
elif mood == "😣 우울해요":
    st.warning("우울할 땐 혼자 있지 말고 누군가와 이야기해보는 것도 좋아요 💬")
elif mood == "😡 짜증나요":
    st.error("짜증날 땐 일단 숨을 크게 3번 쉬고, 잠깐 눈을 감아보세요 😌")

st.subheader("4️⃣ 랜덤 밸런스 게임 💬")
q = random.choice(balance_questions)
st.write(f"**어떤 걸 고르시겠어요?**")
col1, col2 = st.columns(2)
with col1:
    st.button(q[0])
with col2:
    st.button(q[1])

st.subheader("5️⃣ 오늘의 미션 🎯")
st.info(random.choice(challenges))
