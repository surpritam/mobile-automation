import logging


class PageObjectManager:
    def __init__(self):
        self.pages = {}

    def get_page(self, page_class, driver):
        logging.info(f"get_page driver session id for page class {page_class}: {driver.session_id}")
        """Returns an instance of the requested page, initializing it with the driver if not already done."""
        if page_class not in self.pages:
            self.pages[page_class] = page_class(driver)
        else:
            self.pages[page_class].set_driver(driver)  # Update the driver in existing page object
        return self.pages[page_class]
