#function to generate videogame titles

import random
import videogame_info

def videogame_generator(genre, topic, title, templates):
  
  template = random.choice(templates)
  
  output = []
  
  index = 0
  
  while index < len(template):
    
    if template[index: index + 5] == "GENRE":
      output.append(random.choice(genre))
      index += 5
      
    elif template[index: index + 5] == "TOPIC":
      output.append(random.choice(topic))
      index += 5
      
    elif template[index: index + 5] == "TITLE":
      output.append(random.choice(title))
      index += 5
      
    else:
      output.append(template[index])
      index += 1
      
 return "".join(output)

videogame_generator(videogame_info.genre, videogame_info.topic, videogame_info.title, videogame_info.templates)

if __name__ == "__main__":
  print(videogame_generator(videogame_info.genre, videogame_info.topic, videogame_info.title, videogame_info.templates))
