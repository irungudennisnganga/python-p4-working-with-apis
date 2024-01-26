
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://fakestoreapi.com/products"

    response = requests.get(URL)
    return response.content

# programs = GetPrograms().get_programs()
# print(programs)

  def program_school(self):
      # we use the JSON library to parse the API response into nicely formatted JSON
      programs_list = []
      programs = json.loads(self.get_programs())
      for program in programs:
          programs_list.append(program['title'])

          return programs_list
        
        
programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)        