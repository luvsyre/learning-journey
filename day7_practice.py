project_day = 7
status = 'In Progress'
total_days = 14
days_remaining = total_days - project_day
print(f"Project Summary: Day {project_day} ({status}). We have {days_remaining} days left to reach the finish line!")
if days_remaining < 5:
    print("⚠️ WARNING: Deadline is approaching quickly!")
else:
    print("Keep up the pace. Progress is steady.")