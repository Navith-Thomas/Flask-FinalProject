'''Takes the response from the function
        and outputs a valid output message
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    '''Function to parse and send output
'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid input ! Try again."
    # pylint: disable=consider-using-f-string
    return "For the given statement, the system response is {}."\
    "The dominant emotion is {}.".format(response,dominant_emotion)

@app.route("/")
def render_index_page():
    '''Renders HTML page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
