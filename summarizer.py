from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_text(text, num_sentences):

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    total_sentences = len(
        parser.document.sentences
    )

    if num_sentences > total_sentences:
        num_sentences = total_sentences

    summarizer = LsaSummarizer()

    summary = summarizer(
        parser.document,
        num_sentences
    )

    return " ".join(
        str(sentence)
        for sentence in summary
    )