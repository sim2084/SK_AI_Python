import streamlit as st

# 앱의 기본 설정을 지정한다.
# page_title: 브라우저 탭 제목
# layout="wide": 화면을 넓게 사용
st.set_page_config(
    page_title="Sales & Inventory Portal",
    layout="wide",
)

st.title("Sales & Inventory Portal")
st.caption("매출 대시보드 / 재고 편집 / 업로드·다운로드를 멀티페이지로 묶는다.")

st.divider()

st.subheader("페이지 안내")
st.write("Sales Dashboard: CSV를 읽고 필터, KPI, 차트를 확인한다.")
st.write("Inventory Editor: data_editor와 session_state로 재고 상태를 편집하고 유지한다.")
st.write("Upload / Download: CSV를 업로드하고 필요한 열만 골라 다시 다운로드한다.")

st.divider()

st.subheader("페이지 이동")
# 멀티페이지 앱에서는 pages 폴더 아래의 각 파일로 이동 링크를 만들 수 있다.
# 경로는 실제 파일명과 정확히 일치해야 한다.
st.page_link("pages/1_sales_dashboard.py", label="1) Sales Dashboard")
st.page_link("pages/2_inventory_editor.py", label="2) Inventory Editor")
st.page_link("pages/3_upload_download.py", label="3) Upload / Download")