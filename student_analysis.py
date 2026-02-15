import pandas as pd
import matplotlib.pyplot as plt

print("===== Student Result Analysis Program Started =====")

# Read CSV file
df = pd.read_csv("student_marks.csv")

print("\nStudent Data:")
print(df)

# Total & Average Marks
df["Total_Marks"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average_Marks"] = df["Total_Marks"] / 3

# Grade Function
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Average_Marks"].apply(get_grade)

print("\nFinal Data:")
print(df)

# ---------------- GRAPH 1: Subject-wise Average ----------------
subject_avg = {
    "Maths": df["Maths"].mean(),
    "Science": df["Science"].mean(),
    "English": df["English"].mean()
}

plt.figure()
plt.bar(subject_avg.keys(), subject_avg.values())
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# ---------------- GRAPH 2: Student Total Marks ----------------
plt.figure()
plt.plot(df.index + 1, df["Total_Marks"], marker='o')
plt.title("Total Marks of Students")
plt.xlabel("Student Number")
plt.ylabel("Total Marks")
plt.show()

# ---------------- GRAPH 3: Grade Distribution ----------------
grade_count = df["Grade"].value_counts()

plt.figure()
plt.bar(grade_count.index, grade_count.values)
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()

# ---------------- GRAPH 4: Subject Comparison (Box Plot) ----------------
plt.figure()
plt.boxplot([df["Maths"], df["Science"], df["English"]],
            labels=["Maths", "Science", "English"])
plt.title("Subject-wise Marks Distribution")
plt.ylabel("Marks")
plt.show()

# Save Final Result
df.to_csv("final_result.csv", index=False)
print("\nFinal result saved as final_result.csv")

print("===== Program Finished Successfully =====")