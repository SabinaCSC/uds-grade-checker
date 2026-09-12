import streamlit as st

st.set_page_config(
    page_title="UDS Grade Checker",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 UDS Grade Checker")
st.caption("Developed by Sabina Awenchiiminoi Akanko • BSc Computer Science • UDS Nyankpala")

name = st.text_input("Student Name")

score = st.number_input(
    "Enter Score",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("Check Grade"):

    if score >= 80:
        grade = "Grade A"
    elif score >= 75:
        grade = "Grade B+"
    elif score >= 70:
        grade = "Grade B"
    elif score >= 65:
        grade = "Grade C+"
    elif score >= 60:
        grade = "Grade C"
    elif score >= 50:
        grade = "Pass"
    else:
        grade = "Fail"

    st.success(f"🎉 {name}, your result is: {grade}")

    st.write("### Result Summary")
    st.write(f"**Student:** {name}")
    st.write(f"**Score:** {score}")
    st.write(f"**Grade:** {grade}")
