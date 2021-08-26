def TestCase():
    #1 The method can take up to two numbers, separated by commas, and will return their sum.
    #for an empty string it will return 0
    assert(Add("") == 0),"Empty String doesn't return 0"

    assert(Add("1") == 1),"Given String 1 doesn't return 1"
    assert(Add("2,3") == 5),"Given String 2,3 doesn't return 5"

    #2 Allow the Add method to handle an unknown amount of numbers
    assert(Add("1,2,3") == 6),"Given String 1,2,3 doesn't return 6"
    assert(Add("1,4,5,6") == 16),"Given String 1,4,5,6 doesn't return 16"

    #3 Allow the Add method to handle new lines between numbers (instead of commas).
    assert(Add("1\n2") == 3),"Given String \"1\n2\" doesn't return 3"
    assert(Add("3\n4") == 7),"Given String \"3\n4\" doesn't return 7"

    #4 Support different delimiters
    assert(Add("//;\n1;2;3") == 6),"Given String \"//;\n1;2;3\" doesn't return 6"
    assert(Add("//-\n1-2-3") == 6),"Given String \"//-\n1-2-3\" doesn't return 6"

    #5 Calling Add with a negative number
    assert(Add("//;\n-1;-2;-3;2") == 2),"Given String \"//;\n-1;-2;-3;2\" doesn't return 2"

    #6 Numbers bigger than 1000 should be ignored, so Adding 2 + 1001 = 2
    assert(Add("//;\n1000;2") == 2),"Given String \"//;\n1000;2\" doesn't return 2"

    #7 Delimiters can be of any length with the following format
    assert(Add("//-----\n1-----2-----3") == 6),"Given String \"//----\n1----2----3\" doesn't return 6"

    #8 Allow multiple delimiters
    assert(Add("//-!;-\n1-!;-2-!;-3") == 6),"Given String \"//-!;-\n1-!;-2-!;-3\" doesn't return 6"

    #9 make sure you can also handle multiple delimiters with length longer than one char
    assert(Add("//-!;v-\n1-!;v-2-!;v-3") == 6),"Given String \"//-!;v-\n1-!;v-2-!;v-3\" doesn't return 6"
    assert(Add("//-!;v-\n15-!;v-12-!;v-3") == 30),"Given String \"//-!;v-\n15-!;v-12-!;v-3\" doesn't return 30"

    print("All Test Case Passed Successfully")

def Add(NumString):
    if len(NumString) == 0:
        return 0
    elif len(NumString) == 1:
        return int(NumString)
    elif NumString[0]=="/":
        delim=""
        lines=NumString.split("\n")
        for char in range(2,len(lines[0])):
            delim=delim+lines[0][char]
        numbers = lines[1].split(delim)
        return MultiNumbers(numbers)
    else:
        delim = ","
        NumString = NumString.replace('\n', ',')
        numbers = NumString.split(delim)
        return MultiNumbers(numbers)
def MultiNumbers(numbers):
    result = 0
    status=0
    s=""
    for num in numbers:
        try:
            assert int(num) > 0 
        except AssertionError :
            status=1
            if s == "":
                s = num
            else:
                s = s+','+ num
        if int(num) > 0 and int(num) < 1000:
            result += int(num)
    if status==1:
        print("negatives not allowed",s)
    return result
if __name__ == "__main__":
    TestCase()
