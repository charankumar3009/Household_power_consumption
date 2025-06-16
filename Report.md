# Energy Consumption Analysis - Project Report

## Problem Statement

Energy usage is a significant cost and environmental factor for households. This project analyzes a detailed household electric power consumption dataset to extract usage patterns and provide recommendations for optimizing electricity consumption.

---

## Methodology

- **Data Loading:** Imported data from Kaggle, handled missing values, and parsed date/time.
- **Cleaning:** Dropped rows with missing data, converted columns to numeric types, and set a DateTime index.
- **Exploratory Data Analysis:**
    - Calculated total, average, max, and min consumption.
    - Resampled data to daily, weekly, monthly frequencies.
    - Visualized daily and hourly consumption patterns.
    - Analyzed average usage by day of week.
- **Additional Analysis:**
    - Checked correlation between voltage and consumption.
    - Identified periods of unusually high consumption.
    - Added features for day of week and weekend/weekday.

---

## Key Insights

- **Consumption Peaks:** Evening hours (6–9 PM) are periods of highest usage.
- **Weekly Trends:** Consumption is higher on weekdays than weekends.
- **Voltage Link:** Minimal correlation between voltage and power consumed.
- **Anomalies:** Occasional high-usage periods point to potential inefficiencies or unusual activity.
- **Weekend Effect:** Slightly lower consumption on weekends.

---

## Recommendations

- **Optimize Appliance Use:** Operate major appliances during off-peak hours.
- **Investigate Spikes:** Review days with high usage for inefficient or malfunctioning devices.
- **Focus on Evenings:** Apply energy-saving strategies during peak evening hours.
- **Continuous Tracking:** Use data visualization tools for ongoing monitoring and optimization.



