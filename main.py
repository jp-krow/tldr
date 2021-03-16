from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from flask import Flask, request, jsonify

errorMsg = """
      <p>Couldn't complete request.</p>\n
      \n
      <p>- Check if summerization URL is correct / valid</p>\n
      \n
      <p>- Try lowering your sentences parameter (e.g change from 15 sentences to 5)</p>\n
      \n
      <p>- Check if language is properly spelled and valid\n
      (Reminder: language is NOT your language per say, but the language the selected site uses.)</p>\n
      \n
      <p>- Check if website is protected from GET requests from bots\n
      (Cloudflare, Amazon CloudFront, etc.) If this is true, add "cached" to True in your request (uses google cached save).</p>\n
      \n
      <p>- Or your request may be rate limited.</p>
      """

app = Flask(__name__)
@app.route("/sum", methods=["POST"])
def summerize():
  if request.method == "POST":
    
    try:
      LANGUAGE = request.form.get('site-language')

      #sentences parameter optional, defaults to 10
      if request.form.get("sentences",None) == None:
        SENTENCES_COUNT = 10
      else:
        SENTENCES_COUNT = int(request.form.get('sentences'))

      #optional google cashed parameter, helps avoid anti-bot pages
      if request.form.get("cached", None).lower() == "true":
        url = "http://webcache.googleusercontent.com/search?q=cache:" + request.form.get('url')
      elif request.form.get("cached", None) == None or request.form.get("cached", None).lower() == "false":
        url = request.form.get('url')

      #try:
      parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
      #except:
        #return errorMsg, 400
      # or for plain text files
      # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
      stemmer = Stemmer(LANGUAGE)

      summarizer = Summarizer(stemmer)
      summarizer.stop_words = get_stop_words(LANGUAGE)
      sums = ""
      fax = False
      c = 0

      for sentence in summarizer(parser.document, SENTENCES_COUNT):
            c += 1
            sums += str(sentence)
            sums += "\n"
            if c == SENTENCES_COUNT:
              fax = True

      while True:
        if fax == True:
          return jsonify(str(sums)), 200
    except:
      return errorMsg, 400
@app.route("/")
def index():
  return "Use a POST on /sum to summerize text."


if __name__ == "__main__":
  import os
  os.system("""python -c "import nltk; nltk.download('punkt')"
  """)
  app.run(
  threaded = True,
  host="0.0.0.0"
  )
