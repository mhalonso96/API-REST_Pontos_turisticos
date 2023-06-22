def reprova_comment(modeladmin, request, queryset):
    queryset.update(approved=False)

def aprova_comment(modeladmin, request, queryset):
    queryset.update(approved=True)
    

reprova_comment.short_description = 'reprova comentario'
aprova_comment.short_description = 'aprova comentario'