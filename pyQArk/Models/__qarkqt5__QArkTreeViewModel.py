# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTreeViewModel
#
# @see http://qt-project.org/doc/qt-4.8/itemviews-editabletreemodel.html
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
from __future__ import (absolute_import, division, print_function, unicode_literals)
import sys
try:
    from future import standard_library
    standard_library.install_aliases()

    from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                          int, map, next, oct, open, pow, range, round,
                          str, super, zip)
except ImportError:
    if sys.version_info.major == 2:
        print('Warning : future package is missing - compatibility issues between python 2 and 3 may occur')
try:
    # Python 2 : basestring exists (for isinstance test)
    basestring
except:
    # Python 3 : basestring does not exist
    basestring = str
#}-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt5 import QtCore


from pyQArk.Models.QArkTreeItem import QArkTreeItem
from pyQArk.Core.QArkMimeData import QArkMimeData
import copy

class QArkTreeItemMimeData(QArkMimeData):
    MIME_TYPE = 'application/qarktreeitem-instance'

class QArkTreeViewModel( QtCore.QAbstractItemModel ):

    itemAddedSignal = QtCore.pyqtSignal(object)
    itemRemovedSignal = QtCore.pyqtSignal(object)

    # Signal emitted to ask for an expand
    # The parameter is the QModelIndex to expand
    expandRequestSignal = QtCore.pyqtSignal( object )


    def __init__( self
                 , parent
                 , _t_data = None
                 , _t_header = None
                 ):
        """
        It is up to the constructor to create a root item for the model.
        This item only contains vertical header data for convenience.
        We also use it to reference the internal data structure that
        contains the model data, and it is used to represent an
        imaginary parent of top-level items in the model.
        """
        super( QArkTreeViewModel, self ).__init__( parent )

        self.o_rootItem = QArkTreeItem( None, _t_header )

        if not _t_data is None:
            self.setupModelData( _t_data )

        self.b_itemIsEditable = False
        self.b_itemIsDragEnabled = False
        self.b_itemIsDropEnabled = False
        self.b_itemIsUserCheckable = False

        # If True : drop can only be done at root
        self.b_onlyDropAtRoot = True

        # If True : item data are also copied
        # Else only item are cloned and data
        # keeps the same reference
        # This is used when dropping
        self.b_dropDataDeepCopy = False

        # Force data to be unique when drop
        self.b_forceDropDataUnicity = True

        self.b_singleMimeType = True
        self.cls_mimetype = QArkTreeItemMimeData

        #self.b_contextMenuIsEnabled = False


    def initMultiMimeType(self):
        self.b_singleMimeType = False
        self.cls_mimetype = [ QArkTreeItemMimeData ]


    def appendMimeType( self, _cls_class ):
        if self.b_singleMimeType:
            raise Exception('Calling appendMimeType is not permitted with a single mime type model')

        self.cls_mimetype.append( _cls_class )


    def setMimeType( self, _cls_class ):
        if not self.b_singleMimeType:
            raise Exception('Calling setMimeType is not permitted with a multi mime type model')

        self.cls_mimetype = _cls_class



    def encodeMime( self, _x_object, _u_indexMimeType=None ):
        if self.b_singleMimeType:
            return self.cls_mimetype(_x_object)
        else:
            return self.cls_mimetype[_u_indexMimeType](_x_object)



    def setForceDropDataUnicity( self, _b_bool=True ):
        self.b_forceDropDataUnicity = _b_bool



    def setItemIsEditable( self, _b_enabled=True ):
        self.b_itemIsEditable = _b_enabled



    def setItemIsDropEnabled( self, _b_enabled=True ):
        self.b_itemIsDropEnabled = _b_enabled



    def setItemIsDragEnabled( self, _b_enabled=True ):
        self.b_itemIsDragEnabled = _b_enabled



    def setItemIsUserCheckable( self, _b_enabled=True ):
        self.b_itemIsUserCheckable = _b_enabled



    def setOnlyDropAtRoot( self, _b_bool=True ):
        self.b_onlyDropAtRoot = _b_bool



    def setDropDataDeepCopy( self, _b_bool=True ):
        self.b_dropDataDeepCopy = _b_bool



    #def enableContextMenu(self):
        #self.b_contextMenuIsEnabled = True
        #self.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        #self.customContextMenuRequested.connect( self.handleContextMenuRequest )




    def getRootItem( self ):
        return self.o_rootItem




    def getItem( self, o_index ):
        """
        Since the model's interface to the other model/view components
        is based on model indexes, and the internal data structure is
        item-based, many of the functions implemented by the model need
        to be able to convert any given model index to its corresponding
        item. For convenience and consistency, we have defined a getItem()
        function to perform this repetitive task

        This function assumes that each model index it is passed
        corresponds to a valid item in memory. If the index is invalid,
        or its internal pointer does not refer to a valid item, the root
        item is returned instead.
        """
        if o_index.isValid():
            o_item = o_index.internalPointer()
            if o_item:
                return o_item

        return self.o_rootItem







    def rowCount( self, parent=None ):
        """
        The rowCount() function simply returns the number of child items
        for the TreeItem that corresponds to a given model index, or the
        number of top-level items if an invalid index is specified
        """
        if parent.column() > 0:
            return 0

        return self.getItem(parent).childCount()



    def columnCount( self, parent=None ):
        """
        Since each item manages its own column data, the columnCount()
        function has to call the item's own columnCount() function to
        determine how many columns are present for a given model index.
        As with the rowCount() function, if an invalid model index is
        specified, the number of columns returned is determined from the
        root item
        """
        if parent and parent.isValid():
            return parent.internalPointer().columnCount()

        else:
            return self.o_rootItem.columnCount()



    #def index( self
              #, row
              #, column
              #, parent
              #):
        #"""
        #Models must implement an index() function to provide indexes for
        #views and delegates to use when accessing data.
        #Indexes are created for other components when they are referenced
        #by their row and column numbers, and their parent model index.
        #If an invalid model index is specified as the parent, it is up
        #to the model to return an index that corresponds to a top-level
        #item in the model.

        #When supplied with a model index, we first check whether it is
        #valid. If it is not, we assume that a top-level item is being
        #referred to; otherwise, we obtain the data pointer from the model
        #index with its internalPointer() function and use it to reference
        #a QArkTreeItem object.
        #Note that all the model indexes that we construct will contain a
        #pointer to an existing QArkTreeItem, so we can guarantee that *
        #any valid model indexes that we receive will contain a valid data
        #pointer.
        #"""
        #if not self.hasIndex( row, column, parent ):
            #return QtCore.QModelIndex()

        #if not parent.isValid():
            #parentItem = self.o_rootItem
        #else:
            #parentItem = parent.internalPointer()


        ##Since the row and column arguments to this function refer to a
        ##child item of the corresponding parent item, we obtain the item
        ##using the QArkTreeItem.child() function.
        ##The createIndex() function is used to create a model index to be
        ##returned. We specify the row and column numbers, and a pointer
        ##to the item itself.
        ##The model index can be used later to obtain the item's data.
        #childItem = parentItem.child(row)

        #if childItem:
            #return self.createIndex(row, column, childItem)

        #else:
            #return QtCore.QModelIndex()


    def index( self
              , row
              , column
              , parent
              ):
        """
        The model needs to be able to generate model indexes to allow
        other components to request data and information about its
        structure. This task is performed by the index() function, which
        is used to obtain model indexes corresponding to children of a
        given parent item
        """
        # In this model, we only return model indexes for child items
        # if the parent index is invalid (corresponding to the root item)
        # or if it has a zero column number.
        if parent.isValid() and parent.column() != 0:
            return QtCore.QModelIndex()

        if not self.hasIndex( row, column, parent ):
            return QtCore.QModelIndex()

        parentItem = self.getItem(parent)
        childItem = parentItem.child(row)


        if childItem:
            return self.createIndex(row, column, childItem)

        else:
            return QtCore.QModelIndex()




    def parent(self, index):
        """
        Returns the parent QModelIndex
        """
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        #We only need to ensure that we never return a model index
        #corresponding to the root item. To be consistent with the way
        #that the index() function is implemented, we return an invalid
        #model index for the parent of any top-level items in the model.
        if parentItem is self.o_rootItem:
            return QtCore.QModelIndex()

        if parentItem is None:
            return QtCore.QModelIndex()

        #When creating a model index to return, we must specify the row
        #and column numbers of the parent item within its own parent.
        #We can easily discover the row number with the QArkTreeItem.row()
        #function, but we follow a convention of specifying 0 as the
        #column number of the parent. The model index is created with
        #createIndex() in the same way as in the index() function.
        return self.createIndex( parentItem.childNumber(), 0, parentItem )




    def emitAllDataChanged(self):
        #parentItem = self.getRootItem()

        #index0 = self.createIndex( 0, 0, self.getRootItem().child(0) )
        #index1 = self.createIndex( len(self.getRootItem().getChildren())-1
                                  #, 0, self.getRootItem().getChildren()[-1] )

        self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )





    def data( self, index, role ):
        """
        Returns data
        """
        if not index.isValid():
            return QtCore.QVariant()

        #if role in ( QtCore.Qt.DisplayRole
                    #,QtCore.Qt.EditRole
                    #,QtCore.Qt.UserRole
                    #):
            # Data is obtained from the model via data(). Since the item
            # manages its own columns, we need to use the column number
            # to retrieve the data with the QArkTreeItem.data() function
        item = self.getItem(index)
        return item.data(index.column(), role)

        #if role == QtCore.Qt.UserRole:
            #if item:
                #return item

        #return QtCore.QVariant()



    def flags( self, index ):
        """
        To enable items to be edited and selected, the flags() function
        needs to be implemented so that it returns a combination of flags
        that includes the Qt::ItemIsEditable and Qt::ItemIsSelectable
        flags as well as Qt::ItemIsEnabled
        """
        if not index.isValid():
            if self.b_itemIsDropEnabled:
                return QtCore.Qt.ItemIsDropEnabled
            else:
                return 0;

        u_flag = QtCore.Qt.ItemIsEnabled\
               | QtCore.Qt.ItemIsSelectable

        if self.b_itemIsEditable:
            u_flag = u_flag | QtCore.Qt.ItemIsEditable

        if self.b_itemIsDragEnabled:
            u_flag = u_flag | QtCore.Qt.ItemIsDragEnabled

        if self.b_itemIsDropEnabled:
            u_flag = u_flag | QtCore.Qt.ItemIsDropEnabled

        if self.b_itemIsUserCheckable:
            u_flag = u_flag | QtCore.Qt.ItemIsUserCheckable

        return u_flag


    #def headerData( self, column, orientation, role ):
        #if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole ):
            #try:
                #return QtCore.QVariant( "" )
            #except IndexError:
                #pass

        #return QtCore.QVariant()




    def headerData( self, column, orientation, role ):
        try:
            if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole ):
                return self.o_rootItem.data( column )
        except:
            pass
        
        return QtCore.QVariant()



    def setupModelData( self, _t_data ):
        for _o_item in _t_data:
            self.o_rootItem.appendChild( _o_item )





    def insertColumns( self
                      , position
                      , columns
                      , parent
                      ):
        """
        """
        self.beginInsertColumns( parent, position, position + columns - 1)
        b_success = self.o_rootItem.insertColumns( position, columns )
        self.endInsertColumns()

        return b_success



    def insertRows( self
                   , position
                   , rows
                   , parent
                   ):
        """
        """
        parentItem = self.getItem(parent)

        self.beginInsertRows(parent, position, position + rows - 1)
        b_success = parentItem.insertChildren(position, rows, self.o_rootItem.columnCount())
        self.endInsertRows()

        return b_success




    def removeColumns(self
                      , position
                      , columns
                      , parent
                      ):
        """
        """
        self.beginRemoveColumns( parent, position, position + columns - 1)
        b_success = self.o_rootItem.removeColumns( position, columns )
        self.endRemoveColumns()

        if self.o_rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        return b_success



    def removeRows( self
                    , position
                    , rows
                    , parent
                    ):
        """
        """
        parentItem = self.getItem(parent)

        if parentItem is None:
            parentItem = self.getRootItem()
            parent = QtCore.QModelIndex()

        self.beginRemoveRows( parent, position, position + rows - 1)
        b_success = parentItem.removeChildren( position, rows )
        self.endRemoveRows()

        return b_success

        



    def moveRows( self
                 , srcRow
                 , dstRow
                 , count
                 , srcParent
                 , dstParent
                 ):
        """
        The sourceParent index corresponds to the parent from which the rows are moved;
        sourceFirst and sourceLast are the first and last row numbers of the rows to be moved.
        The destinationParent index corresponds to the parent into which those rows are moved.
        The destinationChild is the row to which the rows will be moved.
        That is, the index at row sourceFirst in sourceParent will become row destinationChild in destinationParent, followed by all other rows up to sourceLast.

        However, when moving rows down in the same parent (sourceParent and destinationParent are equal), the rows
        will be placed before the destinationChild index. That is, if you wish to move rows 0 and 1 so they will
        become rows 1 and 2, destinationChild should be 3. In this case, the new index for the source row i
        (which is between sourceFirst and sourceLast) is equal to (destinationChild-sourceLast-1+i).

        Note that if sourceParent and destinationParent are the same, you must ensure that the destinationChild
        is not within the range of sourceFirst and sourceLast + 1.
        You must also ensure that you do not attempt to move a row to one of its own children or ancestors.
        This method returns false if either condition is true, in which case you should abort your move operation.
        
        To move rows within the same parent, specify the row to move them to.
        
        For example, as shown in the diagram, we move one item from row 2 to row 0, so sourceFirst and sourceLast are 2 and destinationChild is 0.
        
         beginMoveRows(parent, 2, 2, parent, 0);
        
        Note that other rows may be displaced accordingly. Note also that when moving items within the same parent you should not attempt invalid or no-op moves. In the above example, item 2 is at row 2 before the move, so it can not be moved to row 2 (where it is already) or row 3 (no-op as row 3 means above row 3, where it is already)
        Moving rows in the same parent down	To move rows within the same parent, specify the row to move them to.
        
        For example, as shown in the diagram, we move one item from row 2 to row 4, so sourceFirst and sourceLast are 2 and destinationChild is 4.
        
         beginMoveRows(parent, 2, 2, parent, 4);
        
        Note that other rows may be displaced accordingly.
        
        http://qt.apidoc.info/4.8.5/qabstractitemmodel.html#beginMoveRows
        """
        # WORK FOR MOVE UP AND MOVE DOWN 1 ITEM
        # ADD MORE CHECK IN OTHER USE CASE
        srcParentItem = self.getItem(srcParent)
        dstParentItem = self.getItem(dstParent)
        
        if srcParentItem is None:
            srcParentItem = self.getRootItem()
            srParent = QtCore.QModelIndex()

        if dstParentItem is None:
            dstParentItem = self.getRootItem()
            dstParent = QtCore.QModelIndex()


        # First check srcRow
        if srcRow < 0 or srcRow > srcParentItem.childCount():
            return False

        # First check dstRow
        if srcRow < 0 or srcRow > srcParentItem.childCount():
            return False


        dstRowNew = dstRow
        srcRowNew = srcRow
        insertRow = dstRow

        # Check parent and destination indexes. If equals we must redefine new rows indexes
        if srcParent is dstParent:
            
            print( 'src is dest' )

            if srcRow == dstRow:
                # No move ; return True
                return True

            if srcRow < dstRow:
                dstRowNew = dstRow + count
                insertRow = dstRow - count + 1

            #if srcRow > dstRow:
                #srcRowNew = srcRow + count
        
        b_beginMoveRows = self.beginMoveRows( srcParent, srcRowNew, srcRowNew+count-1, dstParent, dstRowNew )

        t_children = [ srcParentItem.popChild(srcRow) for i in range(count) ]

        for i, o_child in enumerate(t_children):
            o_child.setParent( dstParentItem )
            dstParentItem.insertChild( insertRow+i, o_child )

        b_endMoveRows = self.endMoveRows()
        
        return True


    #def moveRow( self
                #, srcRow
                #, dstRow
                #, count
                #, parent
                #):
        #"""
        #@param srcRow : source row index
        #@type srcRow : C{int}
        #@param dstRow : destination row index
        #@type dstRow : C{int}
        #@param count : number of row to move
        #@type count : C{int}
        #@param parent : parent index
        #@type parent : L{QtWidgets.QModelIndex}
        #"""
        #parentItem = self.getItem(parent)

        #if parentItem is None:
            #parentItem = self.getRootItem()
            #parent = QtCore.QModelIndex()

        #if srcRow < 0 or srcRow > parentItem.childCount() \
          #or dstRow < 0 or dstRow > parentItem.childCount():
            #return False

        #if srcRow == dstRow:
            #return True


        #dstRowNew = dstRow
        #srcRowNew = srcRow

        #if srcRow <= dstRow: dstRowNew = dstRow + 1
        #if srcRow > dstRow: srcRowNew = srcRow + count

        #if not self.insertRows( dstRowNew, count, parent ):
            #return False

        #t_childCopies = []
        #for i in xrange(count):
            #t_childCopies.append( copy.copy( parentItem.child( srcRow + i ) ) )

        #for i in xrange(count):
            #parentItem.insertChild( dstRow + i, t_childCopies[i] )


        #print self.removeRows( srcRowNew, count, parent )
        #self.dataChanged.emit(parent, parent)
        #return True




    def setData( self
                , index
                , value
                , role
                ):
        """
        """
        if not index.isValid():
            return False

        #if role != QtCore.Qt.EditRole:
            #return False

        item = self.getItem(index)
        b_result = item.setData( index.column(), value, role )

        if b_result:
            self.dataChanged.emit(index, index)

        return b_result



    def setHeaderData( self
                      , section
                      , orientation
                      , value
                      , role
                      ):
        """
        """
        if role != QtCore.Qt.EditRole or role != QtCore.Qt.Horizontal:
            return False


        b_result = self.o_rootItem.setData(section, value)

        if b_result:
            self.headerDataChanged.emit(orientation, section, section)

        return b_result



    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction




    #def mimeTypes(self):
        #return ['application/treeitem']


    #def mimeData( self, indexes ):
        #"""
        #"""
        #mimeData = QtCore.QMimeData()
        #encodedData = QByteArray
