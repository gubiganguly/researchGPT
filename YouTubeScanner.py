from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeScanner:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.latest_video_id = None


    # Fetch the transcript of the video
    def fetch_transcript(self, video_id):
        # Fetch the transcript of the video
        try:
            # Attempt to fetch the transcript of the video
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

            # Concatenate all text elements from the transcript
            transcript_text = ' '.join([segment['text'] for segment in transcript_list])

            return transcript_text
        except Exception as e:
            print(f"Couldn't fetch transcript: {e}")
            return "No transcript available"

    # Fetch latest video id
    def fetch_latest_video(self):
        # Request to get the latest video from the channel
        request = self.youtube.search().list(
            part="snippet",
            channelId=self.channel_id,
            order="date",  # ensures the latest videos come first
            maxResults=1  # we only want the latest video
        )
        response = request.execute()

        # Extract video ID from the response
        if response['items']:
            # Define latest_video_id here from the response
            latest_video_id = response['items'][0]['id']['videoId']
            if self.latest_video_id != latest_video_id:
                self.latest_video_id = latest_video_id

                # Fetch additional details
                transcript = self.fetch_transcript(latest_video_id)

                # Constructing the JSON data
                video_data = {
                    "channel_id": self.channel_id,
                    "channel_title": response['items'][0]['snippet']['channelTitle'] if response['items'] else 'No title found',
                    "video_title": response['items'][0]['snippet']['title'] if response['items'] else 'No title found',
                    "video_id": latest_video_id,
                    "transcript": transcript
                }

                return video_data
            else:
                print("No new videos since the last check.")
        else:
            print("No videos found for the channel.")
        return None

