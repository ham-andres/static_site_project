

def markdown_to_blocks(markdown):
    result = []
    markdown_text = markdown.split("\n\n")
    for block in markdown_text:
        stripped = block.strip()
        if stripped != "":
           result.append(stripped)
    return result