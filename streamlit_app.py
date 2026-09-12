import streamlit as st

st.set_page_config(
    page_title="UDS Grade Checker",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 UDS Grade Checker")

st.caption(
    "Developed by Sabina Akanko Awenchiiminoi • "
    "BSc Computer Science • UDS Nyankpala"
)

st.divider()

name = st.text_input("👤 Student Name")

score = st.number_input(
    "📝 Enter Score",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("🔍 Check Grade", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter the student's name.")

    else:

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

        st.divider()

        st.subheader("📊 Result Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Student", name)

        with col2:
            st.metric("Score", f"{score}/100")

        with col3:
            st.metric("Grade", grade)
