
# Markdown Image Expander 

![](https://img.shields.io/badge/Python-3.7-blue?style=flat)
![](https://img.shields.io/badge/License-MIT-green?style=flat)

このパッケージははマークダウンのライブラリである [markdown](https://python-markdown.github.io/) に拡張機能を提供します。

この拡張機能は画像表示を含むマークダウンを HTML に変換する際に `<img>` タグを `<p>` タグで囲まれないようにします。
それによって意図しない `<p>` タグの出現を抑えることができます。
ただし、段落内の文章中に埋め込まれた画像は、そのまま段落内に配置されます。

## Usage

```python
import markdown
from markdown_image_expander import MarkdownImageExpander

md = markdown.Markdown(extensions=[MarkdownImageExpander()])
```

```markdown
![](single-picture.jpg)

![](multiple-picture1.jpg)
![](multiple-picture2.jpg)
![](multiple-picture3.jpg)

some text
![](inline-picture.jpg)
some text
```

```html
<img src="single-picture.jpg">

<img src="multiple-picture1.jpg">
<img src="multiple-picture2.jpg">
<img src="multiple-picture3.jpg">

<p>
  some text<img src="inline-picture.jpg">some text
</p>
```

## Installation

```shell
python setup.py install
```

```shell
python setup.py test
```

```shell
python -m pip uninstall markdown_image_expander
```

## License

&copy; tikubonn 2020<br>
Markdown Image Expander released under [MIT License](LICENSE).<br>
[markdown](https://python-markdown.github.io/) released under [BSD License](LICENSE).
