import time
from YouTubeScanner import YouTubeScanner  # Make sure this is the name of your file containing the class
from GPTSummarizer import GPTSummarizer

# Replace with your actual YouTube API Key and desired Channel ID
YouTube_API_KEY = 'AIzaSyAH73d14VW5PisEXd0j_sOblNvuscrUC2Q'
Matt_Wolfe_CHANNEL_ID = 'UChpleBmo18P08aKCIgti38g'
OpenAI_API_KEY = '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'

def main():
    Matt_Wolfe = YouTubeScanner(YouTube_API_KEY , Matt_Wolfe_CHANNEL_ID)

    while True:
        new_video_info = Matt_Wolfe.fetch_latest_video()
        if new_video_info:
            # print(new_video_info)
            summarizer = GPTSummarizer(OpenAI_API_KEY, new_video_info['transcript'])
            summary = summarizer.summarize("Summarize the following youtube transcript into short easy to understand bullet points. The bullet points will be used to write a news letter so keep that in mind, no extra fluff. Here is the transcript:")
            print(new_video_info['channel_title'], " - ", new_video_info['video_title'], "\n", summary)

        time.sleep(3600)  # Wait for 1 hour before checking again. Adjust as needed.

if __name__ == "__main__":
    main()