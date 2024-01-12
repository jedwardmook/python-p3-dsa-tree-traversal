class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    elements_to_visit = [self.root]

    while elements_to_visit:
      current = elements_to_visit.pop()
      if current['id'] == id:
        return current
      elements_to_visit = elements_to_visit + current['children']
    return None



      
      

    

    
