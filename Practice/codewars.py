def is_anagram(test, original):
    if len(test) == len(original):
        test.split()
        original.split()
        print(test)
        print(original)
        for i in test.lower():
            if i in original.lower():
                print("True")
            else:
                print("False")
                break
    else:
        print("False")

is_anagram("foefet", "toffee")

is_anagram( 'oIAjtdXilIre', 'XoeOAiZctrno')
