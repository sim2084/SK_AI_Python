import streamlit as st
import pandas as pd

st.title("1) Sales Dashboard")

# data 폴더에 있는 CSV 파일을 읽어온다.
# parse_dates를 사용하면 date 열을 날짜형으로 바로 읽을 수 있다.
try:
    df = pd.read_csv("final_app\data\sales.csv", parse_dates=["date"])
except FileNotFoundError:
    st.error("data/sales.csv 파일을 찾을 수 없습니다.")
    st.stop()

st.sidebar.header("필터")

# CSV에 들어 있는 실제 값으로 필터 목록을 만든다.
regions = sorted(df["region"].unique().tolist())
products = sorted(df["product"].unique().tolist())

region = st.sidebar.selectbox("지역", ["전체"] + regions)
product = st.sidebar.selectbox("제품", ["전체"] + products)

min_d = df["date"].min().date()
max_d = df["date"].max().date()
date_range = st.sidebar.date_input("기간", value=(min_d, max_d))

# date_input은 단일 날짜 또는 날짜 범위를 반환할 수 있으므로 방어 코드를 둔다.
if not isinstance(date_range, (tuple, list)) or len(date_range) != 2:
    st.warning("기간은 시작일과 종료일 2개를 선택하는 것을 권장한다.")
    st.stop()

start = pd.to_datetime(date_range[0])
end = pd.to_datetime(date_range[1])

# 먼저 날짜 기준으로 필터링한다.
filtered = df[(df["date"] >= start) & (df["date"] <= end)]

# 전체가 아닌 경우에만 추가 필터를 적용한다.
if region != "전체":
    filtered = filtered[filtered["region"] == region]

if product != "전체":
    filtered = filtered[filtered["product"] == product]

if filtered.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다.")
    st.stop()

st.subheader("요약 지표")
c1, c2, c3 = st.columns(3)

total_sales = int(filtered["sales"].sum())
total_orders = int(filtered["orders"].sum())
avg_order_value = int(total_sales / total_orders) if total_orders > 0 else 0

with c1:
    st.metric("총 매출", f"₩{total_sales:,}")

with c2:
    st.metric("총 주문", f"{total_orders:,}")

with c3:
    st.metric("평균 주문금액", f"₩{avg_order_value:,}")

st.divider()

st.subheader("일자별 매출 추이")

# 날짜별 매출 합계를 구한 뒤 line_chart에 넣는다.
by_day = (
    filtered
    .groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

chart_df = by_day.set_index("date")
st.line_chart(chart_df)

st.divider()

st.subheader("원천 데이터")
st.dataframe(filtered, width="stretch", hide_index=True)