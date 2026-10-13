
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Patient Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# Dashboard title
st.title("🏥 Patient Analytics Dashboard")
st.write("Analyze patient counts by day of the week.")

# Upload CSV file
uploaded_file = st.file_uploader(
    "Upload your patient data CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        test_3_data = pd.read_csv(uploaded_file)

        # Validate required columns
        required_columns = ["Day", "PATIENTNAME"]
        missing_columns = [
            col for col in required_columns
            if col not in test_3_data.columns
        ]

        if missing_columns:
            st.error(
                f"Missing required columns: {', '.join(missing_columns)}"
            )

        else:
            # Count patients by day
            result = (
                test_3_data
                .groupby("Day")["PATIENTNAME"]
                .count()
                .reset_index()
            )

            result.columns = ["Day", "Patient_Count"]

            # Display summary data
            st.subheader("Patient Count by Day")
            st.dataframe(result, use_container_width=True)

            # Create bar chart
            fig, ax = plt.subplots(figsize=(8, 5))

            ax.bar(
                result["Day"],
                result["Patient_Count"],
                color="skyblue",
                edgecolor="black"
            )

            ax.set_xlabel("Day of the Week", fontsize=12)
            ax.set_ylabel("Number of Patients", fontsize=12)
            ax.set_title(
                "Patient Count by Day",
                fontsize=14,
                fontweight="bold"
            )

            ax.grid(
                axis="y",
                linestyle="--",
                alpha=0.7
            )

            fig.tight_layout()

            # Display chart in Streamlit
            st.pyplot(fig)
            plt.close(fig)

            # Show total count
            st.metric(
                "Total Non-Empty Patient Names",
                int(test_3_data["PATIENTNAME"].count())
            )

    except Exception as e:
        st.error(f"Unable to process the CSV file: {e}")

else:
    st.info("Please upload your patient data CSV file to view the dashboard.")
