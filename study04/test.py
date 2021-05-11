import pandas as pd
import datetime

LOG_FILE_PATH = 'study04/log/log_###DATETIME###.log'
ITEM_MASTER_CSV_PATH="study04/item_master.csv"

log_file_path=LOG_FILE_PATH.replace("###DATETIME###",datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
def log(txt):
    now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logStr = '[%s: %s] %s' % ('log',now , txt)
    # ログ出力
    with open(log_file_path,mode='a', encoding='utf-8_sig') as f:
        f.write(logStr + '\n')
    print(logStr)

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    def get_price(self):
        return self.price

# KeyError対策でCSVを書き直す⇨indexありで（今はindex=falseになってる）

class Order:
    def __init__(self,item_master):
        self.order_list = []
        self.item_master = item_master

    def view_items(self):
        print("商品一覧")
        print('--------------------')
        for item in self.item_master:
            print(str(item.item_code) + ',' + str(item.item_name) + ',' + str(item.price))
        print('--------------------')

    def input_order(self):
        check = 'n'
        self.all_order_price = 0
        while check == 'n':
            order_code = int(input('オーダーする商品コードを入力してください：'))
            selected_menu = self.item_master[order_code-1]
            count = int(input('オーダーする個数を入力してください：'))
            item_total_price = selected_menu.price * count
            your_order = str(selected_menu.item_code) + ',' + str(selected_menu.item_name) + ',' + str(selected_menu.price) +'円,' + str(count) + '個,合計' + str(item_total_price) +'円'
            print('選択されたメニュー:')
            print(your_order)
            log(your_order)
            orders = [selected_menu.item_code,selected_menu.item_name,selected_menu.price,count,item_total_price]
            self.order_list.append(orders)
            self.all_order_price += item_total_price
            while check == 'y'or'n':
                check = input('オーダーを終了しますかy/n：')
                if check =='y':
                    break
                elif check == 'n' :
                    break
                else :
                    print('無効な入力です。再度入力してください')
        
    def view_order_item (self):
        print("オーダー一覧")
        print('--------------------')
        for n in self.order_list:
            print(n)
        finaly_price = '総合計' + str(self.all_order_price) + '円'
        print(finaly_price)
        log(finaly_price)
        print('--------------------')

    def payment (self):
        money = 0
        while self.all_order_price >= money :
            money = int(input('お支払い金額を入力してください：'))
            if self.all_order_price > money:
                print('お支払い金額が不足しています')
                print('再度お支払い金額を入力してくだいさい')
            else :
                break
        finaly_money = 'お預かり' + str(money) + '円'
        finaly_money_change = 'お釣り：' + str(money-self.all_order_price) + '円'
        print(finaly_money)
        print(finaly_money_change)
        log(finaly_money)
        log(finaly_money_change)

def input_item_master(ITEM_MASTER_CSV_PATH):
    item_master = []
    item_master_df = pd.read_csv(ITEM_MASTER_CSV_PATH)
    # ,dtype={"item_code":object}
    for item_code,item_name,price in zip(list(item_master_df['item_code']),list(item_master_df['item_name']),list(item_master_df['price'])):
        item_master.append(Item(item_code,item_name,price))
    return item_master

def main():
    item_master = input_item_master(ITEM_MASTER_CSV_PATH)
    print(item_master)
    order = Order(item_master)
    order.view_items()
    order.input_order()
    order.view_order_item()
    order.payment()

if __name__ == "__main__":
    main()
