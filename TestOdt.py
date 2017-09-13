from odf.opendocument import load
from odf.element import Node

def odf_dump_nodes(start_node, level=0):
    if start_node.nodeType==3:
        # text node
        if (str(start_node).strip()==('□4申請延長照護複核')):
            start_node.data='V4申請延長照護複核'
        print("  "*level, "NODE:", start_node.nodeType, ":(text):", str(start_node)," TYPE: ",type(start_node)," parentNode:",start_node.parentNode)
    else:
        # element node
        attrs= []
        for k in start_node.attributes.keys():
            attrs.append( k[1] + ':' + start_node.attributes[k])
        print("  "*level, "NODE:", start_node.nodeType, ":", start_node.qname[1], " ATTR:(", ",".join(attrs), ") ", str(start_node)," TYPE: ",type(start_node))

        for n in start_node.childNodes:
            odf_dump_nodes(n, level+1)
    return


doc = load('.\\全民健康保險居家醫療照護整合計畫收案申請書.odt')
print(doc)
odf_dump_nodes(doc.text)
doc.save('Test.odt')



