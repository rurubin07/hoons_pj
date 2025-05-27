import streamlit as st
from PIL import Image, ImageDraw
import random
import time

# 화면 설정
canvas_width = 400
canvas_height = 600
player_size = 30
rock_min_size = 15
rock_max_size = 50
rock_speed = 5

# 세션 상태 초기화
if 'player_x' not in st.session_state:
    st.session_state.player_x = canvas_width // 2
if 'rocks' not in st.session_state:
    st.session_state.rocks = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'frame' not in st.session_state:
    st.session_state.frame = 0

# 키 입력 처리
left, right = st.columns([1, 1])
with left:
    if st.button("⬅️"):
        st.session_state.player_x -= 30
with right:
    if st.button("➡️"):
        st.session_state.player_x += 30

# 벽 충돌 방지
st.session_state.player_x = max(0, min(canvas_width - player_size, st.session_state.player_x))

# 경과 시간 표시
elapsed = time.time() - st.session_state.start_time
st.markdown(f"⏱️ **경과 시간: {elapsed:.1f}초**")

# 게임 캔버스 생성
img = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(img)

# 플레이어 그리기
player_y = canvas_height - 40
draw.rectangle(
    [st.session_state.player_x, player_y, st.session_state.player_x + player_size, player_y + player_size],
    fill="blue"
)

# 돌 추가: 프레임 수에 따라 확률 증가
if st.session_state.frame % max(1, int(30 - elapsed // 3)) == 0:
    rock_size = random.randint(rock_min_size, rock_max_size)
    rock_x = random.randint(0, canvas_width - rock_size)
    st.session_state.rocks.append({'x': rock_x, 'y': 0, 'size': rock_size})

# 돌 이동 및 그리기
new_rocks = []
for rock in st.session_state.rocks:
    rock['y'] += rock_speed
    if rock['y'] < canvas_height:
        new_rocks.append(rock)
    draw.ellipse([rock['x'], rock['y'], rock['x'] + rock['size'], rock['y'] + rock['size']], fill="gray")

    # 충돌 체크
    if (
        st.session_state.player_x < rock['x'] + rock['size'] and
        st.session_state.player_x + player_size > rock['x'] and
        player_y < rock['y'] + rock['size'] and
        player_y + player_size > rock['y']
    ):
        st.session_state.game_over = True

st.session_state.rocks = new_rocks
st.session_state.frame += 1

# 캔버스 표시
st.image(img)

# 게임 종료 메시지
if st.session_state.game_over:
    st.error(f"💥 게임 오버! 생존 시간: {elapsed:.1f}초")
    if st.button("🔁 다시 시작"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
else:
    st.experimental_rerun()
