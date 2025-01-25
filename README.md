# Python Selenium Automation Framework

This repository contains a comprehensive Selenium framework designed for automating various web application testing scenarios. The project is modularized into different directories to ensure scalability, maintainability, and ease of understanding.

---

## 📂 Directory Overview

### `alert_frames_windows/`
Handles alerts, frames, windows, and dropdowns:
- `dynamic_dropdown.py`, `handling_alerts.py`, `handling_frames.py`, `handling_popups.py`, `static_dropdowns.py`

### `elements/`
Automates UI elements and data handling:
- `check_box.py`, `click_buttons.py`, `handling_excel_data.py`, `links.py`, `radio_button.py`, `text_box.py`, `web_tables.py`

### `testCases/`
End-to-end test scripts:
- `loginWebsite.py`, `practice_form.py`, `test.py`

### `test_data/`
Test data files:
- `DEMOQA.xlsx`, `status_text_static_data.json`

### `widgets/`
Widget-specific interactions:
- `auto_suggestions.py`, `calender_type1.py`, `date_formatting.py`

---

## 🚀 Features
- Modular design for scalability.
- Data-driven testing with Excel and JSON.
- Handles dropdowns, pop-ups, frames, and web tables.
- Supports dynamic and static elements.

---

## 🛠️ Prerequisites
Before running the project, ensure you have the following installed:
1. **Python (>=3.8)**: Download from [python.org](https://www.python.org/).
2. **Selenium**: Install via pip:
   pip install selenium

ChromeDriver/GeckoDriver: Compatible with the browser you wish to test on.

Excel Handling Library: Install openpyxl via pip:
pip install openpyxl

⚙️ Setup Instructions

Clone the repository:
git clone https://github.com/your-username/Python_Selenium.git

cd Python_Selenium

Install dependencies:
pip install -r requirements.txt

Update the driver path in the scripts as needed:
python

driver = webdriver.Chrome(executable_path="path/to/chromedriver")

🧪 How to Run Tests
Navigate to the respective test script directory:
cd testCases

Execute the script:
python loginWebsite.py
Review the logs and screenshots for validation.

📊 Test Data
Test data is stored in the test_data/ directory.

Update the DEMOQA.xlsx file or status_text_static_data.json to modify test scenarios as needed.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and create a pull request.

👨‍💻 Author
Sachin Sherki
QA Automation Professional | Passionate about Selenium, Python, and Test Automation.


This `README.md` provides a clear and professional overview of your project while highlighting its structure, features, and usage instructions. Let me know if you'd like to modify anything!

