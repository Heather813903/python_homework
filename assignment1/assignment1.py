#task 1
def say_hello():
    return "Hello!"

print(say_hello())

#task 2
def greet(name="John"):
    return "Hello, " + name + "!"

print (greet())

#task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
             case "add": 
                return a + b    
             case "subtract":
                return a - b    
             case "multiply":
                return a * b 
             case "divide":
                return a / b    
             case "modulo":
                return a % b
             case "int_divide":
                return a // b   
             case "power":
                return a ** b   
             case _:
                return "Invalid!"
    except ZeroDivisionError:
       return "You can't divide by 0!"
    except TypeError:
       return "You can't multiply those values!"
    
print(calc(7, 8, "add"))
print(calc(7, 0, "divide"))

    
    
#task 4
def data_type_conversion(value, data_type):
      try:
          if data_type == "float":
            return float (value)
          elif data_type == "str":
            return str (value)
          elif data_type == "int":
             return int (value)
          else:
             return f"Invalid data type requested: {data_type}"
      except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion("banana", "int"))

#task 5
def grade(*args):
   try:
      average = sum(args) / len(args)
      if average >=90:
         return "A"
      elif average >=80:
         return "B"
      elif average >=70:
         return "C"
      elif average >=60:
         return "D"
      else:
         return "F"
   except:
      return "Invalid data was provided."
      
      
        
                
#task 6
def repeat(string, count):
   result = ""
   for _ in range(count):
      result += string
   return result
print (repeat("up," , 4))

#task 7
def student_scores(pos, **kwargs):
   if pos == "best":
      #highest score
      best_student = max(kwargs, key=kwargs.get)
      return best_student
   elif pos == "mean":
      #average score
      average_score = sum(kwargs.values()) / len(kwargs)
      return average_score
   else:
      return "Invalid pos! Use 'best' or 'mean'"
print(student_scores("best", Tom=75, Dick=89, Angela=91))
print(student_scores("mean", Tom=75, Dick=89, Angela=91))

#talk 8

def titleize(book):
   #list of little words
   little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

   words = book.split()
   for i, word in enumerate(words):
      #capitalize first and last words
      if i == 0 or i == len(words) - 1:
         words[i] = word.capitalize()
      #capitalize other words
      elif word.lower() not in little_words:
         words[1] = word.capitalize()
      else:
         words[i] = word.lower()
   return " ".join(words)

print(titleize("one flew over the cuckoo's nest"))
print(titleize("the count of monte cristo"))

#task9
def hangman(secret, guess):
   result = ""
   for char in secret:
      #check if char is in guess string
      if char in guess:
         #if yes, add char
         result += char
      else:
         result += "_"
   return result

print(hangman("difficulty", "ic"))

#task 10
def pig_latin(phrase):
   def convert_word(word):
   #if the str starts with a vowel
      vowels = ("aeiou")
      if word[0] == vowels:
         return ("word" + "ay")
   #if the str starts with a consonant
      elif word[:2] == "qu":
         return word[2:] + "quay"
      else:
         for i in range(len(word)):
            if word[i] in vowels:
               return word[i] + word[i] + "ay"
            return word + "ay"
   words = phrase.split()
   converted_words = [convert_word(word) for word in words]
   return " ".join(converted_words)
   
english_sentence = "apple"
print(pig_latin(english_sentence))

   



   
          


         

         






   
     


                   
                
      


    


    

    
    
      
        









          



