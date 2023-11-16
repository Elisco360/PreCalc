import streamlit as st

st.set_page_config(layout="wide")


def main():
    st.title("Eii! ")

    st.info("This software is supposed to help you forecast your score for exam")

    st.markdown("<hr>", unsafe_allow_html=True)

    l, m, r = st.columns([3, 2, 6])

    with l:
        st.header("Inputs")
        percentage = st.selectbox("Final exam percentage (%)", options=[40, 30, 20, 15, 10])
        curr = st.number_input("Enter your current CANVAS score", min_value=0.00, max_value=100.00)
        st.markdown("\n")
        st.markdown("\n")

        submit = st.button("Let's go ⚡")

        curr_score = curr * (100-percentage)/100

    if submit:
        with r:
            with st.expander("Open for a surprise 🎁"):
                st.divider()

                grades = {"A+": 85, "A": 80, "B+": 75, "B": 70, "C+": 65, "C": 60, "D+": 55}
                new_grades = {}
                for grade, value in grades.items():
                    if value-curr_score >= percentage:
                        new_grades[grade] = "Chale ecast wai 💀😭🤣🤣"
                    else:
                        new_grades[grade] = f"{round((value - curr_score) * 2.5, 2)} or more"
                st.dataframe(new_grades)


if __name__ == '__main__':
    main()
