from product_data_manager import ProductData
from sheet_data_manager import SheetData
from notification_manager import NotificationManager

# class objects
product_data = ProductData()
sheet_data = SheetData()
price_notification = NotificationManager()

# product = product_data.get_product_data()
# sheet_data.post_data(product)
cheaper_prices = sheet_data.check_prices()

price_notification.send_message(cheaper_prices)

















# TODO: Create a simple landing page that allows the user to paste item link





