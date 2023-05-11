import googleapiclient.discovery
import matplotlib.pyplot as plt
import openai

def get_video_comments(video_id, api_key):
    # Build a YouTube client using the provided API key
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    # Make a request to retrieve comment threads for the specified video
    request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100, textFormat="plainText")
    response = request.execute()
    # Extract the comments from the response and return them
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response['items']]
    return comments

def filter_relevant_comments(comments):
    # Define a list of keywords to filter relevant comments
    keywords = ['dead by daylight', 'dbd', 'gameplay', 'balance', 'killer', 'survivor', 'perk', 'bug', 'issue', 'buff', 'nerf']
    relevant_comments = []
    # Iterate over each comment and check if any of the keywords are present
    for comment in comments:
        if any(keyword.lower() in comment.lower() for keyword in keywords):
            # If a relevant keyword is found, add the comment to the relevant_comments list
            relevant_comments.append(comment)
    return relevant_comments

def analyze_sentiments(comments):
    sentiment_scores = ""
    comments_to_analyze = ""
    message_history = []
    for comment in comments:
        # Concatenate the comments to analyze within a certain length limit
        comments_to_analyze += str(comment)
        if len(comments_to_analyze) > 3000:
            message_history = []
            # Prepare a message history for the AI model, including system instructions and user messages
            message_history.append({"role": "system", "content": 'analyze the text and provide a list of common complaints, along with their frequency'})
            message_history.append({"role": "user", "content": comments_to_analyze})
            # Request a list of common complaints, along with their frequency from the OpenAI ChatCompletion model
            response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=message_history
                )
            print("\n",(comments_to_analyze),'\n','Ai response',response.choices[0].message.content)
            summary = response.choices[0].message.content
            sentiment_scores += summary  # (non solution) todo: Intelligently combine the final summary
            comments_to_analyze = ""
    return sentiment_scores

'''
from old version could be updated if summary was updated

def plot_sentiment_histogram(sentiment_scores):
    # Plot a histogram of sentiment scores
    plt.hist(sentiment_scores, bins=20, color='blue', edgecolor='black')
    plt.xlabel('Sentiment Scores')
    plt.ylabel('Frequency')
    plt.title('Sentiment Analysis of YouTube Comments on Dead by Daylight')
    plt.show()
'''

# Prompt the user for input
video_id = input("Enter video ID: ")
api_key = input("Enter your YouTube API key: ")
openai.api_key = input("Enter your OpenAI API key: ")

# Retrieve the comments for the specified video
comments = get_video_comments(video_id, api_key)
# Filter relevant comments based on predefined keywords
relevant_comments = filter_relevant_comments(comments)
# Perform sentiment analysis on the relevant comments
sentiment_scores = analyze_sentiments(relevant_comments)

# Print the final sentiment summary
print('\n','final summary',sentiment_scores)
# Plot the sentiment histogram
# plot_sentiment_histogram(sentiment_scores)