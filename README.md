# fitvoxglobal-post
## Carousels (from 29 Nov 2026)
Every post is a carousel of 3 to 5 slides, 1080x1350 each. Slide files are named `YYYY-MM-DD-N-topic-sK.jpg` (N = post number of the day, K = slide number) with one caption `YYYY-MM-DD-N-topic.txt`.
`tools/carousel/chars.py` holds the illustrated character cast (`emirati`, `consultant`, `suit`) and `gen_carousel_example.py` shows how the first carousel was built.

## Photos (from 28 Nov 2026)
People in the slides are real-looking AI photos made by the owner in ChatGPT and kept in `photos/`: `cast-team-cover.jpg` (three people, cover), `cast-desk-pair.jpg` (two people at a desk, call to action), `cast-woman-portrait.jpg` and `cast-man-portrait.jpg` (square portraits for round badges). A slide uses a photo through `<img src="/_blob/ID" data-local="photos/<file>.jpg">`; the render script reads the file from this folder. `tools/carousel/gen_photo_carousel_example.py` shows how the first photo carousel was built. Captions of posts that use these photos end with "Images generated with AI."
