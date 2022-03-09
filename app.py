#!/usr/bin/env python
# coding: utf-8

# In[4]:


from textblob import TextBlob


# In[5]:


from flask import Flask 


# In[6]:


app = Flask(__name__)


# In[7]:


from flask import render_template, request


# In[8]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result = r))
    else: 
        return(render_template("index.html", result = "2"))


# In[9]:


if __name__ == "__main__":
    app.run()

