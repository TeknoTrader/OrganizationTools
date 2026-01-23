# 📚 DailyTask Organizer by Nicola Chimenti

A **smart web application** built with **Streamlit** that helps you create realistic study plans and work schedules to reach your goals on time.  
Whether you're preparing for an exam, completing a project, or managing tasks with a deadline, this tool calculates how much you need to work each day and shows you different scenarios to balance productivity and rest.

🌐 **[Try the live app here](https://organizationtools.streamlit.app/)**

---

## 🎯 Purpose

This web app is designed to:
- **Calculate daily workload** based on your deadline and total tasks/pages
- **Generate multiple study/work scenarios** with different amounts of rest days
- **Visualize your options** through interactive charts and tables
- **Help you set realistic goals** and avoid burnout by planning rest days

Perfect for students, freelancers, project managers, and anyone who wants to organize their time efficiently.

---

## ✨ Key Features

### 📅 Smart Date Selection
- Input your exam or project deadline with validation
- Automatic detection of invalid dates (e.g., February 31st)
- Real-time calculation of days remaining

### 📊 Workload Calculator
- Enter the total number of pages to study or tasks to complete
- Get instant daily average calculations
- Results rounded to practical integer values

### 🧘‍♀️ Rest Day Planner
A powerful feature that shows you **multiple organization strategies**:
- Define how many rest days you want
- See how many pages/tasks you'll need to complete per day
- Visual bar chart comparing different scenarios
- Detailed table with customizable decimal precision

### 📈 Interactive Visualizations
- **Bar charts** showing workload vs. rest days
- **Data tables** with normal or extended view
- **Downloadable CSV** for further analysis
- **Styled tables** with visual bars for better readability

---

## 🖥️ How It Works

1. **Set Your Deadline**: Choose the year, month, and day of your exam or project deadline
2. **Enter Your Workload**: Input the total number of pages to study or tasks to complete
3. **View Basic Calculation**: See how many pages/tasks you need to do per day
4. **Explore Scenarios** *(optional)*: Adjust the interval progression and decimal precision to see different work-rest balance options
5. **Choose Your Plan**: Pick the scenario that fits your lifestyle and work capacity

---

## 🚀 Installation & Usage

### Run Locally

1. Clone the repository:
```bash
git clone https://github.com/TeknoTrader/OrganizationTools.git
cd OrganizationTools
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the app:
```bash
streamlit run DailyTask_WEBAPP.py
```

4. Open your browser at `http://localhost:8501`

### Use Online

Simply visit the **[live web app](https://organizationtools.streamlit.app/)** — no installation required!

---

## 📦 Requirements

The app uses the following Python libraries:
- **streamlit** — for the web interface
- **pandas** — for data manipulation and tables
- **matplotlib** — for chart visualization
- **numpy** — for numerical calculations

See `requirements.txt` for complete dependency list.

---

## 🎓 Use Cases

### For Students
- Plan exam preparation with optimal daily page counts
- Balance study sessions with rest days
- Avoid last-minute cramming

### For Professionals
- Organize project tasks with realistic daily targets
- Manage deadlines across multiple projects
- Visualize workload distribution

### For Personal Goals
- Plan reading challenges
- Organize course completions
- Manage any time-bound objectives

---

## 💡 Example Scenario

**Goal**: Read a 300-page book before an exam in 20 days

**Basic calculation**: ~15 pages per day

**With rest days**:
- 3 days off → ~18 pages/day
- 5 days off → ~20 pages/day  
- 7 days off → ~23 pages/day

Choose the scenario that matches your reading speed and schedule!

---

## 🛠️ Technical Details

- Built with **Python 3.x**
- Powered by **Streamlit** framework
- Responsive design for desktop and mobile
- Real-time calculations with instant feedback
- Error handling for edge cases

---

## 💬 Feedback & Support

Found a bug or have a suggestion? I'd love to hear from you!

- 🖥️ Website: **[My website](https://www.nicolachimenti.com)** (in italian!)
- 📧 Email: **preventivi@nicolachimenti.com**
- 🔗 LinkedIn: **[Nicola Chimenti](https://www.linkedin.com/in/nicolachimenti)**
- 💼 Fiverr: **[teknonicola](https://www.fiverr.com/sellers/teknonicola/)**

---

## 📜 License

This project is open source and available for personal and educational use.  
Feel free to fork, modify, and share with proper attribution.

---

## 👤 About the Developer

**Nicola Chimenti**  
MQL4 Developer & Business Analyst

Passionate about creating practical tools that solve real-world problems through code.

---

⭐ **If this tool helps you stay organized, consider giving the repository a star — it supports future development!**
