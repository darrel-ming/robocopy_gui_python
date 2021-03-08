from PySide2.QtCore import (Qt, QRect)
from PySide2.QtWidgets import (
    QStyledItemDelegate, QStyleOptionViewItem, QStyle)
from PySide2.QtGui import (QColor)


class LabelItemDelegate(QStyledItemDelegate):
    '''
    Label delegate to show text as much as it allows
    Attributes:
    -----------
    m_TextAlign : alignment
        text alignment
    '''

    def __init__(self, model, parent=None, align=Qt.AlignVCenter):
        super(LabelItemDelegate, self).__init__(parent)
        self.m_TextAlign = align

    def editorEvent(self, event, model, option, index):
        '''
        '''
        return False

    def paint(self, painter, option, index):
        '''
        '''
        painter.save()
        options = QStyleOptionViewItem(option)
        options.text = index.data()
        rt = QRect(options.rect)
        flag = False

        if option.state & QStyle.State_Selected:
            flag = True
        # sets back/fore color for selected/non-selected
        back_color = Qt.white if not flag else QColor('#0087D0')
        fore_color = Qt.black if not flag else Qt.white
        painter.fillRect(rt, back_color)
        painter.setPen(QColor(fore_color))
        rt.adjust(10, 0, 0, 10)
        painter.drawText(rt, self.m_TextAlign, options.text)
        painter.restore()
