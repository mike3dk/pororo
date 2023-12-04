import sys
import json
from pororo.pororo import Pororo

def main(text):
    ner = Pororo(task="ner", lang="ko")
    out = json.dumps(ner(text), ensure_ascii=False)
    print(out)


if __name__ == "__main__":
    print(sys.argv)
    text = sys.argv[1]
    main(text)
