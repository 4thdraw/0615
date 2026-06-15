import pandas as pd
import matplotlib.pyplot as plt

# 1. 1월부터 5월까지의 정수기 등급별 판매량 데이터 생성
데이터 = {
    "월": ["1월", "2월", "3월", "4월", "5월"],
    "싼거": [50, 65, 45, 70, 55],
    "기본": [80, 85, 90, 105, 110],
    "비싼거": [20, 35, 40, 60, 85]
}

# 2. 딕셔너리 데이터를 판다스의 DataFrame(표 형태)으로 변환
표 = pd.DataFrame(데이터)

# 3. 데이터 시각화 (그래프 그리기) 설정
# 한글 폰트 깨짐 방지 (윈도우 기준 맑은 고딕 설정) -> rc 함수는 '기본 스타일 환경 설정'을 통째로 제어(Control)하는 기능
plt.rc('font', family='Malgun Gothic')

# 그래프 크기 설정 및 선 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(표["월"], 표["싼거"], marker='o', label="싼거 (찬물)", color='#42a5f5', linewidth=2)
plt.plot(표["월"], 표["기본"], marker='s', label="기본 (찬물+더운물)", color='#ffb74d', linewidth=2)
plt.plot(표["월"], 표["비싼거"], marker='^', label="비싼거 (얼음추가)", color='#ef5350', linewidth=2)

# 4. 그래프 꾸미기 (제목, 축 이름, 범례)
plt.title("📈 정수기 공장 등급별 월간 판매 현황", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("판매 월", fontsize=12)
plt.ylabel("판매량 (대)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) # 배경 격자무늬
plt.legend(fontsize=11) # 범례 표시

# 5. 그래프 화면에 띄우기
plt.show()