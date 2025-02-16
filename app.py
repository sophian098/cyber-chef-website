from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)


def caesar(word):
  result=''
  for character in word:
    if character.isupper():
      unicode=(ord(character)+3-65)%26+65
      result+=(chr(unicode))
    elif character.islower():
      unicode=(ord(character)+3-97)%26+97
      result+=(chr(unicode))
    else:
      result+=(character)
  return result

def reverse(word):
  i=0
  result=''
  for character in word:
    result+=word[len(word)-i-1]
    i+=1
  return result

def atbash(word):
  result=''
  for character in word:
    if character.isupper():
      unicode=26-(ord(character)-65+1)+65
      result+=(chr(unicode))
    elif character.islower():
      unicode=26-(ord(character)-97+1)+97
      result+=(chr(unicode))
    else:
      result+=(character)
  return result
  
@app.route('/cooking', methods=['POST', 'GET'])
def cooking():
    if request.method == 'POST':
        word=request.form.get('ingredient-input')
        choice=request.form["button"]

        if choice=='caesar':
            result=caesar(word)
        elif choice=='reverse':
            result=reverse(word)
        elif choice=='atbash':
            result=atbash(word)
        else:
            result="error"
        
        print(choice)
        print(word)
        return render_template('cooking.html', result=result)  
    else:
        return render_template('cooking.html')

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/signup')
def signup():
  return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    fname=request.form.get('fname')
    lname=request.form.get('lname')
    password=request.form.get('password')
    
    if len(password)<6:
        message="Your password is too short! Make sure it is 6 characters or more"
        return render_template('form.html', message=message)
  
    if not any(character.isupper() for character in password):
        message="Your password does not have a capital letter! Make sure it contains a capital letter."
        return render_template('form.html', message=message)
  
    if not any(character.islower() for character in password):
        message="Your password does not have a lower-case letter! Make sure it contains a lower-caseletter."
        return render_template('form.html', message=message)
    else:
      return redirect(url_for('submit', fname=fname, lname=lname))

@app.route('/submit')
def submit():
    fname=request.args.get('fname')
    lname=request.args.get('lname')
    return render_template('submit.html', fname=fname, lname=lname)
  
@app.route('/hacks')
def hacks():
    return render_template('personality.html')

if __name__ == '__main__':
  app.run(debug=True)
