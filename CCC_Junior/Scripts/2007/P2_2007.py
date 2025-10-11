

def rules(phrase):
    child = ['CU',':-)',':-(',';-)',':-P','(˜.˜)','TA','CCC','CUZ','TY','YW','TTYL']
    i = child.index(phrase)
    adult = ['see you','I’m happy','I’m unhappy','wink','stick out my tongue','sleepy','totally awesome','Canadian Computing Competition','because','thank-you','you’re welcome','talk to you later']
    return adult[i]



def main():
    phrase = input('Enter phrase>')
    f = rules(phrase)
    print(f)

if __name__ == '__main__':
    main()