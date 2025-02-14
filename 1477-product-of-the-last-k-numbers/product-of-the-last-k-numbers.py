class ProductOfNumbers:

    def __init__(self):
        self.products = {0:1}
        self.current_length = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.products = {0:1}
            self.current_length = 0
        else:
            self.current_length += 1
            self.products[self.current_length] = self.products[self.current_length-1]*num
        

    def getProduct(self, k: int) -> int:
        if self.current_length - k < 0:
            return 0
        else:
            return self.products[self.current_length]//self.products[self.current_length - k]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)