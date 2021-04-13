import pandas as pd
import datetime

LOG_FILE_PATH = 'study04/log/log_###DATETIME###.log'
ITEM_MASTER_CSV_PATH="study04/item_master.csv"

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    def get_price(self):
        return self.price

log_file_path=LOG_FILE_PATH.replace("###DATETIME###",datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
def log(txt):
    now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logStr = '[%s: %s] %s' % ('log',now , txt)
    # ログ出力
    with open(log_file_path,mode='a', encoding='utf-8_sig') as f:
        f.write(logStr + '\n')
    print(logStr)




# KeyError対策でCSVを書き直す⇨indexありで（今はindex=falseになってる）

def order():
    item_master = []
    item_master_df = pd.read_csv(ITEM_MASTER_CSV_PATH)
    # ,dtype={"item_code":object}
    for item_code,item_name,price in zip(list(item_master_df['item_code']),list(item_master_df['item_name']),list(item_master_df['price'])):
        item_master.append(Item(item_code,item_name,price))

    print("商品一覧")
    print('--------------------')
    for item in item_master:
        print(str(item.item_code) + ',' + str(item.item_name) + ',' + str(item.price))
    print('--------------------')

    check = 'n'
    order_list = []
    all_order_price = 0
    while check == 'n':
        order = int(input('オーダーする商品コードを入力してください：'))
        selected_menu = item_master[order-1]
        count = int(input('オーダーする個数を入力してください：'))
        item_total_price = selected_menu.price * count
        your_order = str(selected_menu.item_code) + ',' + str(selected_menu.item_name) + ',' + str(selected_menu.price) +'円,' + str(count) + '個,合計' + str(item_total_price) +'円'
        print('選択されたメニュー:')
        print(your_order)
        log(your_order)
        orders = [selected_menu.item_code,selected_menu.item_name,selected_menu.price,count,item_total_price]
        order_list.append(orders)
        all_order_price += item_total_price
        while check == 'y'or'n':
            check = input('オーダーを終了しますかy/n：')
            if check =='y':
                break
            elif check == 'n' :
                break
            else :
                print('無効な入力です。再度入力してください')

    print("オーダー一覧")
    print('--------------------')
    for n in order_list:
        print(n)
    finaly_price = '総合計' + str(all_order_price) + '円'
    print(finaly_price)
    log(finaly_price)
    print('--------------------')

    money = 0
    while all_order_price >= money :
        money = int(input('お支払い金額を入力してください：'))
        if all_order_price > money:
            print('お支払い金額が不足しています')
            print('再度お支払い金額を入力してくだいさい')
        else :
            break
    finaly_money = 'お預かり' + str(money) + '円'
    finaly_money_change = 'お釣り：' + str(money-all_order_price) + '円'
    print(finaly_money)
    print(finaly_money_change)
    log(finaly_money)
    log(finaly_money_change)

def main():
    order()

if __name__ == "__main__":
    main()
