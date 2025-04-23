import re
from collections import Counter

class LanguageIdentifier:
    def __init__(self, n=3, top_k=400, penalty=400):
        """
        Initializes the identifier with:
         - n: the size of the character n-grams (default 3)
         - top_k: only the top_k most frequent n-grams are kept in each profile
         - penalty: a fixed penalty added when an n-gram is missing in a language profile
        """
        self.n = n
        self.top_k = top_k
        self.penalty = penalty
        self.language_profiles = {}  # language -> n-gram ranking dictionary

    def _preprocess(self, text):
        """
        Preprocesses the text by converting to lowercase and normalizing spaces.
        """
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)
        return text

    def get_profile(self, text):
        """
        Creates an n-gram profile for a given text. The profile is a dictionary where
        each key is an n-gram and the value is its rank (0 being most frequent).
        """
        text = self._preprocess(text)
        ngrams = [text[i:i+self.n] for i in range(len(text) - self.n + 1)]
        counter = Counter(ngrams)
        # Extract the top_k n-grams by frequency and assign a rank based on their order.
        most_common = counter.most_common(self.top_k)
        profile = {ngram: rank for rank, (ngram, count) in enumerate(most_common)}
        return profile

    def add_language(self, language, text):
        """
        Adds a language and its training text to the language profiles.
        """
        profile = self.get_profile(text)
        self.language_profiles[language] = profile

    def compute_distance(self, profile1, profile2):
        """
        Computes the "out-of-place" distance between two n-gram profiles.
        For each n-gram in profile1, if it exists in profile2, the absolute difference in
        their ranks is added; otherwise, a fixed penalty is added.
        """
        distance = 0
        for ngram, rank in profile1.items():
            if ngram in profile2:
                distance += abs(rank - profile2[ngram])
            else:
                distance += self.penalty
        return distance

    def identify_language(self, text):
        """
        Identifies the language of the input text by comparing its n-gram profile to the
        stored language profiles. Returns the language with the smallest distance.
        """
        profile = self.get_profile(text)
        distances = {}
        for language, lang_profile in self.language_profiles.items():
            distances[language] = self.compute_distance(profile, lang_profile)
        best_language = min(distances, key=distances.get)
        return best_language, distances