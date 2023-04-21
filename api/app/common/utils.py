def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions