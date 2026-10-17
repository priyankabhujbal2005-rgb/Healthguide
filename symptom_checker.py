
import streamlit as st


def show_symptom_checker():
    """Display a guided symptom checker for general health education."""

    st.subheader("Guided Symptom Checker")
    st.write(
        "Answer these questions to receive general health guidance. "
        "This tool cannot diagnose a medical condition."
    )

    st.warning(
        "If you have severe chest pain, serious breathing difficulty, "
        "uncontrolled bleeding, sudden facial drooping, or difficulty "
        "speaking, seek emergency medical help immediately."
    )

    with st.form("symptom_checker_form"):
        symptoms = st.multiselect(
            "Which symptoms are you experiencing?",
            [
                "Headache",
                "Fever",
                "Cough",
                "Sore throat",
                "Dizziness",
                "Nausea",
                "Stomach discomfort",
                "Fatigue",
                "Other"
            ]
        )

        duration = st.selectbox(
            "How long have you had these symptoms?",
            [
                "Less than 24 hours",
                "1–3 days",
                "4–7 days",
                "More than 7 days"
            ]
        )

        severity = st.radio(
            "How severe are your symptoms?",
            [
                "Mild",
                "Moderate",
                "Severe"
            ]
        )

        submitted = st.form_submit_button("Get general guidance")

    if submitted:
        if not symptoms:
            st.warning("Please select at least one symptom.")
            return

        st.markdown("### Your summary")
        st.write("**Symptoms:** " + ", ".join(symptoms))
        st.write("**Duration:** " + duration)
        st.write("**Reported severity:** " + severity)

        if severity == "Severe":
            st.error(
                "Severe symptoms need prompt medical assessment. "
                "Please seek urgent medical care now. If symptoms may "
                "be life-threatening, contact emergency services."
            )

        elif duration == "More than 7 days":
            st.warning(
                "Because your symptoms have lasted more than a week, "
                "consider arranging an assessment with a qualified "
                "healthcare professional, especially if symptoms "
                "are worsening or not improving."
            )

        else:
            st.info(
                "Monitor your symptoms and rest as appropriate. "
                "Maintain fluids if you can safely drink them. "
                "Seek professional advice if symptoms persist, worsen, "
                "or concern you."
            )

        st.caption(
            "This educational tool does not diagnose conditions, "
            "recommend medicines, or replace professional medical advice."
        )
