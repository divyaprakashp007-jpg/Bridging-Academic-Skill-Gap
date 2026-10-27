
import streamlit as st

st.set_page_config(
    page_title="Skill Gap Analyzer",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Bridging the Academic Skill Gap")
st.write(
    "Discover your skill gaps and find out what you need to learn "
    "for your dream career."
)

st.subheader("1. Choose your career goal")

career = st.selectbox(
    "Select a career",
    ["Software Developer", "Data Analyst", "AI Engineer"]
)

career_skills = {
    "Software Developer": {
        "Python": 4,
        "Problem Solving": 4,
        "Communication": 3
    },
    "Data Analyst": {
        "Python": 3,
        "Data Analysis": 5,
        "Communication": 4
    },
    "AI Engineer": {
        "Python": 5,
        "Mathematics": 5,
        "Machine Learning": 4
    }
}

st.subheader("2. Rate your current skills")

student_levels = {}

for skill in career_skills[career]:
    student_levels[skill] = st.slider(
        f"{skill} (1 = Beginner, 5 = Advanced)",
        min_value=1,
        max_value=5,
        value=2
    )

if st.button("Analyze My Skill Gaps"):
    st.subheader("3. Your Skill Gap Report")

    total_gap = 0

    for skill, required_level in career_skills[career].items():
        current_level = student_levels[skill]
        gap = max(0, required_level - current_level)
        total_gap += gap

        st.write(f"**{skill}**")
        st.write(f"Your level: {current_level}/5")
        st.write(f"Target level: {required_level}/5")
        st.write(f"Skill gap: {gap}")

        if gap > 0:
            st.info(
                f"Recommended action: Practice {skill} "
                "and complete a related learning course."
            )
        else:
            st.success(f"You have reached the target for {skill}!")

    st.metric("Total skill gap", total_gap)

    if total_gap > 0:
        st.write(
            "Start with the skills that have the largest gaps "
            "and track your progress as you learn."
        )
    else:
        st.balloons()
        st.success("Excellent! You meet all the selected skill targets.")
