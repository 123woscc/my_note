# PyQt5图片设置

```python
from PyQt5.QtGui import QPixmap
import requests

pic = requests.get(url).content
pixmap=QPixmap()
pixmap.loadFromData(pic)
label.setPixmap(pixmap)
```

