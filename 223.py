import streamlit as st

st.text_input(label, type="password")
# OpenAI API 키 설정
openai.api_key = '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'  # 실제 API 키로 변경하세요

# Streamlit 앱 제목
st.title("GPT-4.1-mini 모델 응답 출력기")

# 사용자로부터 질문 입력 받기
user_input = st.text_input("질문을 입력하세요:")

# 질문이 입력되었을 때 OpenAI API 호출
if user_input:
    try:
        # OpenAI API로 GPT-4.1-mini 모델에 요청
        response = openai.Completion.create(
            model="gpt-4.1-mini",  # GPT-4.1-mini 모델 사용
            prompt=user_input,     # 사용자가 입력한 질문
            max_tokens=150         # 최대 토큰 수 (응답 길이 조절)
        )
        
        # 모델의 응답 출력
        answer = response.choices[0].text.strip()  # 모델의 첫 번째 응답을 가져옴
        st.write("응답:", answer)
    
    except Exception as e:
        st.write(f"에러 발생: {e}")
