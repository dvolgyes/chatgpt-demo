#!/usr/bin/env python3
import os
import openai
import click

@click.command()
@click.option('-m', '--model', default='text-davinci-003', help='The model to use for generating the response.')
@click.argument('prompt')
def main(prompt, model):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print(response.choices[0].text.strip())

if __name__ == '__main__':
    main()
