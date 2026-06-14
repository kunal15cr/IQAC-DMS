import streamlit as st
st.title("Research Projects")
from utility import insert_data, read_database



st.markdown("""
<style>

div[data-testid="stExpander"] {
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

div[data-testid="stExpander"] details summary {
    background-color: #f8f9fa;
    padding: 12px;
    font-size: 18px;
    font-weight: 600;
}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

div[data-testid="stFormSubmitButton"] button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Dropdown Data
# -----------------------------
DIVISIONS = [
    "Division 1",
    "Division 2",
    "Division 3",
    "Division 4"
]

SCHOOLS = [
    "School of Engineering & Technology",
    "School of Computer Engineering & Technology",
    "School of Business",
    "School of Leadership",
    "School of Economics and Commerce",
    "School of Government",
    "School of Health Sciences and Technology",
    "School of Science and Environmental Studies",
    "School of Design",
    "School of Liberal Arts",
    "School of Law"
]

DEPARTMENTS = [
    "Department of Civil Engineering",
    "Department of Electrical and Electronics Engineering",
    "Department of Mechanical Engineering",
    "Department of Materials Science and Engineering",
    "Department of Chemical Engineering",
    "Department of Petroleum Engineering",
    "Department of Polymer Engineering",
    "Department of Computer Engineering and Technology",
    "Department of Computer Science and Applications",
    "Department of Business",
    "Department of Hospitality Management",
    "Department of Economics and Public Policy",
    "Department of Commerce and Accounting",
    "Department of Pharmaceutical Sciences",
    "Department of Clinical Sciences",
    "Department of Public Health",
    "Department of Wellness and Yogic Science",
    "Department of Biosciences and Technology",
    "Department of Physics",
    "Department of Chemistry",
    "Department of Mathematics and Statistics",
    "Department of Environmental Studies",
    "Department of Visual Arts",
    "Department of Design",
    "Department of Liberal Arts",
    "Department of Media and Communication",
    "Department of Peace Studies",
    "Department of Photography",
    "Department of Education",
    "Dadasaheb Phalake Film Institute of Technology",
    "School of Law"
]

# -----------------------------
# Form
# -----------------------------
with st.expander("📋 Research Project Submission Form", expanded=True):

    with st.form("research_project_form"):

        col1, col2 = st.columns(2)

        with col1:
            division = st.selectbox(
                "Division *",
                ["Select Division"] + DIVISIONS
            )

           

            department = st.selectbox(
                "Department *",
                ["Select Department"] + DEPARTMENTS
            )

            project_title = st.text_input("Project Title *")

            sanctioned_grant = st.text_input("Sanctioned Grant *")

            grant_year = st.text_input("Grant Year *")
            

        with col2:
            school = st.selectbox(
                "School *",
                ["Select School"] + SCHOOLS
            )

            

            pi_co_pi = st.text_input("PI / Co-PI *")

            funding_agency = st.text_input("Funding Agency *")


           

            sanction_date = st.date_input("Sanction Date *")

            

            sanction_letter_link = st.text_input(
                "Sanction Letter Link *"
            )

        # Optional Field
        abstract = st.text_area(
            "Abstract (Optional)",
            height=150
        )

        submit_button = st.form_submit_button(
            "🚀 Submit Project"
        )

# -----------------------------
# Validation
# -----------------------------
if submit_button:

    required_fields = {
        "Division": division if division != "Select Division" else "",
        "School": school if school != "Select School" else "",
        "Department": department if department != "Select Department" else "",
        "PI / Co-PI": pi_co_pi,
        "Project Title": project_title,
        "Funding Agency": funding_agency,
        "Grant Year": grant_year,
        "Sanctioned Grant": sanctioned_grant,
        "Sanction Letter Link": sanction_letter_link
    }

    missing_fields = [
        field
        for field, value in required_fields.items()
        if not str(value).strip()
    ]

    if missing_fields:

        st.error(
            "Please fill all required fields:\n\n• "
            + "\n• ".join(missing_fields)
        )

    else:

        st.success("✅ Form Submitted Successfully!")

        insert_data.insert_research_project(
            division,
            school,
            department,
            pi_co_pi,
            project_title,
            funding_agency,
            grant_year,
            abstract,
            sanction_date,
            sanctioned_grant,
            sanction_letter_link
)

        st.dataframe(
            {
                "Field": [
                    "Division",
                    "School",
                    "Department",
                    "PI / Co-PI",
                    "Project Title",
                    "Funding Agency",
                    "Grant Year",
                    "Sanction Date",
                    "Sanctioned Grant",
                    "Sanction Letter Link",
                    "Abstract"
                ],
                "Value": [
                    division,
                    school,
                    department,
                    pi_co_pi,
                    project_title,
                    funding_agency,
                    grant_year,
                    sanction_date,
                    sanctioned_grant,
                    sanction_letter_link,
                    abstract
                ]
            },
            use_container_width=True,
            hide_index=True
        )



if st.button("show all data", type="primary"):
    st.dataframe(read_database.Get_data())