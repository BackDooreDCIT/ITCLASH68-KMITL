# def find_valid_words(dictionary, available_chars):
#     available_chars = list(available_chars)  # แปลงเป็น list เพื่อให้ลบตัวอักษรได้
#     valid_words = []

#     for word in dictionary:
#         temp_chars = available_chars.copy()  # สร้างสำเนาเพื่อใช้งานแยกกัน
#         if len(word) >= 3 and all(word.count(c) <= temp_chars.count(c) for c in word):
#             valid_words.append(word)

#     if not valid_words:
#         return 0, "NO VALID WORDS"

#     valid_words.sort(key=lambda x: (-len(x), x))  # เรียงตามความยาวก่อน และตามลำดับพจนานุกรม
#     return len(valid_words), valid_words[0]

# # รับ input
# n = int(input())  # จำนวนคำในพจนานุกรม
# dictionary = [input().strip() for _ in range(n)]
# available_chars = input().strip()

# # ประมวลผลและแสดงผลลัพธ์
# count, longest_word = find_valid_words(dictionary, available_chars)
# print(count)
# print(longest_word)


def main():
    n = int(input())  
    dictionary = [input().strip() for _ in range(n)]
    available_chars = input().strip()

    available_chars = list(available_chars)  
    valid_words = []

    
    for word in dictionary:
        temp_chars = available_chars.copy()  
        if len(word) >= 3 and all(word.count(c) <= temp_chars.count(c) for c in word):
            valid_words.append(word)

    
    if not valid_words:
        print(0)
        print("NO VALID WORDS")
    else:
        valid_words.sort(key=lambda x: (-len(x), x))  
        print(len(valid_words))
        print(valid_words[0])


main()
