# 1단계: 찬물만 나오는 정수기 함수 정의
def basic_purifier():
    print("💧 정수기 필터를 통과하는 중...")
    return "🥛 시원한 찬물 만 있습니다. 선택못함"

# 🛑 실행식
my_drink = basic_purifier()
print(f"결과물: {my_drink}\n")


# 2단계: 냉/온수 선택이 가능한 정수기 함수 정의
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


# 문제1: 얼음 기능이 추가된 프리미엄 정수기 함수 정의 만들어주세요.

# 문제2: 매개인자없이 그냥 실행하면 찬물이 나오는 정수기로 만들어주세요.

