# python-sample-apps-with-AIaaS-apis

## Table of Contents

+ [Summary](#summary)
+ [Reference](#reference)
+ [Features](#features)
+ [Getting started](#getting-started)

## Summary

Sample apps utilizing AI as a Service (primarily OpenAI and Gemini) Web APIs.

## Reference

- [Get started with the Gemini API](https://ai.google.dev/docs)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [OpenAI Models](https://platform.openai.com/docs/models/overview)

### Features

- [ ] Chat bot sample app utilizing gpt-3.5-turbo model
- [ ] Image generator sample app utilizing e.g. DALL-E
- [ ] Speech generator sample app

### Getting started

#### Preconditions

- If your IDE supports it, install `Dev Containers extension`
- Create from the [secrets.template.cfg](./templates/secrets.template.cfg) in the [templates folder](./templates/) a `secrets.cfg` file.
In a Unix-like terminal run the command `source secrets.cfg`.
- Create an `API key` in your OpenAI organization

#### Starting applications

##### Chat bot

```sh
cd samples/chat-bot
pip install -r requirements.txt
python chatbot.py --system <System content here> --user <User content here>
```

##### Image generator

```sh
cd samples/image-generator
pip install -r requirements.txt
TBD
```

##### Speech generator

```sh
cd samples/speech-generator
pip install -r requirements.txt
TBD
```