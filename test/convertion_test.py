
import textwrap
from bs4 import BeautifulSoup as Bs
from unittest import TestCase 
from markdown import Markdown
from markdown_image_expander import MarkdownImageExpander

class ConvertionTest (TestCase):

  def test1 (self):
    md = Markdown(extensions=[MarkdownImageExpander()])
    source = """
    ![](example.png)
    """
    mustbe = """
    <img alt="" src="example.png">
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )

  def test2 (self):
    md = Markdown(extensions=[MarkdownImageExpander()])
    source = """
    example text
    ![](example.png)
    example text
    """
    mustbe = """
    <p>
    example text
    <img alt="" src="example.png">
    example text
    </p>
    """
    self.assertEqual(
      Bs(md.convert(textwrap.dedent(source)), "html.parser").prettify().replace("\n", ""),
      Bs(textwrap.dedent(mustbe), "html.parser").prettify().replace("\n", "")
    )
