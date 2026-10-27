import torch
from collections import defaultdict

def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    merges = []
    
    # Track the split tokens for each word
    splits = {word: word.split() for word in corpus.keys()}
    
    for _ in range(num_merges):
        # Step 1: Count all adjacent pairs weighted by word frequency
        pairs = defaultdict(int)
        for word, freq in corpus.items():
            symbols = splits[word]
            for i in range(len(symbols) - 1):
                pair = (symbols[i], symbols[i+1])
                pairs[pair] += freq
                
        if not pairs:
            break
            
        # Step 2: Find the most frequent pair
        best_pair = max(pairs, key=pairs.get)
        merges.append(best_pair)
        
        # Step 3: Merge that pair everywhere it appears
        bigram = " ".join(best_pair)
        replacement = "".join(best_pair)
        
        new_corpus = {}
        new_splits = {}
        for word, freq in corpus.items():
            # Replace the space-separated pair in the string representation
            new_word = word.replace(bigram, replacement)
            new_corpus[new_word] = freq
            new_splits[new_word] = new_word.split()
            
        corpus = new_corpus
        splits = new_splits
    
    return merges