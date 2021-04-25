#organizes photos with a date_place structure
#creates directories based on place
#moves photos to directory based on place in filename

import os

def extract_place(filename):
  return filename.split("_")[1]


def make_place_directories(places):
   for place in places:
        os.mkdir(place)
  
        
def organize_photos(directory):
  os.chdir(directory)
  originals = os.listdir()
  places = []
  for file in originals:
      place = extract_place(file)
      if place not in places:
        places.append(place)
  make_place_directories(places)
  for file in orginals:
    place = extract_place(file)
    os.rename(file, 
              os.path.join(place, file))
    
