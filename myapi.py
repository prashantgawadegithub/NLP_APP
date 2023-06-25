import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('cFq6WhLHBPX2ltxngt8G53vfnAYw1aCjSpbnJ5rDNZs')

    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

    def ner(self,text):
        paralleldots.ner(text)

    def emotion_prediction(self,text):
        paralleldots.emotion(text)


