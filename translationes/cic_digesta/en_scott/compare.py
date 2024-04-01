import re

with open("../../../fontes/cic_digesta/digesta_stage_3_minified.txt", encoding="utf-8", newline="") as source:
    lines = source.read().split("\n")

la_signatures = []

for line in lines:
    # Book
    match = re.match(r"^(\d+) (.+)$", line)

    if match is not None:
        la_signatures.append(match.group(1))
        continue

    # Title
    match = re.match(r"^(\d+,\d+) (.+)$", line)

    if match is not None:
        la_signatures.append(match.group(1))
        continue

    # Inscription
    match = re.match(r"^(\d+,\d+,\d+a?) ([^ ]+) (.*)$", line)

    if match is not None:
        la_signatures.append(match.group(1))
        continue

    # Paragraph
    match = re.match(r"^(\d+,\d+,\d+a?,\d+[a-e]?) (.+)$", line)

    if match is not None:
        la_signatures.append(match.group(1))
        continue

    print(f"Could not read LA line:\n{line}")

en_signatures = []

with open("digesta_scott.txt", encoding="utf-8", newline="") as source:
    lines = source.read().split("\n")

for line in lines:
    # Book
    match = re.match(r"^(\d+) (.+)$", line)

    if match is not None:
        if match.group(1) in en_signatures:
            print(f"EN: {match.group(1)} already present!")

        en_signatures.append(match.group(1))
        continue

    # Title
    match = re.match(r"^(\d+,\d+) (.+)$", line)

    if match is not None:
        if match.group(1) in en_signatures:
            print(f"EN: {match.group(1)} already present!")

        en_signatures.append(match.group(1))
        continue

    # Inscription
    match = re.match(r"^(\d+,\d+,\d+a?) (.*)$", line)

    if match is not None:
        if match.group(1) in en_signatures:
            print(f"EN: {match.group(1)} already present!")

        en_signatures.append(match.group(1))
        continue

    # Paragraph
    match = re.match(r"^(\d+,\d+,\d+a?,\d+[a-e]?) (.+)$", line)

    if match is not None:
        if match.group(1) in en_signatures:
            print(f"EN: {match.group(1)} already present!")

        en_signatures.append(match.group(1))
        continue

    print(f"Could not read EN line:\n{line}")

print(f"LA: {len(la_signatures)}")
print(f"EN: {len(en_signatures)}")

diff = set(la_signatures).symmetric_difference(en_signatures)
diff = sorted(diff)

ignore = ["5,1,49,1",
          "9,2,17,1",
          "19,5,27", "19,5,27,0",
          "22,3,30", "22,3,30,0", "22,3,31", "22,3,31,0",
          "26,4,11", "26,4,11,0",
          "28,8,7,1", "28,8,7,2", "28,8,7,3",
          "30,0,41,16",
          "34,5,3a", "34,5,3a,0",
          "36,1,45", "36,1,45,0",
          "36,1,84", "36,1,84,0", "36,1,85", "36,1,85,0",
          "36,4,16", "36,4,16,0", "36,4,17", "36,4,17,0",
          "38,2,8,5",
          "40,13,5", "40,13,5,0",
          "41,3,4,24a",
          "44,2,8", "44,2,8,0",
          "46,8,26", "46,8,26,0",
          "47,2,37a", "47,2,37a,0",
          "48,8,15,1",
          "48,13,13,1",
          "49,14,17", "49,14,17,0",
          "49,15,22,2a"]

for signature in ignore:
    diff.remove(signature)

print(f"{len(diff)} differences, {len(ignore)} more ignored")
print(diff)
