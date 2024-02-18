from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models.openai import ChatOpenAI
from flask import Flask, request, jsonify
import random
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'], )
def process():
    data = request.get_json()#start of webscraper
    print(data)
    lan = data['name']
    error1 = data['email']#gets error form frontend
    error3=error1.replace(' ','+')#changes space to + for it to work for links
    error=error3
    response=[]
    for i in range(2):#rotates between sites
        start='http://'
        site=['www.google.com/','www.meta.stackoverflow.com/','www.quora.com/']
        end=error
        link=start+str(site[i])+'search?q='+str(error)#genrates url based on problem

        # response.append(link)
        url_list = [link]

        prompt = '''
            Go to one forum
            that best matchs the prompt in the Google search bar and that shows up in the Google page results
            and give a summary for it. Emphasize the answer for the forum and show the forum's link. Only use 76 words.
        '''

        def web_scrape(url_list, query):
            openai = ChatOpenAI(
                model_name='gpt-4',
                max_tokens=2048
            )
            loader_list = []
            for i in url_list:
                print("loading url: %s" % i)
                loader_list.append(WebBaseLoader(i))
    
            index = VectorstoreIndexCreator().from_loaders(loader_list)
            ans = index.query(query)

            return ans

        scrape = web_scrape(url_list, prompt)
        response.append(scrape)

    # response.headers.add('Access-Control-Allow-Origin', '*')
    print(jsonify(response[0]))
    return jsonify(response[0]) #gives link
    

if __name__ == '__main__':
    app.run(debug=True)