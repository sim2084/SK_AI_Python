import streamlit as st
import pandas as pd

st.title("3) Upload / Download")

st.subheader("CSV 업로드")
uploaded = st.file_uploader("CSV 업로드", type=["csv"])

if uploaded is None:
    st.info("CSV를 올리면 미리보기와 다운로드를 제공한다.")
else:
    # 업로드된 CSV를 DataFrame으로 읽는다.
    df = pd.read_csv(uploaded)

    cols = list(df.columns)
    selected_cols = st.multiselect("보고 싶은 열 선택", cols, default=cols)

    filtered = df[selected_cols] if selected_cols else df
    st.dataframe(filtered, width="stretch")

    st.divider()

    st.subheader("CSV 다운로드(현재 표 그대로)")
    # utf-8-sig는 Excel에서 한글 깨짐을 줄이기 위해 자주 사용한다.
    csv_bytes = filtered.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "다운로드",
        data=csv_bytes,
        file_name="uploaded.csv",
        mime="text/csv",
    )

st.divider()
st.subheader("재고표도 다운로드(session_state 연동)")

if "inventory" in st.session_state:
    inv = st.session_state.inventory
    inv_bytes = inv.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "재고 CSV 다운로드",
        data=inv_bytes,
        file_name="inventory.csv",
        mime="text/csv",
    )
else:
    st.warning("먼저 'Inventory Editor' 페이지에서 재고표를 생성하거나 편집하세요.")