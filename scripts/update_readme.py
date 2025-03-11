import os
import matplotlib.pyplot as plt

def extract_metadata(file_path):
    metadata = {
        "Problem": "Unknown",
        "Difficulty": "Unknown",
        "Time Taken": "Unknown",
        "Attempts": "Unknown",
        "Hints Used": "Unknown",
        "Notes": "None",
        "Status": "Unsolved"
    }
    
    with open(file_path, "r", encoding="utf-8") as f:
        has_code = False
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                parts = line[1:].split(":", 1)
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip()
                    if key in metadata:
                        metadata[key] = value
            elif line:  # If there's non-commented code, mark as solved
                has_code = True
                
        if has_code:
            metadata["Status"] = "Solved"
    
    return metadata

def count_problems():
    base_dir = os.path.join("..", "code")
    problems = []
    
    if os.path.exists(base_dir):
        for category in os.listdir(base_dir):
            category_path = os.path.join(base_dir, category)
            if os.path.isdir(category_path):
                for file in os.listdir(category_path):
                    file_path = os.path.join(category_path, file)
                    metadata = extract_metadata(file_path)
                    problems.append((metadata, category))
    
    return problems

def generate_progress_bar(solved, total, length=20):
    if total == 0:
        return "No problems available yet."
    
    progress = int((solved / total) * length)
    return f"[{'█' * progress}{'-' * (length - progress)}] {solved}/{total} solved"

def generate_pie_chart(solved, total):
    labels = ["Solved", "Unsolved"]
    sizes = [solved, total - solved]
    colors = ["#4CAF50", "#FF3D00"]
    
    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
    plt.axis("equal")
    
    chart_path = "../progress_chart.png"
    plt.savefig(chart_path)
    plt.close()
    
    return chart_path

def update_readme():
    problems = count_problems()
    total_solved = sum(1 for metadata, _ in problems if metadata["Status"] == "Solved")
    total_problems = len(problems)
    
    progress_bar = generate_progress_bar(total_solved, total_problems)
    chart_path = generate_pie_chart(total_solved, total_problems)
    
    readme_path = "../README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# LeetCode Progress Tracker 🚀\n")
        f.write("\n## 📊 Progress Overview\n")
        f.write(f"- **Total Problems**: {total_problems}\n")
        f.write(f"- **Total Solved**: {total_solved}\n")
        f.write(f"- **Progress:** {progress_bar}\n")
        f.write(f"\n![Progress Chart](progress_chart.png)\n")
        f.write("\n## 📌 Problem List\n")
        f.write("| #  | Problem | Category | Difficulty | Time Taken | Attempts | Hints Used | Notes | Status |\n")
        f.write("|----|---------|----------|------------|------------|----------|------------|-------|--------|\n")
        
        for idx, (metadata, category) in enumerate(problems, start=1):
            f.write(f"| {idx} | {metadata['Problem']} | {category} | {metadata['Difficulty']} | {metadata['Time Taken']} | {metadata['Attempts']} | {metadata['Hints Used']} | {metadata['Notes']} | {metadata['Status']} |\n")
        
update_readme()