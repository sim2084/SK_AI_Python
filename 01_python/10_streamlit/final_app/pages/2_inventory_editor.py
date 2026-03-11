import streamlit as st
import pandas as pd

st.title("2) Inventory Editor")

# session_state에 재고표를 저장해 두면
# 페이지를 다시 실행하거나 다른 페이지로 이동해도 상태를 유지할 수 있다.
if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {"제품": "A", "재고": 30, "단가": 12000},
        {"제품": "B", "재고": 15, "단가": 18000},
        {"제품": "C", "재고": 50, "단가": 9000},
    ])

st.subheader("재고표 편집")

edited = st.data_editor(
    st.session_state.inventory,
    num_rows="dynamic",
    width="stretch",
    hide_index=True,
    column_config={
        "제품": st.column_config.TextColumn("제품", required=True),
        "재고": st.column_config.NumberColumn("재고", min_value=0, step=1),
        "단가": st.column_config.NumberColumn("단가", min_value=0, step=100),
    },
)

# 편집 결과를 다시 저장해야 다음에도 유지된다.
st.session_state.inventory = edited

st.divider()

st.subheader("간단 요약")
total_items = int(edited["재고"].sum()) if len(edited) else 0
total_amount = int((edited["재고"] * edited["단가"]).sum()) if len(edited) else 0

c1, c2 = st.columns(2)

with c1:
    st.metric("총 재고 수량", total_items)

with c2:
    st.metric("총 재고 금액", f"₩{total_amount:,}")

st.caption("data_editor + session_state 조합은 업무용 내부 툴에서 매우 자주 쓰인다.")