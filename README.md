Why:
- Didn't like any TTS voices shipped on Windows, macOS, Linux, and online.
- Did like the Google Cloud Wavenet voices provided by
  [Google Cloud Text-To-Speech](https://cloud.google.com/text-to-speech/).
- Wanted to provide a generally platform-agnostic way of obtaining reasonable
  voice announcements.

Setup and Use:
- Use [Google Cloud Console](https://console.cloud.google.com/apis/credential)
  to generate an API key. Place said key into `gsay.py`.
- `python3 gsay.py "Test Voice Announcement" > test.mp3`
- `ffmpeg -y -i test.mp3 -ar 8000 test.wav` - taking care to make sure the file
  comes to 3 seconds or less (or wait until conversion to be told about it.)
- Repeat ad nauseam until satisfied.
- `APX CPS > Tools > VA Converter Utility` to perform `.wav -> .mva` in bulk.
- Add to `Radio Ergonomics Configuration > Voice Announcements >
  Voice Announcement List` and assign away to Zone/Channels!

Quirks about TTS:
- All TTS software and voices butcher things.
- Here are some examples in the case of Google Cloud Wavenet:
  - "BAPERN" -> "B A P E R N." Try "Baypern" instead.
  - "MEMA" -> "M E M A.". Try "Meema" instead.
  - "EMS System" -> "Em's System." Try "E-MS System" instead.
  - "BAA" -> "B A A." Try "B-A-A" instead. ("B-AA" gave me "B double A.")

Quirks about Motorola APX CPS:
- Each VA has a 3 second limit.
- 32 character file name limit (minus the `.mva` file type suffix).
- Codeplugs have a 1000s maximum limit - so at 3 seconds each, that's 333 files.
- This is of course a worst case scenario, but is a reasonable indicator.
- Assuming all that goes to sets of 17 (zone + 16 channels), that's 19.5 zones.
- Does not include things for buttons and actions.
- Therefore, assume that VA is to be used where you expect most channel use.

Thoughts about Voice Announcements:
- VAs are highly useful - forgotten about unless they disappear.
- Unfortunately VAs are difficult to set up, perhaps comically so.
- Cursory field testing indicates many users/testers preferred feminine voices.
- Would be interesting to see if this determination can be reproduced in an
  academic study, and investigate why this is the case.
- Out of the 3 feminine Wavenet voices, users tended towards C and E as opposed
  to F, the highest pitched voice. C appeared to be more popular.

TODO:
- Improve `gsay.py` configuration.
- Tooling to process bulk VAs from a list in a file.
- Automated checking of audio file length.
