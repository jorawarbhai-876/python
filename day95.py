#regular expression
import re
pattern = r"[A-Z]+yclone"
text = '''The Importance of Being Earnest is a drawing-room comedy by Oscar Wilde. Premiered on 14 February 1895 Cyclone and Dyclone in London, it depicts the affairs of two young men about town who lead double lives to evade unwanted social obligations, both assuming the name Ernest to woo two young women. Other characters are the formidable Lady Bracknell, the fussy governess Miss Prism and the benign and scholarly Canon Chasuble. The play, celebrated for its wit and repartee, parodies contemporary dramatic norms and comically satirises late-Victorian manners. The triumphant opening night was followed within weeks by Wilde's downfall and imprisonment for homosexual acts and the closure of the production, and Wilde wrote no more comic or dramatic works. From the early 20th century onwards, the play has been revived frequently and adapted for radio, television, film, operas and musicals.'''
# match = re.search(pattern, text)
# if match:
#     print("match found")
# else:
#     print("match not found")
# meta characters use to make pattern
match = re.finditer(pattern,text)
for match in match:
  print(match.span())
  print(match[match.span()[0],match.span()[1]])