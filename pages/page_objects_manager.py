class PageObjectManager:
    def __init__(self):
        self.pages = {}

    def get_page(self, page_class, driver):
        """Returns an instance of the requested page, initializing it with the driver if not already done."""
        if page_class not in self.pages:
            self.pages[page_class] = page_class(driver)
        return self.pages[page_class]
