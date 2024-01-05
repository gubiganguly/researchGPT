import time
import os
from YouTubeScanner import YouTubeScanner  # Make sure this is the name of your file containing the class
from GPTSummarizer import GPTSummarizer
from dotenv import load_dotenv
load_dotenv()

def main():
    Matt_Wolfe = YouTubeScanner(os.getenv("YOUTUBE_API_KEY") , 'mrewolf')

    while True:
        new_video_info = Matt_Wolfe.fetch_latest_video()
        #print(new_video_info)
        if new_video_info:
            summarizer = GPTSummarizer(os.getenv("OPENAI_API_KEY"), new_video_info['transcript'])
            summary = summarizer.summarize("Summarize the following youtube transcript into short easy to understand bullet points. The bullet points will be used to write a news letter so keep that in mind, no extra fluff. Here is the transcript:")
            print(new_video_info['channel_title'], " - ", new_video_info['video_title'], "\n", summary)
        else:
            print("Could not find youtuber id")
        time.sleep(3600)  # Wait for 1 hour before checking again. Adjust as needed.

if __name__ == "__main__":
    main()