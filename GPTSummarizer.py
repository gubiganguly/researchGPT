from openai import OpenAI

class GPTSummarizer:
    def __init__(self, api_key, transcript):
        self.transcript = transcript
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)  # Instantiate the client with the API key

    def summarize(self, prompt):
        # Constructing the full prompt with the transcript
        full_prompt = f"{prompt}\n\nTranscript: {self.transcript}\n\nSummary:"

        # Making a call to the OpenAI API using the new interface
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",  # Specify the model you want to use
                messages=[
                    {"role": "system", "content": "You are an assistant used to summarize youtube transcripts for a news letter."},
                    {"role": "user", "content": full_prompt}
                ]
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"An error occurred: {e}")
            return "Failed to generate summary"

