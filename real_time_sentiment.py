import time
from collections import deque

# Mock real-time comment stream
def get_new_comments():
    # In a real scenario, this would fetch comments from an API or WebSocket
    mock_data = [
        {'timestamp': time.time(), 'text': 'This coffee is amazing!'}, 
        {'timestamp': time.time() + 1, 'text': 'Too bitter for me.'},
        {'timestamp': time.time() + 2, 'text': 'Love the latte art!'}, 
        {'timestamp': time.time() + 3, 'text': 'Expensive but worth it.'},
        {'timestamp': time.time() + 4, 'text': 'Great for studying.'},
        {'timestamp': time.time() + 5, 'text': 'Not my usual preference.'},
        {'timestamp': time.time() + 6, 'text': 'So smooth and creamy!'}, 
        {'timestamp': time.time() + 7, 'text': 'Wish it was stronger.'},
        {'timestamp': time.time() + 8, 'text': 'Perfect morning brew.'},
        {'timestamp': time.time() + 9, 'text': 'Disappointed with the taste.'}
    ]
    for comment in mock_data:
        yield comment
        time.sleep(0.5) # Simulate delay between comments

# Simple sentiment analysis function (replace with a real NLP model for production)
def analyze_sentiment(text):
    text_lower = text.lower()
    positive_words = ['amazing', 'love', 'great', 'perfect', 'smooth', 'creamy', 'worth']
    negative_words = ['bitter', 'expensive', 'not', 'disappointed', 'wish']

    score = 0
    for word in positive_words:
        if word in text_lower:
            score += 1
    for word in negative_words:
        if word in text_lower:
            score -= 1

    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Main analysis loop
def analyze_stream():
    print("Starting real-time comment analysis...")
    
    # Use a deque to store recent comments for potential time-window analysis
    recent_comments = deque(maxlen=10) 

    for comment in get_new_comments():
        sentiment = analyze_sentiment(comment['text'])
        
        # Log the comment and its sentiment in real-time
        print(f"[{time.strftime('%H:%M:%S')}] Comment: '{comment['text']}' -> Sentiment: {sentiment}")
        
        recent_comments.append({'text': comment['text'], 'sentiment': sentiment})
        
        # In a real application, you might aggregate sentiment over time windows
        # or trigger alerts based on sentiment shifts.

if __name__ == "__main__":
    analyze_stream()
