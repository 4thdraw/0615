
# 문제1: 얼음 기능이 추가된 프리미엄 정수기 함수 정의 만들어주세요.

def hot_and_cold_purifier(temperature):
    print("💧 정수기 필터를 통과하는 중...")
    
    if temperature == "찬물":
        return "🥛 시원한 찬물 한 잔"
    elif temperature == "더운물":
        return "☕ 따뜻한 더운물 한 잔"
    else:
        return "❌ 올바른 선택이 아닙니다. (찬물 또는 더운물을 선택하세요)"

# 🛑 실행식 (각각 호출해보며 비교)
drink_A = hot_and_cold_purifier("찬물")
print(f"결과물: {drink_A}")

drink_B = hot_and_cold_purifier("더운물")
print(f"결과물: {drink_B}\n")

# 문제2: 매개인자없이 그냥 실행하면 찬물이 나오는 정수기로 만들어주세요.

def default_purifier(temperature="찬물"):
    print("💧 정수기 필터를 통과하는 중...")
    
    if temperature == "찬물":
        return "🥛 시원한 찬물 한 잔"
    elif temperature == "더운물":
        return "☕ 따뜻한 더운물 한 잔"
    elif temperature == "얼음":
        return "🧊 컵에 가득 담긴 각얼음"
    else:
        return "❌ 올바른 선택이 아닙니다. (찬물, 더운물, 얼음 중 선택하세요)"

# 🛑 문제 2 실행식
print("--- 문제 2: 기본값 테스트 ---")
# 1. 인자를 아무것도 넣지 않고 호출 (자동으로 '찬물'이 선택됨)
drink_default = default_purifier()
print(f"결과물 (인자 없음): {drink_default}")

# 2. 인자로 '얼음'을 넣고 호출 (내가 선택한 '얼음'이 나옴)
drink_custom = default_purifier("얼음")
print(f"결과물 (인자 '얼음'): {drink_custom}")
