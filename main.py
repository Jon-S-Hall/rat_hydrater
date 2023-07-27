import os
import openai

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    the_article = "The Middlebury College sailing team rang in the spring season with sailors traveling all across New England to compete at various regattas. "

    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this article for me in a few sentences: " + the_article,
        max_tokens=100,
        temperature=1
    )

    print(response["choices"][0]["text"])





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
