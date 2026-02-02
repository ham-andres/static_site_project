from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            temp = old_node.text.split(delimiter)
            if len(temp)> 1 and len(temp) % 2 == 0:
                raise Exception("Unmatched Delimiter")
            else:
                for i,part in enumerate(temp):
                    if part =="":
                        continue
                    if i % 2 ==0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
                


    return new_nodes


