import matplotlib.pyplot as plt

def read_sales_data(file_path):
  """Функция принимает путь к файлу и возвращает список продаж"""
  sales_data = []
  with open(file_path, "r", encoding='utf-8') as f:
    for line in f:
      product_name, quantity, price, date = line.strip().split(",")
      sales_data.append({
        "product_name": product_name,
        "quantity": int(quantity),
        "price": float(price),
        "date": date
      })
  return sales_data

def total_sales_per_product(sales_data):
  """Функция принимает список продаж и возвращает общую сумму продаж по продуктам"""
  sales_per_product = {}
  for sale in sales_data:
    product_name = sale["product_name"]
    if product_name in sales_per_product:
      sales_per_product[product_name] += sale["quantity"] * sale["price"]
    else:
      sales_per_product[product_name] = sale["quantity"] * sale["price"]
  return sales_per_product

def sales_over_time(sales_data):
  """Функция принимает список продаж и возвращает общую сумму продаж по дате"""
  sales_over_time = {}
  for sale in sales_data:
    product_date = sale["date"]
    if product_date in sales_over_time:
      sales_over_time[product_date] += sale["quantity"] * sale["price"]
    else:
      sales_over_time[product_date] = sale["quantity"] * sale["price"]
  return sales_over_time

file_path = 'sales_data.csv'
sales_data = read_sales_data(file_path)
total_sales = total_sales_per_product(sales_data)
sales_date = sales_over_time(sales_data)

most_profitable_product = max(total_sales, key=total_sales.get)
print("Продукт с наибольшей выручкой:", most_profitable_product)

most_profitable_date = max(sales_date, key=sales_date.get)
print("День с наибольшей суммой продаж:", most_profitable_date)

def plot_sales_per_product(total_sales):
  """Функция строит график продаж по продуктам"""
  products = list(total_sales.keys())
  sales = list(total_sales.values())
  plt.figure()
  plt.bar(products, sales)
  plt.xlabel("Продукты")
  plt.ylabel("Общая сумма продаж")
  plt.title("Общая сумма продаж по продуктам")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("sales_per_product.png")  # Если в интеракт режиме, то для удобства сохраняю в пнг

def plot_sales_over_time(sales_date):
  """Функция строит график продаж по дате"""
  dates = list(sales_date.keys())
  sales = list(sales_date.values())
  plt.figure()
  plt.plot(dates, sales)
  plt.xlabel("Даты")
  plt.ylabel("Общая сумма продаж")
  plt.title("Общая сумма продаж по дням")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("sales_over_time.png")  # Если в интеракт режиме, то для удобства сохраняю в пнг

plot_sales_per_product(total_sales)
plot_sales_over_time(sales_date)
plt.show()







