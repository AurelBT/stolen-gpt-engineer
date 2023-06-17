from StolenGPT import StolenGPT

class AI:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.kwargs['model'] = "gpt-3.5-turbo"
        self.stl = StolenGPT()
        self.lastm = []

    def start(self, system, user):
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

        return self.next(messages)

    def fsystem(self, msg):
        return {"role": "system", "content": msg}

    def fuser(self, msg):
        return {"role": "user", "content": msg}

    def next(self, messages: list[dict[str, str]], prompt=None):
        if prompt:
            messages = messages + [{"role": "user", "content": prompt}]

        msg2send = [i for i in messages if not i in self.lastm]
        ai_response = ""
        for i in msg2send:
            ai_response = self.stl.chat(i["content"])

        print(ai_response.replace("\\n", "\n").replace('\\"', '"').replace("\\'", "'").replace("\\t", "\t"))
        self.lastm = messages + [{"role": "assistant", "content": ai_response}]
        return self.lastm
