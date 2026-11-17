"""Write boards/language/topics.json and boards/literature/topics.json (site topics -> spec ids / question types)."""
import json, pathlib
LANG = [  # slug, name, group, statement ids
 ('representation', 'Meanings and representations in texts', 'Textual variations and representations', ['4.1.1-03', '4.1.1-06', '4.2.1-10']),
 ('audience-purpose-context', 'Audience, purpose, genre and context', 'Textual variations and representations', ['4.1.1-01', '4.1.1-02']),
 ('identity-relationships', 'Identity and relationships in language', 'Textual variations and representations', ['4.1.1-04', '4.1.1-05', '4.2.1-09']),
 ('child-language-speech', "Child language acquisition: speech", "Children's language development", ['4.1.3-01', '4.1.3-02']),
 ('child-language-literacy', 'Child language: literacy and writing', "Children's language development", ['4.1.3-03', '4.1.3-04']),
 ('child-language-theories', 'Child language acquisition theories', "Children's language development", ['4.1.3-05']),
 ('occupational-language', 'Occupational and social group language', 'Language diversity and change', ['4.2.1-01']),
 ('language-and-gender', 'Language and gender', 'Language diversity and change', ['4.2.1-02']),
 ('ethnicity-world-englishes', 'Ethnicity and world Englishes', 'Language diversity and change', ['4.2.1-03', '4.2.1-05']),
 ('accent-and-dialect', 'Accent and dialect', 'Language diversity and change', ['4.2.1-04']),
 ('language-change', 'Language change', 'Language diversity and change', ['4.2.1-06']),
 ('attitudes-to-language', 'Language variation and attitudes to it', 'Language diversity and change', ['4.2.1-07', '4.2.1-08']),
 ('language-discourses', 'Language discourses', 'Language discourses and writing', ['4.2.3-01', '4.2.3-02', '4.2.3-03', '4.2.3-04']),
 ('directed-writing', 'Directed writing: opinion articles', 'Language discourses and writing', ['4.2.4-01', '4.2.4-02', '4.2.4-03']),
]
LIT = [
 ('othello', 'Othello', 'Shakespeare', ['4.1.1-OTH']), ('taming-of-the-shrew', 'The Taming of the Shrew', 'Shakespeare', ['4.1.1-TAM']),
 ('measure-for-measure', 'Measure for Measure', 'Shakespeare', ['4.1.1-MFM']), ('the-winters-tale', "The Winter's Tale", 'Shakespeare', ['4.1.1-WT']),
 ('love-poetry-pre-1900', 'AQA Anthology: love poetry pre-1900', 'Love poetry and prose', ['4.1.2-PRE']),
 ('love-poetry-post-1900', 'AQA Anthology: love poetry post-1900', 'Love poetry and prose', ['4.1.2-POST']),
 ('comparing-prose-love', 'Comparing prose texts (love through the ages)', 'Love poetry and prose', ['4.1.3-PROSE', '4.1.3-PERS', '4.1.3-JE', '4.1.3-WH', '4.1.3-AWAK', '4.1.3-ROTT', '4.1.3-MILL', '4.1.3-TESS', '4.1.3-GATS', '4.1.3-RWV', '4.1.3-GOB', '4.1.3-REB', '4.1.3-ATON']),
 ('unseen-love-poetry', 'Unseen poetry comparison (love)', 'Love poetry and prose', [], {'fmt': ['Unseen poetry comparison']}),
 ('unseen-love-prose', 'Unseen prose (AS)', 'Love poetry and prose', [], {'fmt': ['Unseen prose']}),
 ('regeneration', 'Regeneration (Pat Barker)', 'WW1 and its aftermath', ['4.2.1-REGEN']), ('birdsong', 'Birdsong (Sebastian Faulks)', 'WW1 and its aftermath', ['4.2.1-BIRD']),
 ('oh-what-a-lovely-war', 'Oh! What a Lovely War', 'WW1 and its aftermath', ['4.2.1-OWLW']), ('journeys-end', "Journey's End (R.C. Sherriff)", 'WW1 and its aftermath', ['4.2.1-JEND']),
 ('up-the-line-to-death', 'Up the Line to Death (WW1 poetry)', 'WW1 and its aftermath', ['4.2.1-UPLD']), ('scars-upon-my-heart', 'Scars Upon My Heart (WW1 poetry)', 'WW1 and its aftermath', ['4.2.1-SCARS']),
 ('ww1-unseen-extract', 'WW1 unseen extract', 'WW1 and its aftermath', [], {'fmt': ['Contextual linking'], 'paper': '2A'}),
 ('ww1-comparison', 'WW1 comparing texts', 'WW1 and its aftermath', [], {'fmt': ['Contextual comparison'], 'paper': '2A'}),
 ('the-handmaids-tale', "The Handmaid's Tale (Margaret Atwood)", 'Modern times', ['4.2.2-HMT']), ('waterland', 'Waterland (Graham Swift)', 'Modern times', ['4.2.2-WATL']),
 ('top-girls', 'Top Girls (Caryl Churchill)', 'Modern times', ['4.2.2-TOPG']), ('a-streetcar-named-desire', 'A Streetcar Named Desire', 'Modern times', ['4.2.2-STREET']),
 ('feminine-gospels', 'Feminine Gospels (Carol Ann Duffy)', 'Modern times', ['4.2.2-FEMG']), ('skirrid-hill', 'Skirrid Hill (Owen Sheers)', 'Modern times', ['4.2.2-SKIR']),
 ('modern-times-unseen-extract', 'Modern times unseen extract', 'Modern times', [], {'fmt': ['Contextual linking'], 'paper': '2B'}),
 ('modern-times-comparison', 'Modern times comparing texts', 'Modern times', [], {'fmt': ['Contextual comparison'], 'paper': '2B'}),
]
for name, rows in (('language', LANG), ('literature', LIT)):
    out = []
    for r in rows:
        d = dict(slug=r[0], name=r[1], group=r[2], statements=r[3])
        if len(r) > 4: d['match'] = r[4]
        out.append(d)
    json.dump(out, open(f'boards/{name}/topics.json', 'w'), indent=1, ensure_ascii=False)
    print(name, len(out))
