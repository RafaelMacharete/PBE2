class Bank():

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customer_registration = []

    def register_customer(self, customer_id, customer_name, customer_balance):
        self.customer_id = customer_id
        self.customer_registration.append(
            {'id': customer_id, 
             'name': customer_name,
             'balance': customer_balance
             })

    def action_on_account(self, option_chosen, value, account_transfer_id = None):
        
        # Withdrawal
        if option_chosen == 1:
            self.customer_registration[self.customer_id]['balance'] -= value
            print(f'o {self.customer_registration[self.customer_id]['name']} agora tem: {self.customer_registration[self.customer_id]['balance']}')
        # Deposit
        elif option_chosen == 2:
            self.customer_registration[self.customer_id]['balance'] += value
            print(f'o {self.customer_registration[self.customer_id]['name']} agora tem: {self.customer_registration[self.customer_id]['balance']}')
        # Transfer
        elif option_chosen == 3 and account_transfer_id != None:
            self.customer_registration[self.customer_id]['balance'] -= value
            self.customer_registration[account_transfer_id]['balance'] += value
            print(f'o {self.customer_registration[self.customer_id]['name']} transferiu {value} para: {self.customer_registration[account_transfer_id]['name']}')

            
bank1 = Bank('Bradesco')
bank2 = Bank('Inter')

bank1.register_customer(0, 'Rafael', 10)
bank1.register_customer(1, 'Leafar', 20)

bank2.register_customer(0, 'asd', 30)
bank2.register_customer(1, 'dsa', 40)

bank1.action_on_account(3,10, 0)