#!/usr/bin/env python3
import os
import openai
import click
from pathlib import Path

@click.command()
@click.option('-m', '--model', default='text-davinci-003', help='The model to use for generating the response.')
@click.argument('prompt')
@click.option('-t','--text', type=str, default=None)
def main(prompt, model,text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if text:
        text = Path(text).read_text()

        prompt = prompt + text

    response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=1.0,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    print(response.choices[0].text.strip())

if __name__ == '__main__':
    main()
