#test version 

#This is the Qt Version of MicroHope IDE
#Here we are using PyQt4 library
#Author : Arun Jayan
#Email ID : arunjayan32@gmail.com

__author__ = 'Arun Jayan'
__email__ = "arunjayan32@gmail.com"


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MyHighlighter( QSyntaxHighlighter ):

    def __init__( self, parent, theme ):
      QSyntaxHighlighter.__init__( self, parent )
      self.parent = parent
      keyword = QTextCharFormat()
      ATMEGA32_REG = QTextCharFormat()
      PREPROCESS_DIR = QTextCharFormat()
      headerfile = QTextCharFormat()
      assignmentOperator = QTextCharFormat()
      delimiter = QTextCharFormat()
      specialConstant = QTextCharFormat()
      boolean = QTextCharFormat()
      number = QTextCharFormat()
      comment = QTextCharFormat()
      string = QTextCharFormat()
      singleQuotedString = QTextCharFormat()

      self.highlightingRules = []
      # keyword
      brush = QBrush( Qt.darkBlue, Qt.SolidPattern )
      keyword.setForeground( brush )
      keyword.setFontWeight( QFont.Bold )
      keywords = QStringList( [ "int","float","double","char"
								,"unsigned","long","uint8_t",
								"uint16_t","uint32_t","uint64_t","if","else","for","switch","while","do",
								"return","void"] )
	
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, keyword )
        self.highlightingRules.append( rule )
