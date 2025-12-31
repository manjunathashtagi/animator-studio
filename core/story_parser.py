def split_story_into_segments(story: str):
    """
    Splits long story into semantic segments.
    Returns list of text blocks.
    """
    lines = [l.strip() for l in story.split("\n") if l.strip()]
    segments = []
    current = []

    for line in lines:
        current.append(line)
        if line.endswith(".") or line.endswith("!"):
            segments.append(" ".join(current))
            current = []

    if current:
        segments.append(" ".join(current))

    return segments
