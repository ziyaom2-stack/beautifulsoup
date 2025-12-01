class SoupReplacer:
    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        #Milestone2
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        #Milestone 3
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer