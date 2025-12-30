import argparse
import sys

def wordcount(filename):
    """Return a dict of word -> frequency for the given file.

    This function is pure (no printing) so it can be unit-tested easily.
    """
    counts = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;"\'()[]{}')
                if not word:
                    continue
                counts[word] = counts.get(word, 0) + 1

    return counts


def main(argv=None):
    try:
        if argv is None:
            argv = sys.argv[1:]
        parser = argparse.ArgumentParser()
        parser.add_argument("filename")
        args = parser.parse_args(argv)
        counts = wordcount(args.filename)

        # Sort by frequency and print top 10
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for word, freq in sorted_counts[:10]:
            print(word, freq)

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())