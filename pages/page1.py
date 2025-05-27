import streamlit as st

# 대학별 데이터: 수능 점수대, 위치(대략적인 지역)
universities = {
    "서울대학교": {"score_range": "1~2등급", "location": "서울 관악구"},
    "연세대학교": {"score_range": "2~3등급", "location": "서울 서대문구"},
    "고려대학교": {"score_range": "2~3등급", "location": "서울 성북구"},
    "한양대학교": {"score_range": "3~4등급", "location": "서울 성동구"},
    "성균관대학교": {"score_range": "3~4등급", "location": "서울 종로구"},
    "중앙대학교": {"score_range": "4~5등급", "location": "서울 동작구"},
    "경희대학교": {"score_range": "4~5등급", "location": "서울 동대문구"},
    "이화여자대학교": {"score_range": "3~4등급", "location": "서울 서대문구"},
    "부산대학교": {"score_range": "4~5등급", "location": "부산 금정구"},
    "경북대학교": {"score_range": "4~5등급", "location": "대구 북구"},
    # 필요하면 더 추가 가능
}

st.title("한국 대학 순위별 정보")

st.write("아래에서 대학을 선택하면 수능 점수대와 위치 정보를 보여줍니다.")

# 순위별 나열 (딕셔너리는 순서 보장되니 이렇게 나열됨)
univ_list = list(universities.keys())

# 사용자가 대학 선택
selected_univ = st.selectbox("대학을 선택하세요", univ_list)

# 선택한 대학 정보 보여주기
info = universities[selected_univ]

st.subheader(f"{selected_univ} 정보")
st.write(f"- 수능 점수대: {info['score_range']}")
st.write(f"- 위치: {info['location']}")
