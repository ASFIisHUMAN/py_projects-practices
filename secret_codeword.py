import random

a = "the quick=b40wn,fox!j6mps@2v1r/789-lazy:d3g._?"

def reverse(char):
    variables = {
        a[0]: ['b4001', 'b44', 'b79'],
        a[1]: ['b31', 'b21', 'b68'],
        a[2]: ['b002', 'b94', 'b008'],
        a[3]: ['b09318', 'b348', 'b9821'],
        a[4]: ['b092', 'b787', 'b119'],
        a[5]: ['b883', 'b104', 'b311'],
        a[6]: ['b305', 'b206', 'b101'],
        a[7]: ['b193', 'b213', 'b29'],
        a[8]: ['b3', 'b201', 'b98'],
        a[9]: ['b14', 'b564', 'b863'],
        a[10]: ['b81', 'b27', 'b083'],
        a[11]: ['b404', 'b90', 'b37'],
        a[12]: ['b303', 'b834', 'b207'],
        a[13]: ['b869', 'b062', 'b004'],
        a[14]: ['b313', 'b241', 'b704'],
        a[15]: ['b23', 'b009', 'b603'],
        a[16]: ['b77', 'b09', 'b5'],
        a[17]: ['b102', 'b69', 'b191'],
        a[18]: ['b601', 'b007', 'b68'],
        a[19]: ['b76', 'b32', 'b6'],
        a[20]: ['b093', 'b46', 'b39'],
        a[21]: ['b473', 'b97', 'b702'],
        a[22]: ['b659', 'b28', 'b35'],
        a[23]: ['b1245', 'b985', 'b'],
        a[24]: ['b326', 'b3298', 'b159'],
        a[25]: ['b324', 'b753', 'b654'],
        a[26]: ['b796', 'b0066', 'b08'],
        a[27]: ['b1111', 'b3596', 'b900'],
        a[28]: ['b6543', 'b33', 'b9763'],
        a[29]: ['b982', 'b000', 'b96'],
        a[30]: ['b877', 'b91', 'b453'],
        a[31]: ['b407', 'b9022', 'b5441'],
        a[32]: ['b617', 'b6788', 'b9728'],
        a[33]: ['b2008', 'b735', 'b16'],
        a[34]: ['b1991', 'b8', 'b03'],
        a[35]: ['b1985', 'b9780', 'b805'],
        a[36]: ['b570', 'b8624', 'b1971'],
        a[37]: ['b11', 'b4700', 'b533'],
        a[38]: ['b7009', 'b5682', 'b1469'],
        a[39]: ['b0085', 'b1966', 'b6487'],
        a[40]: ['b1973', 'b9814', 'b100'],
        a[41]: ['b1975', 'b1496', 'b3008'],
        a[42]: ['b66', 'b0564', 'b6969'],
        a[43]: ['b0703', 'b9005', 'b83'],
        a[44]: ['b30035', 'b5954', 'b315'],
        a[45]: ['b99301', 'b3057', 'b00509']     
    }

    # Convert the text to lowercase
    char = char.lower()

    # Check if the character exists in the mappings
    if char in variables:
        return random.choice(variables[char])
    else:
        return "No variable associated with this character"

def reverse_sentence(sentence):
    reversed_sentence = ""
    for char in sentence:
        reversed_sentence += str(reverse(char)) + "+"
    return reversed_sentence.strip()

# Test the function
input_sentence = input("Enter text : ")
print(reverse_sentence(input_sentence)[:-1])
