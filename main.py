import openai


def askGPT(text):
    openai.organization = "<ORGANIZATION-ID>"
    openai.api_key = "<Your-API-KEY>"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=150,
    )
    return print(response.choices[0].text)


def main():
    while True:
        myQn = input('GPT: Ask me a question\n')
        askGPT(myQn)


if __name__ == '__main__':
    main()
