# Bridging-Academic-Skill-Gap
Working prototype to help students identify skill gaps and find learning resources.
# Bridging the Academic Skill Gap

**Team Name:** RTC Dominators  
**Team ID:** HSC|TN|01007  
**State:** Tamil Nadu

## 1. Project Overview

Bridging the Academic Skill Gap is a web application that helps students identify the difference between their current skill levels and the skills required for their desired careers.

## 2. Problem Statement

Students may have academic knowledge but lack some of the practical or technical skills expected by employers. Identifying these gaps can help students plan their learning more effectively.

## 3. Proposed Solution

The application allows students to select a career, rate their current skills, compare them with target skill levels, and receive learning recommendations.

## 4. Features

- Career goal selection
- Student skill-level assessment
- Skill-gap calculation
- Personalized learning suggestions
- Summary of total skill gaps

## 5. Technology Stack

- Python
- Streamlit
- GitHub for source code management
- Streamlit Community Cloud for deployment

## 6. Project Structure

```text
bridging-academic-skill-gap/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── docs/
│   └── technical-design.md
├── data/
│   └── sample_data.csv
└── tests/
    └── test_cases.md
```

The folders and files listed above will be added as the project documentation is completed.

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- pip package installer
- Git (optional, for cloning the repository)

### Clone the repository

```bash
git clone https://github.com/RTC DOMINATORS/bridging-academic-skill-gap.git
cd bridging-academic-skill-gap
```

Replace `RTC DOMINATORS` with your actual GitHub username.

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal to use the application.

## 8. Environment Variables

The current prototype does not require environment variables or API keys.

If external services are added in future versions, configure their credentials securely and never commit secrets to GitHub.

## 9. How to Use

1. Open the application.
2. Select a career goal.
3. Rate your current skills from 1 to 5.
4. Click **Analyze My Skill Gaps**.
5. Review the calculated skill gaps and learning recommendations.

## 10. Testing

The prototype should be tested with different career choices and skill levels. Sample data, test cases, and observed test results will be documented in the project repository.

## 11. Future Enhancements

- Personalized learning-resource links
- Student progress tracking
- More career paths and skill assessments
- Industry-aligned skill requirements
- Student dashboards and progress reports

## 12. License

This project is released under the MIT License. See the `LICENSE` file for details.


https://bridging-academic-skill-gap-hmjs4ewqkjmhygevipqtne.streamlit.app/
