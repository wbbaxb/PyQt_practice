# 样式管理器 (StyleManager)

`StyleManager` 是一个集中管理应用程序中所有QSS样式的工具类。它提供了一种统一管理所有UI样式的方法，使样式定义更加规范化、可重用和易于维护。样式表定义在单独的QSS文件中，而不是硬编码在Python代码中。

## 主要特点

- 集中管理所有QSS样式
- 从外部QSS文件加载样式
- 支持各种组件的独立样式定义
- 提供通用样式以保持UI一致性
- 使用统一的硬编码字体大小(16px)简化调用

## 重构的好处

重构QSS样式管理带来了以下几个主要好处：

1. **集中式管理**：所有样式定义都位于单独的QSS文件中，方便查找和修改
2. **关注点分离**：样式定义与代码分离，让项目结构更清晰
3. **代码重用**：避免在多个文件中重复相同的样式定义
4. **一致性**：保证所有组件使用一致的风格和颜色方案
5. **可维护性**：修改一处即可影响所有相关组件
6. **模块化**：根据功能或组件类型组织样式代码
7. **可扩展性**：轻松添加新的样式文件而不影响现有代码
8. **易于理解**：QSS文件更易于设计师和开发者理解和修改
9. **简化API**：统一字体大小使API更简洁，更易于使用

## 目录结构

```
Common/
  ├── StyleManager.py       # 样式管理器类
  └── qss/                  # QSS样式文件目录
      ├── common.qss        # 通用样式
      ├── scrollbar.qss     # 滚动条样式
      ├── annotation_tool.qss  # AnnotationTool组件样式
      ├── show_attributes_dialog.qss  # ShowAttributesDialog组件样式
      └── attribute_edit_dialog.qss   # AttributeEditDialog组件样式
```

## 使用方法

### 基本用法

```python
from Common.StyleManager import StyleManager

# 设置窗口样式
self.setStyleSheet(StyleManager.get_common_style())
```

### 获取特定组件样式

```python
# 获取AnnotationTool组件的样式
self.setStyleSheet(StyleManager.get_annotation_tool_style())

# 获取ShowAttributesDialog组件的样式
self.setStyleSheet(StyleManager.get_show_attributes_dialog_style())

# 获取AttributeEditDialog组件的样式
self.setStyleSheet(StyleManager.get_attribute_edit_dialog_style())
```

### 组合多种样式

```python
# 结合多个样式使用combined方法
combined_style = StyleManager.get_combined_style(
    'common', 
    'scrollbar'
)
self.setStyleSheet(combined_style)
```

## 样式函数

StyleManager提供以下样式函数：

- `get_common_style()` - 获取通用样式
- `get_annotation_tool_style()` - 获取AnnotationTool样式
- `get_show_attributes_dialog_style()` - 获取ShowAttributesDialog样式
- `get_attribute_edit_dialog_style()` - 获取AttributeEditDialog样式
- `get_scrollbar_style()` - 获取滚动条样式
- `get_combined_style(*style_names)` - 组合多个样式

## 字体大小配置

所有样式都使用统一的字体大小(16px)，如需修改，可以调整StyleManager类中的FONT_SIZE常量：

```python
class StyleManager:
    # 修改这里可以改变所有样式的字体大小
    FONT_SIZE = 16
    
    # 其他方法...
```

## 样式修改方法

修改样式非常简单，只需编辑对应的QSS文件。例如，要修改所有按钮的颜色：

1. 打开 `Common/qss/common.qss` 文件
2. 找到并修改 QPushButton 样式：

```css
/* 通用按钮样式 */
QPushButton {
    background-color: #3F51B5;  /* 修改这里会影响所有按钮 */
    /* 其他按钮样式保持不变 */
}
```

所有使用 `StyleManager.get_common_style()` 的组件都会立即使用新的样式。

## 添加新样式

要添加新的样式，只需按照以下步骤操作：

1. 在 `Common/qss/` 目录下创建新的 QSS 文件
2. 在 `StyleManager` 类中添加新的方法来加载该文件：

```python
@staticmethod
def get_new_component_style():
    """
    获取新组件的样式表
    """
    qss_dir = StyleManager._get_qss_dir_path()
    base_qss = StyleManager._read_qss_file(os.path.join(qss_dir, 'new_component.qss'))
    
    # 添加字体大小样式
    font_size_qss = f"""
        /* 添加字体大小相关样式 */
        QLabel {{
            font-size: {StyleManager.FONT_SIZE}px;
        }}
    """
    
    return base_qss + font_size_qss
```

3. 在需要使用该样式的组件中调用新方法：

```python
self.setStyleSheet(StyleManager.get_new_component_style())
```

4. 或者将新样式添加到 `get_combined_style` 方法的映射中：

```python
name_to_file = {
    'common': 'common.qss',
    'new_component': 'new_component.qss',  # 添加新样式映射
    # 其他映射...
}
```

## 主题支持

基于外部QSS文件的管理方式非常适合实现主题切换功能。未来可以通过以下方式扩展：

1. 创建主题目录结构：

```
Common/
  └── qss/
      ├── light/   # 浅色主题
      │   ├── common.qss
      │   └── ... 
      └── dark/    # 深色主题
          ├── common.qss
          └── ...
```

2. 在StyleManager中添加主题切换功能：

```python
@staticmethod
def set_theme(theme_name):
    """设置当前使用的主题"""
    StyleManager.current_theme = theme_name

@staticmethod
def get_current_theme():
    """获取当前主题名称"""
    return StyleManager.current_theme

@staticmethod
def _get_theme_qss_dir_path():
    """获取当前主题的QSS目录路径"""
    base_dir = StyleManager._get_qss_dir_path()
    theme_dir = os.path.join(base_dir, StyleManager.current_theme)
    return theme_dir
```

这种方式使主题切换变得简单，同时保持了样式管理的一致性和可维护性。 