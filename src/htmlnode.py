




class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props= None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html method not implemented")

	def props_to_html(self):
		if self.props is None:
			return ""
		f_string = ""
		for key,value in self.props.items():
			f_string = f_string + f' {key}="{value}"'
		return f_string

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
	def __init__(self,tag,value,props=None):
		# we use the super therefore we dont have to assign self.tag = tag , 
		# if we would have a new parameter which the parent class doesnt have then we would need it example class self.class = class
		super().__init__(tag=tag,value=value,children=None,props=props)
		
		

	def to_html(self):
		if self.value == None:
			raise ValueError("All leaf nodes must have a value")
		if self.tag == None:
			return self.value
		else:
			if self.props == None:
				return f"<{self.tag}>{self.value}</{self.tag}>"
			else:
				result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
				return result


class ParentNode(HTMLNode):
	def __init__(self, tag, children, props = None):
		super().__init__(tag = tag, children = children, props = props)

	def to_html(self):
		child_html_string = ""
		if self.tag == None:
			raise ValueError("ParentNode must have tag")

		if self.children == None or self.children == []:
			raise ValueError("ParentNode must have children")
		else:
			for child in self.children:
				child_html_string = child_html_string + child.to_html()
			return f'<{self.tag}>{child_html_string}</{self.tag}>'




	def __repr__(self):
		return f"LeafNode(tag:{self.tag}, value:{self.value}, props:{self.props})"
