import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = 'results-acm-count.csv'
data = pd.read_csv(file_path)

# Ensure the CSV has the expected columns
if 'dataset' not in data.columns or 'count' not in data.columns:
    raise ValueError("The CSV file must contain 'dataset' and 'count' columns.")

# Optional: sort by count descending
data = data.sort_values('count', ascending=False)

# Plot the data
plt.figure(figsize=(6, 4))
bars = plt.bar(
    data['dataset'],
    data['count'],
    color='#4C72B0',
    edgecolor='black',
    linewidth=0.8
)

plt.xlabel('Dataset', fontsize=11)
plt.ylabel('Literature Count', fontsize=11)
plt.title('Dataset X Literature Count (Before Deduplication)', fontsize=13)

plt.ylim(0, 100)  # <<----- Aqui está o limite solicitado

plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(rotation=30, ha='right')

# Add labels above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 3,                  # offset pequeno fixo para não estourar o limite
        f"{int(height)}",
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.savefig('datasetXcount_before_deduplication.png', dpi=300)
plt.show()
