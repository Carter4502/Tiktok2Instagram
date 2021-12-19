# Tiktok2Instagram 📸
## About The Project

<b> What it does: </b>
* Download the source video from a user inputted Tiktok URL. 📙
* Add audio to the Tiktok video from a folder of your audio files. 🎵
* Crop the video to fit the aspect ratio of an instagram post (square by default but you can change this!) 📐
* Output the edited video to a folder of your choice. 📩

<b> Who should use this? </b>
* Of course anyone is free to download and use it, but this program would be particularly useful to anyone who runs a lot of Instagram accounts with content found from tiktok. Instead of manually going to websites to download links and then editing the videos yourself you can simply input the link to the program and it will handle the rest. 😄

### Built With

* [Python 3.9.1](https://www.python.org/)
* [MoviePy](https://zulko.github.io/moviepy/)
* [TiktokAPI](https://github.com/davidteather/TikTok-Api)

<p align="right">

## Getting Started

### Prerequisites

In order to use Tiktok2Instagram you need to download two python libraries: MoviePy and TiktokAPI
  ```sh
  pip install moviepy
  ```
   ```sh
  pip install TikTokApi
  python -m playwright install
  ```
 You also will need to retrieve a verifyFP key to be used by the program. You can find a tutorial on how to get a Tiktok verifyFP key [here](https://medium.com/analytics-vidhya/download-tiktoks-with-python-dcbd79a5237f).
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Carter4502/Tiktok2Instagram.git
   ```
2. Add your verifyFP key to the VERIFY_FP variable.
3. Add the path to your music directory to the PATH_TO_AUDIO
4. Add the path to your output directory to the OUTPUT_FILE_DIR
5. Run:
```sh
  python process_tiktok_video.py
  ```
## Roadmap

- [ ] Add ability to read tiktok links from a file and download all of them.

