







def main():
    orig = input('')
    new = input('')
    silly_orig = ''
    silly_new = ''
    quiet = '-'
    for i in range(len(orig)):
        try:
            if not orig[i] == new[i]:
                silly_orig = orig[i]
                silly_new = new[i]
        except:
            quiet = orig[i]
    print(silly_orig,silly_new)
    print(quiet)
if __name__ == '__main__':
    main()