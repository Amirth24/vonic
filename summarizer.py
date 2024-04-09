import re
import os
import google.generativeai as genai


class Summarizer:
    def __init__(self, temp):
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        generation_config = genai.GenerationConfig(
                temperature=temp
        )

        self.model = genai.GenerativeModel(
            'gemini-1.0-pro-latest',
            generation_config=generation_config)

    def summ(self, transcript):
        prompt = f"""The following text is a auto generated caption\
                of a video. It may have misspelt words. Read them very\
                carefully and summarize it into crisp points

                {transcript}
                """
        res = self.model.generate_content(prompt)
        return re.sub('\\\\n',
                      '\\n',
                      re.findall(
                          r'text[\'"].*\}\], \'role', str(res))[0][8:-10])
