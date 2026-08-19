#!/bin/bash
# Site-wide Stage 7 check across every page that carries a generated block.
cd ~/BGit/Bryan_git/charlie-kirk || exit 1
FILES=$(grep -rl "CK_4SQ_SITEWIDE_START\|CK_INTERESTING_HERE_START\|CK_INTERESTING_OTHER_START\|CK_4SQ_SECTION_START" \
        site/docs --include='*.md' --include='*.mdx')
[ -z "$FILES" ] && { echo "no generated blocks on site yet"; exit 0; }
echo "pages carrying blocks: $(echo "$FILES" | wc -l | tr -d ' ')"
python3 prompts/four_squares/verify_blocks.py $FILES
