import matplotlib.pyplot as plt
import seaborn as sns


def plot_chord_distribution(df, top_n=15):
    plt.figure(figsize=(12, 6))
    top_chords = df['clean_chord'].value_counts().head(top_n)
    sns.barplot(x=top_chords.index, y=top_chords.values, hue=top_chords.index, palette='viridis')
    plt.title(f'Top {top_n} Most Frequent Chords in The Beatles Songs')
    plt.xlabel('Chord')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()