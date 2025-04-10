# 样式管理

该项目使用简单直接的样式管理方法，将所有QSS样式定义集中在一个文件中。

## 主要特点

- **单一样式文件**：所有样式定义集中在一个QSS文件中
- **简单加载方式**：通过简单的工具函数一次性加载所有样式
- **清晰的样式组织**：使用注释分隔不同组件的样式定义
- **统一的字体大小**：所有字体大小统一为16px

## 目录结构

```
Common/
  ├── style_util.py       # 样式加载工具
  └── qss/
      └── style.qss       # 统一的样式文件
```

## 使用方法

```python
from Common.style_util import load_style

# 设置窗口样式
self.setStyleSheet(load_style())
```

所有组件都使用相同的样式加载方式，确保样式一致性，并且极大简化了样式管理。

## 样式修改方法

修改样式非常简单，只需编辑 `Common/qss/style.qss` 文件。文件内已经按组件类型划分了不同的样式区域：

```css
/* ================ 通用样式 ================ */
/* 这里是通用样式定义 */

/* ================ 滚动条样式 ================ */
/* 这里是滚动条样式定义 */

/* ================ AnnotationTool样式 ================ */
/* 这里是AnnotationTool组件样式定义 */

/* ================ ShowAttributesDialog样式 ================ */
/* 这里是ShowAttributesDialog组件样式定义 */

/* ================ AttributeEditDialog样式 ================ */
/* 这里是AttributeEditDialog组件样式定义 */
```

修改后所有组件将自动应用新样式，无需更改代码。

## 优点

1. **极简管理**：只需要维护一个样式文件
2. **直观明了**：所有样式在同一个地方，容易查找和修改
3. **维护方便**：修改样式不需要修改任何Python代码
4. **性能优化**：文件只需加载一次，减少文件I/O操作
5. **代码精简**：不需要复杂的样式管理类，简化代码结构

## 主题支持（未来扩展）

如果将来需要支持主题切换，可以通过简单扩展当前的方法实现：

1. 为每个主题创建单独的样式文件（如 `light_style.qss` 和 `dark_style.qss`）
2. 扩展 `style_util.py` 来支持主题选择：

```python
def load_style(theme='light'):
    """
    加载指定主题的样式表
    
    参数:
        theme: 主题名称，默认为'light'
    
    返回:
        str: 样式表内容
    """
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 样式文件路径
    style_file = os.path.join(current_dir, 'qss', f'{theme}_style.qss')
    
    try:
        with open(style_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"读取样式文件出错: {str(e)}")
        return ""
```

这种方式保持了设计的简洁性，同时保留了灵活扩展的可能性。 