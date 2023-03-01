import opusfilter

import wordnormalizer
import re


class NonPairedBracketsFilter(opusfilter.FilterABC):
    """Filter brackets"""

    def __init__(self, threshold=1, brackets=("()",), skip_numbering=False, **kwargs):
        self.threshold = threshold
        self.brackets = brackets
        self.skip_numbering = skip_numbering
        super().__init__(**kwargs)

    def _brackets(self, sentence):
        count_open = 0
        closed = 0
        unclosed = 0

        for pair in self.brackets:
            if any(br in sentence for br in pair):
                pair_is_equal = pair[0] == pair[1]
                if pair_is_equal:
                    count = sentence.count(pair[0])
                    if count % 2:
                        return (count - count % 2) / count
                    return 1

                for char in sentence:
                    if char == pair[0]:
                        count_open += 1
                    elif char == pair[1]:
                        if count_open >= 1:
                            count_open -= 1
                            closed += 1
                        elif self.skip_numbering and closed + unclosed == 0:
                            if not sentence[: sentence.index(pair[1])].isdigit():
                                unclosed += 1

                        else:
                            unclosed += 1
                unclosed += count_open

        return 1 / (unclosed + 1)

    def score(self, pairs):
        for pair in pairs:
            yield [self._brackets(sentence) for sentence in pair]

    def accept(self, score):
        return all(ratio >= self.threshold for ratio in score)


class LatinCyrillicWordNormalizer(opusfilter.PreprocessorABC):
    """
    Replaces Latin letters in Cyrillic words and vice versa.
    """

    def __init__(self, workdir="", **kwargs):
        super().__init__(workdir, **kwargs)
        self.compiled_reqex = re.compile(
            r"\w*?[\u0400-\u04FF]+[aeopcyxABEHOPCTXKM]+\w*|\w*?[a-zA-Z]+[аеорсухАВЕНОРСТХКМ]+\w*"
        )

    def _normalize(self, segment):
        words = self.compiled_reqex.findall(segment)
        for word in words:
            norm_word = wordnormalizer.correct(word)
            segment.replace(word, norm_word)
            print(word)
        return segment

    def process(self, pairs):
        for segments in pairs:
            yield [self._normalize(segment) for segment in segments]
