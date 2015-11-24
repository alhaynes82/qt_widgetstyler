# qt_widgetstyler
QtWidgetStyler is a small Python class intended to make the dynamic styling of Qt widgets via either PySide or PyQt a simpler task.

### Usage

Initialise WidgetStyler.

    from qt_widgetstyler import WidgetStyler
    sw = WidgetStyler()

Create a new widget category. A category is a logical separation between different sections of your program's widgets, and allows you to easily apply new or updated stylesheets to one or more categories.

    sw.new_style_category('top_navigation')

A custom widget is created below the category. This custom widget falls under the category we've defined, and all individual widgets assigned to this custom widget will share the same stylesheet.

    sw.add_custom_widget(category='top_navigation', widget_name='top_navigation_qlabel_text')

For this category of our program, we have three QLabel widget objects which we wish to assign to this custom_widget, QLabel1, QLabel2, and QLabel3. We can add them individually or together in a list.

    sw.add_widget(widget_instance=QLabel1, category='top_navigation', widget_name='top_navigation_qlabel_text')
    sw.add_widgets(widget_instances_list=[QLabel2, QLabel3], category='top_navigation', widget_name='top_navigation_qlabel_text')

We now add a StyleSheet to this custom widget, which will be shared by all the widget objects assigned to it.

    sw.add_stylesheet(category='top_navigation', widget_name='top_navigation_qlabel_text', stylesheet='QLabel { color: rgb(0, 0, 0); }')

To apply the stylesheets to our widgets, we have three options.

We can apply one widget group's stylesheets individually:

    sw.apply_stylesheet(category='top_navigation', widget_name='top_navigation_qlabel_text')

To all widgets within one category:

    sw.apply_category_stylesheets(category='top_navigation')

Or to all of our widgets in all of our categories:

    sw.apply_all_stylesheets()

To view all of your defined categories:

    sw.show_style_categories()

To view all of your defined widgets within one category:

    sw.show_category_widgets(category='top_navigation')
