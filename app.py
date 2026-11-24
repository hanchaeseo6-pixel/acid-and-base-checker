import streamlit as st

# 1. 리스트(list) 선언 - 산성 5개, 염기성 5개 총 10개 (snake_case 준수)
formulas = [
    "HCl", "H2SO4", "HNO3", "CH3COOH", "H2CO3",
    "NaOH", "KOH", "Ca(OH)2", "Mg(OH)2", "NH4OH"
]
names = [
    "염산", "황산", "질산", "아세트산(식초)", "탄산",
    "수산화나트륨", "수산화칼륨", "수산화칼슘", "수산화마그네슘", "수산화암모늄(암모니아수)"
]
acid_list = ["HCl", "H2SO4", "HNO3", "CH3COOH", "H2CO3"]
base_list = ["NaOH", "KOH", "Ca(OH)2", "Mg(OH)2", "NH4OH"]

# 2. 함수(def) & 선택구조(if-elif-else)
def check_substance(formula):
    if formula in acid_list:
        return "산성입니다", "수소 이온(H+)을 가지고 있습니다."
    elif formula in base_list:
        return "염기성입니다", "수산화 이온(OH-)을 가지고 있습니다."
    else:
        return "판독 불가", "목록에 없는 화학식입니다."

# 3. Streamlit 웹 화면 구성
st.title("🧪 화학식 기반 산성·염기성 물질 판독기")

selected = st.selectbox("판독할 화학식을 선택하세요:", formulas)

# 버튼을 눌러야만 판독 결과와 이유가 출력됨
if st.button("🔍 산성·염기성 판독하기"):
    result, reason = check_substance(selected)
    idx = formulas.index(selected)
    
    st.metric(label=f"선택한 화학식: {selected} ({names[idx]})", value=result)
    st.info(f"💡 이유: {reason}")

st.divider()

# 4. 반복구조(for)로 판독 가능한 물질 안내 표 출력 (정답 숨김)
st.subheader("📋 판독 가능한 화학식 목록 (총 10종)")
info_list = []
for i in range(len(formulas)):
    info_list.append({
        "화학식": formulas[i],
        "물질명": names[i]
    })
st.table(info_list)
