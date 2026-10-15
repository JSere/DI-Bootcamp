import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.figure(figsize=(7, 4))
plt.plot(days, temperatures, marker='o', color='b', linestyle='-', linewidth=2)
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Variations Over a Week')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'exercise2_temp.png'), dpi=300)
plt.close()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(7, 4))
plt.bar(months, sales, color='skyblue', edgecolor='steelblue')
plt.xlabel('Month')
plt.ylabel('Sales Amount ($)')
plt.title('Monthly Sales Data')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'exercise3_sales.png'), dpi=300)
plt.close()

file_path = os.path.join(script_dir, 'Student Mental health.csv')
df = pd.read_csv(file_path, encoding='latin1')

plt.figure(figsize=(8, 4))
sns.histplot(df['What is your CGPA?'].dropna(), color='purple', discrete=True)
plt.title('Distribution of Students CGPA')
plt.xlabel('CGPA Range')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'exercise4_cgpa.png'), dpi=300)
plt.close()

plt.figure(figsize=(7, 4))
sns.countplot(data=df, x='Choose your gender', hue='Do you have Anxiety?', palette='Set2')
plt.title('Anxiety Levels Across Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'exercise5_anxiety.png'), dpi=300)
plt.close()

df['Panic_Numeric'] = df['Do you have Panic attack?'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x='Age', y='Panic_Numeric', alpha=0.7, color='teal', s=70)
plt.title('Relationship Between Age and Panic Attacks')
plt.xlabel('Age')
plt.ylabel('Panic Attacks (1 = Yes, 0 = No)')
plt.yticks([0, 1], ['No', 'Yes'])
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'exercise6_panic.png'), dpi=300)
plt.close()