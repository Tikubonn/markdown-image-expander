
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree import ElementTree as etree

class MarkdownImageExpander (Extension):

 def extendMarkdown (self, md):
   md.treeprocessors["image_expander"] = ImageExpander()

class ImageExpander (Treeprocessor):

  """
  this treeprocessor expand image elements in <p> tag that contain image element only.
  """

  def search_parent (self, element, root):

    """
    find parent node of element.
    this function return position of element in parent node, and parent node.
    """

    dictionary = dict()
    for p in root.iter():
      for index, ele in enumerate(p.findall("./*")):
        dictionary[ele] = index, p 
    return dictionary[element]

  def should_expand (self, element):

    """
    if <p> contain image element only, return true, otherwise false.
    """

    texts = list(element.itertext())
    eles = element.findall("./*")
    if not texts and eles:
      for ele in eles:
        if ele.tag == "a":
          texts = list(ele.itertext())
          es = ele.findall("./*")
          if not texts and es:
            for e in es:
              if e.tag not in ("img", "figure"):
                return False 
            else:
              return True 
          else:
            return False 
        elif ele.tag not in ("img", "figure"):
          return False
      else:
        return True 
    else:
      return False 

  def expand (self, element, root):

    """
    expand elements in <p> to parent node.
    """

    index, parent = self.search_parent(element, root)
    parent.remove(element)
    for ele in reversed(element.findall("./*")):
      parent.insert(index, ele)

  def run (self, root):
    for element in root.iterfind("p"):
      if self.should_expand(element):
        self.expand(element, root)
