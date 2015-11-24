class WidgetStyler:
 
    def __init__(self):
        self.categories = {}
 
    def _check_category_exists(self, category):
        assert category in self.categories, 'Category "{}" does not exist. Please enter a valid category name, or use' \
                                            ' the "show_style_categories" method to list all existing ' \
                                            'categories.'.format(category)
 
    def _check_widget_exists(self, category, widget):
        self._check_category_exists(category)
        assert widget in self.categories[category], 'Widget "{}" does not exist in the "{}" category. Please enter a ' \
                                                    'valid widget name, or use the "show_category_widgets" method to ' \
                                                    'list all widgets within a category.'
 
    def _fetch_blank_widget_dict(self):
        return {
            'stylesheet': '',
            'instances': []
        }
 
    def _fetch_blank_style_dictionary(self):
        widgets = ['QLabel', 'QTableView', 'QListView', 'QPushButton', 'QRadioButton']
 
        return_dict = {}
 
        for widget in widgets:
            return_dict[widget] = self._fetch_blank_widget_dict()
 
        return return_dict
 
    def show_categories(self):
        # Method will return all categories - keys of the self.categories dictionary.
        return list(self.categories.keys())
 
    def show_category_widgets(self, category):
        # Method will return all widgets within a style.
        # Check category exists
        self._check_category_exists(category)
        return list(self.categories[category].keys())
 
    def new_style_category(self, category_desc):
        # Check that the category_desc is a string.
        assert type(category_desc) is str, 'Category description must be of string type.'
        # Check category name doesn't already exist.
        assert category_desc not in self.categories, 'Category already exists. Please use a unique category name.'
 
        self.categories[category_desc] = self._fetch_blank_style_dictionary()
 
    def add_widget(self, widget_instance, category, widget_name):
        # Check category & widget_name
        self._check_widget_exists(category, widget_name)
 
        self.categories[category][widget_name]['instances'].append(widget_instance)
 
    def add_widgets(self, widget_instances_list, category, widget_name):
        self._check_widget_exists(category, widget_name)
 
        for widget in widget_instances_list:
            self.categories[category][widget_name]['instances'].append(widget)
 
    def add_custom_widget(self, category, widget_name):
        # Check category name is valid.
        self._check_category_exists(category)
        # Check widget_name is a valid dictionary key
        assert type(widget_name) in [str, int], '"widget_name" must be of string or integer type.'
 
        # Add dictionary key
        self.categories[category][widget_name] = self._fetch_blank_widget_dict()
 
    def add_stylesheet(self, category, widget_name, stylesheet):
        # Check widget_name is valid.
        self._check_widget_exists(category, widget_name)
 
        self.categories[category][widget_name]['stylesheet'] = stylesheet
 
    def apply_stylesheet(self, category, widget_name):
        # Apply stylesheet to all instances of one widget in one category.
 
        # Check widget_name is valid.
        self._check_widget_exists(category, widget_name)
 
        for widget_instance in self.categories[category][widget_name]['instances']:
            widget_instance.setStyleSheet(self.categories[category][widget_name]['stylesheet'])
 
    def apply_category_stylesheets(self, category):
        # Apply stylesheet to all widgets within one category.
 
        # Check category name
        self._check_category_exists(category)
 
        for widget in self.categories[category]:
            for widget_instance in self.categories[category][widget]['instances']:
                widget_instance.setStyleSheet(self.categories[category][widget]['stylesheet'])
 
    def apply_all_stylesheets(self):
        # Apply all stylesheets for all widgets of all categories.
 
        for category in self.categories:
            for widget in self.categories[category]:
                for widget_instance in self.categories[category][widget]['instances']:
                    widget_instance.setStyleSheet(self.categories[category][widget]['stylesheet'])
