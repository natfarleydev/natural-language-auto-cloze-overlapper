import re
from typing import  Set

phrase_separators = ".;,\n"
split_by_phrase_separators_pattern = re.compile(f"(?<=[{phrase_separators}])?[^{phrase_separators}]+?(?=[{phrase_separators}$])")


def get_phrases(text) -> Set[str]:
    return {x.strip() for x in split_by_phrase_separators_pattern.findall(text)}


def get_card_contents(text: str, overlap=0) -> Set[str]:
    phrases = get_phrases(text)

    if overlap == 0:
        return {text.replace(p, "{{c1:" + p + "}}") for p in phrases}
    else:
        retset = set()
        for i in range(overlap, len(phrases) - (overlap - 1)):
            p = phrases[i-1:i+1]
            retset.add(re.sub(f"({p[0]}.\\s+{p[1]})", r'{{c1::\1}}', text))
            
        return retset