#QMimeData *DragDropListModel::mimeData(const QModelIndexList &indexes) const
 #{
     #QMimeData *mimeData = new QMimeData();
     #QByteArray encodedData;

     #QDataStream stream(&encodedData, QIODevice::WriteOnly);

     #foreach (QModelIndex index, indexes) {
         #if (index.isValid()) {
             #QString text = data(index, Qt::DisplayRole).toString();
             #stream << text;
         #}
     #}

     #mimeData->setData("application/vnd.text.list", encodedData);
     #return mimeData;
 #}

    #def dropMimeData(self, mimedata, action, row, column, parentIndex):
        #print 'call dropMimeData'
        #print mimedata.data()
        #print action
        #print row
        #print column
        #print parentIndex
        #return True

    #def dropMimeData(self, mimedata, action, row, column, parentIndex):
        #if action == Qt.IgnoreAction:
            #return True

        #dragNode = mimedata.instance()
        #parentNode = self.nodeFromIndex(parentIndex)

        ## make an copy of the node being moved
        #newNode = deepcopy(dragNode)
        #newNode.setParent(parentNode)
        #self.insertRow(len(parentNode)-1, parentIndex)
        #self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), parentIndex, parentIndex)
        #return True

    def addItem_OLD( self, o_item, o_parent=None ):
        """
        """
        position = self.o_rootItem.childCount()

        # FIXME : le passage de QtCore.QModelIndex() n'est pas bon
        #         il faudrait corriger ca mais ca a des repercussions
        #         a beaucoup d'endroits
        #         En faisant ca c'est comme si on insere tout le temps
        #         a la racine
        #         Dans l'etat cette fonction ne doit etre appellee
        #         que pour l'insertion d'un fils direct.
        self.beginInsertRows( QtCore.QModelIndex(), position, position )

        if o_parent is None:
            self.o_rootItem.appendChild( o_item )
        else:
            o_parent.appendChild( o_item )

        self.endInsertRows()

        self.itemAddedSignal.emit( o_item )
        #self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )



    def getItemIndex( self, _o_item ):
        t_parents = []
        o_current = _o_item

        if _o_item is None or _o_item is self.o_rootItem:
            return QtCore.QModelIndex()


        # On parcours les parents jusqu'au root
        while not o_current.o_parentItem is self.o_rootItem \
              and not o_current.o_parentItem is None:
            t_parents.append( o_current.o_parentItem )
            o_current = o_current.o_parentItem

        o_parentIndex = QtCore.QModelIndex()

        for o_currentParent in t_parents[::-1]:
            o_parentIndex = self.index( o_currentParent.childNumber(), 0, o_parentIndex )

        return self.index( _o_item.childNumber(), 0, o_parentIndex )



    def addItem( self, o_item, o_parent=None ):
        """
        """
        if o_parent is None:
            position = self.o_rootItem.childCount()
            o_parentIndex = QtCore.QModelIndex()

        else:
            position = o_parent.childCount()
            o_parentIndex = self.getItemIndex( o_parent )
            #o_parentIndex = self.index( o_parent.childNumber(), 0, o_parent )

        self.beginInsertRows( o_parentIndex, position, position )

        if o_parent is None:
            self.o_rootItem.appendChild( o_item )
        else:
            o_parent.appendChild( o_item )

        self.endInsertRows()

        self.itemAddedSignal.emit( o_item )
        #self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )



    def insertItem( self, u_index, o_item, o_parent=None ):
        """
        """
        position = u_index

        if o_parent is None:
            o_parentIndex = QtCore.QModelIndex()

        else:
            o_parentIndex = self.getItemIndex( o_parent )
            #o_parentIndex = self.index( o_parent.childNumber(), 0, o_parent )

        self.beginInsertRows( o_parentIndex, position, position )

        if o_parent is None:
            self.o_rootItem.insertChild( u_index, o_item )
        else:
            o_parent.insertChild( u_index, o_item )

        self.endInsertRows()

        self.itemAddedSignal.emit( o_item )
        #self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )


    def removeItem( self, o_item ):
        """
        """
        try:
            #o_parentIndex = self.createIndex(0, 0, o_item.parent())
            o_parentIndex = self.getItemIndex( o_item.parent() )
            self.removeRows( o_item.childNumber(), 1, o_parentIndex )
            self.itemRemovedSignal.emit( o_item )

        except Exception as e:
            print( e )
            pass




    def moveItemUp( self, o_item ):
        """
        Move an item up in same parent
        """
        o_itemIndex = self.getItemIndex( o_item )
        o_parent = o_item.parent()
        o_parentIndex = self.getItemIndex( o_parent )
        
        u_childPosition = o_item.childNumber()
        
        # Do not move if already at top
        if u_childPosition == 0:
            return True
        
        self.moveRows( u_childPosition, u_childPosition-1, 1, o_parentIndex, o_parentIndex )



    def moveItemDown( self, o_item ):
        """
        Move an item down in same parent
        """
        o_itemIndex = self.getItemIndex( o_item )
        o_parent = o_item.parent()
        o_parentIndex = self.getItemIndex( o_parent )
        
        u_childPosition = o_item.childNumber()
        
        # Do not move if already at bottom
        if u_childPosition == o_parent.childCount() - 1:
            return True
        
        self.moveRows( u_childPosition, u_childPosition+1, 1, o_parentIndex, o_parentIndex )





    def mimeTypes(self):
        types = []
        
        if self.b_singleMimeType:
            types.append( self.cls_mimetype.MIME_TYPE )
        else:
            for o_mimetype in self.cls_mimetype:
                types.append( o_mimetype.MIME_TYPE )
        #types.append('application/qmimedata-instance')
        return types





    def getCleanItemsSelection( self, indexes ):
        """
        Do some cleaning
        We dont want to pass child if its parent is also selected
        """
        t_listItems = []
        t_cleanItemList = []

        for index in indexes:
            item = self.getItem(index)
            t_listItems.append( item )

        for item in t_listItems:
            b_check = True
            parentItem = item.parent()

            while not parentItem is None:
                # filter t_listItems with type of parentItem
                t_filteredListItems = [ o for o in t_listItems
                                        if isinstance( o, type(parentItem) ) and isinstance( parentItem, type(o) )
                                       ]

                if parentItem in t_filteredListItems:
                    b_check = False
                    #print 'not including item %s' % item.getItemData()
                    break
                parentItem = parentItem.parent()

            if b_check:
                t_cleanItemList.append(item)

        return t_cleanItemList




    def mimeData(self, indexes):
        """
        This function is used for drag
        """
        t_listItems = []
        for index in indexes:
            item = self.getItem(index)
            t_listItems.append( item )

        # Lets do some cleaning :
        # We dont want to pass child if its parent is also
        # selected
        t_cleanItemList = []

        for item in t_listItems:
            b_check = True
            parentItem = item.parent()
            while not parentItem is None:
                if parentItem in t_listItems:
                    b_check = False
                    #print 'not including item %s' % item.getItemData()
                    break
                parentItem = parentItem.parent()

            if b_check:
                t_cleanItemList.append(item)

        mimeData = self.encodeMime(t_cleanItemList)

        return mimeData


    def dropMimeData(self, mimedata, action, row, column, parentIndex):
        """
        This function is used for drop
        """
        if action == QtCore.Qt.IgnoreAction:
            return True

        if self.b_onlyDropAtRoot:
            parentNode = self.getRootItem()
        else:
            parentNode = self.getItem(parentIndex)

        t_dragNodes = mimedata.instance()
        t_nodesToRemove = []

        if self.b_forceDropDataUnicity:
            t_cleanNodes = []

            for o_node in t_dragNodes:

                # Check first if o_node direct data already exists
                b_exists\
                ,o_existingItem = self.getRootItem().checkDataForwardExists( o_node )

                if b_exists:

                    # It exists : dont add the node
                    continue

                else:
                    # Check if o_node childrens data exists (recursively)
                    b_exists\
                    ,o_existingItem = self.getRootItem().checkDataBackwardExists( o_node )

                    if b_exists:

                        if not o_existingItem is self.getRootItem():

                            # Add the item to add
                            t_cleanNodes.append( o_node )

                            # Remove existing item
                            t_nodesToRemove.append( o_existingItem )

                    else:
                        t_cleanNodes.append( o_node )


            t_dragNodes = t_cleanNodes


        for o_node in t_nodesToRemove:
            try:
                print( 'remove item %s' % o_node )
                self.removeItem(o_node)
            except:
                pass


        for o_node in t_dragNodes:

            if self.b_dropDataDeepCopy:
                newNode = copy.deepcopy( o_node )

            else:
                # Deep copy for item is done
                # but the data links to the same object
                newNode = o_node.cloneItemOnly(parentNode)

            newNode.setParent(parentNode)
            self.addItem(newNode, parentNode )

        # make an copy of the node being moved
        #newNode = deepcopy(dragNode)
        #print newNode
        #newNode.setParent(parentNode)
        #self.insertRows( parentNode.childCount(), 1, parentIndex )
        #self.addItem( newNode, parentNode )

        self.dataChanged.emit( parentIndex, parentIndex )
        return True



    def sortItem( self, parent, order = QtCore.Qt.AscendingOrder ):
        # Sort children
        b_reverse = order !=  QtCore.Qt.AscendingOrder
        parent.getChildren().sort( reverse=b_reverse )

        for o_child in parent.getChildren():
            self.sortItem(o_child, order)


    def sort( self, column, order = QtCore.Qt.AscendingOrder):
        self.layoutAboutToBeChanged.emit()
        self.sortItem( self.getRootItem() )
        self.layoutChanged.emit()





    def getItems( self, parent=None ):
        if parent is None:
            parent = self.getRootItem()

        t_items = parent.getChildren()

        for o_child in parent.getChildren():
            t_items.extend( self.getItems(o_child) )

        return t_items



    @QtCore.pyqtSlot( QtCore.QObject )
    def handleContextMenuRequested( self, _o_point ):
        """
        Handle context menu request method
        """
        print( 'handle context menu' )

        # Check here if simple selection, multiple selection
        # or no selection









