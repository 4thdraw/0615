import time  # 시간 지연(딜레이) 기능을 쓰기 위해 가져옵니다.

def premium_purifier(temperature="찬물"):
    # 1. 정수 프로세스 시작 알림
    print("🔔 정수기가 작동합니다. 잠시만 기다려주세요...")
    
    # 2. 물방울이 1초 간격으로 하나씩 총 5개 출력되는 반복문
    # (엔터를 치지 않고 옆으로 나란히 출력하기 위해 end=" "를 사용합니다)
    for i in range(5):
        time.sleep(1)  # 1초 동안 멈춤
        print("💧", end=" ", flush=True)
        # flush=True가 없으면 물방울이 1초에 하나씩 안 나오고, 5초 동안 가만히 있다가 마지막에 💧 💧 💧 💧 💧가 한 번에 와르르
    
    print("\n" + "-" * 30) # 물방울 출력이 끝나면 줄바꿈 후 구별선 긋기
    
    # 3. 매개인자 선택에 따른 최종 결과물 리턴
    if temperature == "찬물":
        return "🥛 시원한 찬물 한 잔이 나왔습니다."
    elif temperature == "더운물":
        return "☕ 따뜻한 더운물 한 잔이 나왔습니다."
    elif temperature == "얼음":
        return "🧊 컵에 가득 담긴 각얼음이 나왔습니다."
    else:
        return "❌ 올바른 선택이 아닙니다. (찬물, 더운물, 얼음 중 선택)"

# 🛑 실행식
print("--- [테스트 1] 인자 없이 실행 (기본 찬물) ---")
drink_1 = premium_purifier()
print(drink_1)
print("\n" + "=" * 40 + "\n")

print("--- [테스트 2] '얼음' 선택 시 ---")
drink_2 = premium_purifier("얼음")
print(drink_2)