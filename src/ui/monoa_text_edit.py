from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import (QFontMetrics, QColor, QTextFormat)
from PyQt5.QtCore import (Qt, QSize)
#from PyQt5.Qsci import QsciScintilla, QsciLexerPython

# Globals
ROW_HIGHLIGHT_COLOR = QColor(Qt.yellow).lighter(160)

class MonoaTextEdit(QTextEdit):
    def __init__(self, parent = None):
        super(MonoaTextEdit, self).__init__(parent)
        self.textChanged.connect(lambda: self.updateGeometry())
        self.cursorPositionChanged.connect(self.highlight_active_row)

    def highlight_active_row(self):
        selections = []
        sel = QTextEdit.ExtraSelection()
        sel.format.setBackground(ROW_HIGHLIGHT_COLOR)
        sel.format.setProperty(QTextFormat.FullWidthSelection, True)
        sel.cursor = self.textCursor()
        sel.cursor.clearSelection()
        selections.append(sel)
        self.setExtraSelections(selections)

    def setMinimumLines(self, num_lines):
        self.setMinimumSize(self.minimumSize().width(), self.lineCountToWidgetHeight(num_lines))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        margins = self.contentsMargins()
        if width >= margins.left() + margins.right():
            document_width = width - margins.left() - margins.right()
        else:
            document_width = 0
        document = self.document().clone()
        document.setTextWidth(document_width)
        return margins.top() + document.size().height() + margins.bottom()

    def sizeHint(self):
        original_hint = super(MonoaTextEdit, self).sizeHint()
        return QSize(original_hint.width(), self.heightForWidth(original_hint.width()))

    def lineCountToWidgetHeight(self, line_count):
        assert line_count >= 0
        widget_margins = self.contentsMargins()
        document_margin = self.document().documentMargin()
        font_metrics = QFontMetrics(self.document().defaultFont())
        return (
            widget_margins.top() +
            document_margin +
            max(line_count, 1) * (font_metrics.height()+2) +
            self.document().documentMargin() +
            widget_margins.bottom()
        )
