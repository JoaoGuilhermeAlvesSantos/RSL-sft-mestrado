import os
import glob
import bibtexparser
import pandas as pd
import matplotlib.pyplot as plt

def load_bib_files(folder="bibs"):
    """Load all .bib files from a folder and return a list of entries."""
    all_entries = []

    bib_files = glob.glob(os.path.join(folder, "*.bib"))
    
    for bib_file in bib_files:
        with open(bib_file, "r", encoding="utf8") as f:
            bib_database = bibtexparser.load(f)
            all_entries.extend(bib_database.entries)

    return all_entries


def extract_years(entries):
    """Extract the 'year' field from BibTeX entries."""
    years = []
    for entry in entries:
        if "year" in entry:
            years.append(entry["year"])
    return years


def plot_year_distribution(years, save_path="output/year_distribution.png"):
    """Create and save a styled bar chart of publication count per year."""
    
    # Count entries by year
    df = pd.DataFrame({"year": years})
    year_counts = df["year"].value_counts().sort_index()

    # Create output folder if needed
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # --- Plot with same design as example ---
    plt.figure(figsize=(6, 4))
    bars = plt.bar(
        year_counts.index.astype(str),
        year_counts.values,
        color="#4C72B0",
        edgecolor="black",
        linewidth=0.8
    )

    plt.xlabel("Year", fontsize=11)
    plt.ylabel("Document Count", fontsize=11)
    plt.title("Documents per Year (from .bib files)", fontsize=13)

    # Dynamic limit with padding
    ymax = max(year_counts.values) + 10
    plt.ylim(0, ymax)

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.xticks(rotation=30, ha="right")

    # Add labels above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + (ymax * 0.02),
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

    print(f"Saved plot to: {save_path}")


def main():
    entries = load_bib_files("bibs")
    years = extract_years(entries)

    if not years:
        print("No year information found in .bib files.")
        return

    plot_year_distribution(years)


if __name__ == "__main__":
    main()
