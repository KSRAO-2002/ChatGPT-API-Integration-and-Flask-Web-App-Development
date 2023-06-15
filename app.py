import openai
from flask import Flask, render_template, request

# Set up OpenAI API credentials
openai.api_key = "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"

openai.Model.list()
# Initialize Flask app
app = Flask(__name__, static_url_path='/static')


# Define routes and controllers 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    # Get user input from form submission
    health_condition = request.form.get('health-condition')
    severity = request.form.get('severity')

    # Define the initial system message and user messages
    messages = [
        {"role": "system", "content": "You are now connected to the Health Conditions Helpdesk."},
        {"role": "user", "content": "I need help with a health condition."},
        {"role": "assistant", "content": "Sure, I'll be happy to assist you. Please enter the health condition you are suffering."},
        {"role": "user", "content": health_condition},
        {"role": "assistant", "content": "Thank you for providing the health condition. Now, please enter the severity of the condition."},
        {"role": "user", "content": severity}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message = response.choices[0].message.content

    except Exception as e:
        # Handle API errors or failed requests
        message = f"Error: {str(e)}"
    print(message)
    return render_template("results.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)