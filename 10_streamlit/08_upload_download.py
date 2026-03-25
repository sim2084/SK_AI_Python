import streamlit as st
import pandas as pd

st.title("08. 파일 업로드/다운로드 : .csv")

uploaded = st.file_uploader("CSV 파일 업로드",type=["csv"])

if uploaded is None:
    st.info("CSV를 업로드 하면 표/필터/다운로드까지 연결한다.")
    st.stop()

df = pd.read_csv(uploaded)
st.subheader("업로드된 데이터 미리보기")
st.dataframe(df,width="stretch")

#아주 간단한 열 선택 필터 예시
cols = list(df.columns)
selected_cols = st.multiselect("보소 싶은 열 선택", cols, default=cols[:min(5,(len(cols)))])

filtered = df[selected_cols] if selected_cols else df

st.subheader("필터링 된 데이터")
st.dataframe(filtered,width="stretch")

st.divider()

# 다운로드 dataframe -> csv
csv_bytes = filtered.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    label="필터 결과 CSV 다운로드",
    data=csv_bytes,
    file_name="filtered_csv",
    mime="text/csv"
)