class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if len(self.products) - k < 1:
            return 0
        else:
            return self.products[-1]//self.products[-(k+1)]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)