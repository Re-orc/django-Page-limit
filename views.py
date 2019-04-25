def get_context_data(self,**kwargs):
        context = super(BookmarkListView,self).get_context_data(**kwargs)
        if self.request.GET:
            i = int(self.request.GET.get('page'))
        else:
            i=1
        paginator = context['paginator']
        page_range = paginator.page_range[i-1:5+i]
        context['page_range'] = page_range
        return context
