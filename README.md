# qt_widgetstyler
qt_widgetstyler is a small Python class intended to make the dynamic styling of Qt widgets via either PySide or PyQt a simpler task.

### Usage

Inherit WidgetStyler class:

    from qt_widgetstyler import WidgetStyler
    ws = WidgetStyler()

Create a new category. A category is a logical separation between different sections of your program's widgets, and allows you to easily apply new or updated stylesheets to one or more categories simultaneously.

    ws.new_style_category('top_navigation')

A custom widget group is created below the category. The custom widget group is a collection of individual widgets, generally of the same type (QLabel, QTableView, etc.), and all individual widget objects assigned to this custom widget group will share the same stylesheet.

    ws.add_custom_widget(category='top_navigation', widget_name='top_navigation_qlabel_text')

For this category of our program, we have three QLabel widget objects which we wish to assign to our custom widget group, QLabel1, QLabel2, and QLabel3. We can add them individually, or together in a list.

Individually:

    ws.add_widget(widget_instance=QLabel1, category='top_navigation', widget_name='top_navigation_qlabel_text')

Together:    
    
    ws.add_widgets(widget_instances_list=[QLabel2, QLabel3], category='top_navigation', widget_name='top_navigation_qlabel_text')

We now add a StyleSheet to this custom widget group, which will be shared by all the widget objects assigned to it. This only stores the StyleSheet, it does not yet apply it:

    ws.add_stylesheet(category='top_navigation', widget_name='top_navigation_qlabel_text', stylesheet='QLabel { color: rgb(0, 0, 0); }')

To apply the stylesheets to our widgets, we have three options.

We can apply one widget group's stylesheets individually:

    ws.apply_stylesheet(category='top_navigation', widget_name='top_navigation_qlabel_text')

To all widgets within one category:

    ws.apply_category_stylesheets(category='top_navigation')

Or to all of our widgets in all of our categories:

    ws.apply_all_stylesheets()

To view all of your defined categories:

    ws.show_categories()

To view all of your defined widgets within a single category:

    ws.show_category_widgets(category='top_navigation')
