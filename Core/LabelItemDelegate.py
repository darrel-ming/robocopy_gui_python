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
        When editing of an item starts, this function is called with
        the event that triggered the editing, the model,
        the index of the item, and the option used for rendering the item.
        '''
        return False

    def paint(self, painter, option, index):
        '''
        This pure abstract function must be reimplemented if you
        want to provide custom rendering. Use the painter and style
        option to render the item specified by the item index
        '''
        painter.save()
        options = QStyleOptionViewItem(option)
        # get the cell text
        options.text = index.data()
        # get the cell rectangle
        rt = QRect(options.rect)
        # determines the cell is selected or not
        flag = False
        if option.state & QStyle.State_Selected:
            flag = True
        # sets back/fore color for selected/non-selected
        back_color = Qt.white if not flag else QColor('#0087D0')
        fore_color = Qt.black if not flag else Qt.white
        # paint the backgrouund
        painter.fillRect(rt, back_color)
        # select the pen for draw text
        painter.setPen(QColor(fore_color))
        # make the margin
        rt.adjust(10, 0, 0, 10)
        # draw the text
        painter.drawText(rt, self.m_TextAlign, options.text)
        painter.restore()
