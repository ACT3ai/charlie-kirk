p_create_nano_banaa.md

Create the Nano Banana image prompt for the post in this directory. Running this
prompt file WRITES the prompt text into nano_banana.txt. It does NOT generate the
image. Generating the image is a separate command a human runs, printed at the
end of this prompt.


===========================
VARIABLES
===========================

ROOT_DIR dir is ~/BGit/Bryan_git/charlie-kirk

POST_DIR dir is {ROOT_DIR}/site/docs/Tyler_Robinson/discord/post
  The directory this prompt file sits in. The prompt text and the finished
  image both land here.

NB_TOOL is file ~/BGit/all/tools/nano_banana_4k/nb_4k.js
  The Nano Banana 4K generator. Run `node {NB_TOOL} --help` for the full flag
  list. Never guess a model id; `node {NB_TOOL} --list-models` is free.

NB_PROMPT_FILE is file {POST_DIR}/nano_banana.txt
  The output of this prompt file. Holds the image prompt and nothing else.

IMAGE_FILE is file {POST_DIR}/nano_banana.jpg
  Where the generated image is saved. Same directory as this prompt.

POST_FILE is file {POST_DIR}/good_tweet.txt
  The post this image is paired with. If it does not exist, use
  {POST_DIR}/bad_tweet.txt instead.

POST_PROMPT_FILE is file {POST_DIR}/p_create_post.md
  The companion prompt that writes the post itself.

MODEL   is the value nano-banana-pro     (Google gemini-3-pro-image)
SIZE    is the value 4K
ASPECT  is the value 16:9


===========================
WHAT I NEED  (Bryan fills this in)
===========================

* What the image must show:

* Mood and tone:

* Any exact words that must appear in the image:

* Reference images to feed in (full paths):

* Anything to leave OUT:


Rules for this section:
* Whatever is written here wins over every default below.
* If this section is empty, derive the image concept from {POST_FILE}.
* If both are empty, stop and say there is nothing to make an image from.


===========================
STAGE 1: READ THE INPUTS
===========================

* Read the WHAT I NEED section above.
* Read {POST_FILE}. The image serves that post: it is the thing a scroller sees
  before they read one word.
* Read any screenshots, notes, or reference files already in {POST_DIR}.
* Read {POST_PROMPT_FILE} for the mission behind the post.
* Do not invent facts. The image never asserts a claim the post does not make.


===========================
STAGE 2: DECIDE ONE IMAGE
===========================

* One image, not a set. Pick the single strongest visual idea in the post.
* It must read at thumbnail size on a phone, in one second, with sound off.
* Composition is 16:9 landscape. Keep the subject and any text inside a safe
  margin of about 6 percent on every edge, because X crops the preview.
* Prefer one clear subject and a lot of negative space over a busy collage.


===========================
STAGE 3: WRITE THE PROMPT
===========================

Write one continuous prompt of roughly 120 to 250 words in plain prose. Nano
Banana Pro reads a described photograph better than a list of keywords. Cover,
in this order:

* Shot and framing: wide, medium, close, over the shoulder, overhead. Say the
  aspect ratio is 16:9 landscape and describe where the subject sits in frame.
* Subject: what it is, what it is doing, what it is made of.
* Environment: where it is, what surrounds it, what is on the floor and walls.
* Lens and camera: focal length, depth of field, angle, height.
* Lighting: key, fill, practicals, time of day, hard or soft, direction.
* Color palette: name three or four colors and say which dominates.
* Mood: one or two words carried by the light and the color, not stated as a
  caption.
* Style: photographic realism, editorial photo, documentary still, graphic
  poster, 3D render. Name one and commit to it.
* Text in the image, only if the mission asks for it: give the exact words in
  double quotes, 6 words or fewer, and say where they sit and how large. Nano
  Banana Pro renders typography well but only when the words are short and
  spelled out exactly.
* Negative constraints last, as plain sentences: what must not appear.

Hard rules for the prompt content:
* No recognizable likeness of any real living person. No real faces. If a
  person is needed, describe them silhouetted, back turned, out of focus, or
  cropped below the eyes.
* No real logos, no real trademarks, no real ID cards, no real signatures.
* Nothing that asserts guilt about a living person. No handcuffs on a
  recognizable individual, no crime-scene staging implying a named person did
  something. The image sets a mood; the post carries the claims.
* No gore, no weapon pointed at a person, no depiction of the killing.
* No watermark, no caption bar, no fake news-network chyron, no fake seal of
  any real agency.
* No emojis, no hashtags, no markdown in the prompt file.


===========================
STAGE 4: WRITE THE FILE
===========================

* Write the prompt to {NB_PROMPT_FILE}, replacing whatever is there.
* The file holds ONLY the prompt text. No title, no headers, no bullet list, no
  commentary, no explanation of choices, no trailing notes. The tool sends the
  whole file to the model.
* Plain UTF-8. No smart quotes, no invisible Unicode.


===========================
STAGE 5: DO NOT GENERATE
===========================

This prompt file NEVER runs the generator. Generating costs money. Print the
exact command and stop.

Output to stdout:

  ==============================================================
  Wrote the image prompt: {NB_PROMPT_FILE}

  To generate the image, run:

  node ~/BGit/all/tools/nano_banana_4k/nb_4k.js \
    "{NB_PROMPT_FILE}" \
    "{IMAGE_FILE}" \
    --model nano-banana-pro --size 4K --aspect 16:9

  Add --dry-run first to see exactly what would be sent and spend nothing.
  Add --skip-existing to refuse to overwrite an image that already exists.
  Add --in <path> once per reference image, up to 14.
  ==============================================================

Notes on the tool, for whoever runs it:
* Defaults are already model nano-banana-pro, size 4K, aspect 16:9, JPEG
  quality 95. The flags above are written out so the command is explicit.
* At 16:9 the real output pixels are about 5504 x 3072 for 4K and 2752 x 1536
  for 2K. That is correct, not a bug.
* A 4K call takes roughly 30 seconds. A cold model can take minutes.
* The API key lives at ~/.config/GoogleCloud/apikey.yaml. Never print it.
