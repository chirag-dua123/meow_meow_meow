def wordcount(filename):
    counts = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower().strip(".,!?")  # normalize
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    # Sort by frequency
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Print top 10
    for word, freq in sorted_counts[:10]:
        print(word, freq)

def main():
    try:
        wordcount("input.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()