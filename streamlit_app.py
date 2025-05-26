import streamlit as st
import numpy as np

st.title("台北市房價預算預估工具")

st.markdown("請輸入您理想的房屋條件：")

# 面積區間（坪）
area_min = st.number_input("面積最小值（坪）", min_value=0.0, value=20.0, step=1.0)
area_max = st.number_input("面積最大值（坪）", min_value=area_min, value=40.0, step=1.0)

# 屋齡區間（年）
age_min = st.number_input("屋齡最小值（年）", min_value=0.0, value=0.0, step=1.0)
age_max = st.number_input("屋齡最大值（年）", min_value=age_min, value=20.0, step=1.0)

# 人口密度（人／平方公里）
density = st.number_input("人口密度（人／平方公里）", min_value=0.0, value=20000.0, step=100.0)

# 中位數年收入（萬元）
income = st.number_input("中位數年收入（萬元）", min_value=0.0, value=150.0, step=1.0)

# 治安：每萬人刑案數（件／萬人）
crime = st.number_input("每萬人刑案數（件／萬人）", min_value=0.0, value=100.0, step=1.0)

# 學區（是否為明星學區）
school = st.selectbox("是否為明星學區", ["否", "是"])
school = 1 if school == "是" else 0

# 捷運（是否有捷運站）
mrt = st.selectbox("是否鄰近捷運站", ["否", "是"])
mrt = 1 if mrt == "是" else 0

# 預估價格區間
if st.button("預估總價區間"):

    results = []

    for area in np.linspace(area_min, area_max, num=3):  # 取3個範圍內的值
        for age in np.linspace(age_min, age_max, num=3):

            # 回歸模型公式：
            price = (
                -1689.059
                + 106.896 * area
                + 0.036 * density
                - 22.487 * age
                + 1.451 * income
                + 138.750 * mrt
                + 320.117 * school
                + 1.071 * crime
            )
            results.append(price)

    st.subheader("預估總價範圍（萬元）：")
    st.success(f"{round(min(results))} 萬元 ～ {round(max(results))} 萬元")
