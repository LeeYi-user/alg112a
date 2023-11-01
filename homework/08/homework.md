# 傑佛瑞·辛頓

2018 年圖靈獎得主

## 人物生平

辛頓於1970年在英國劍橋大學獲得實驗心理學學士學位。此後於1978年在愛丁堡大學獲得人工智慧博士學位。此後曾在薩塞克斯大學、加州大學聖地牙哥分校、劍橋大學、卡內基梅隆大學和倫敦大學學院工作。他是蓋茨比計算神經科學中心的創始人，目前擔任多倫多大學計算機科學系教授。

## 獲獎原因

辛頓是反向傳播算法和對比散度算法的發明人之一，也是深度學習的積極推動者，被譽為「深度學習之父」。辛頓因在深度學習方面的貢獻與約書亞·班吉歐和楊立昆一同被授予了2018年的圖靈獎。他研究了使用神經網絡進行機器學習、記憶、感知和符號處理的方法，並在這些領域發表了超過200篇論文。他是將反向傳播算法引入多層神經網絡訓練的學者之一。他與大衛·阿克利、特里·賽傑諾維斯基一同發明了波爾茲曼機。他對於神經網絡的其它貢獻包括分散表示（distributed representation）、時延神經網絡、專家混合系統（mixtures of experts）、亥姆霍茲機（Helmholtz machines）等。

## 知名論文

### [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0)

反向傳播（英語：Backpropagation，意為誤差反向傳播，縮寫為BP）是對多層類神經網路進行梯度下降的演算法，這篇論文講述的是世界上第一篇反向傳播演算法，標題的意思是透過反向傳播錯誤來學習表徵。文章的一開頭就給出了反向傳播演算法的原理:

> The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the dilference between the actual output vector of the net and the desired output vector.

此程式反覆調整網路中連接的權重，以使網路的實際輸出向量與期望輸出向量之間的偏差最小化。而這個過程就是學習的過程，也就是用鏈式法則以網路每層的權重為變數計算損失函數的梯度，並更新權重來最小化損失函數，學習率就是用來調整權重的超參數。該過程主要由兩個階段組成：激勵傳播與權重更新。

#### 第1階段：激勵傳播

每次迭代中的傳播環節包含兩步：

1. （前向傳播階段）將訓練輸入送入網路以獲得預測結果；
2. （反向傳播階段）對預測結果同訓練目標求差(損失函數)。

#### 第2階段：權重更新

對於每個突觸上的權重，按照以下步驟進行更新：

1. 將輸入激勵和回應誤差相乘，從而獲得權重的梯度；
2. 將這個梯度乘上一個比例並取反後加到權重上。

這個比例（百分比）將會影響到訓練過程的速度和效果，因此成為「訓練因子」。梯度的方向指明了誤差擴大的方向，因此在更新權重的時候需要對其取反，從而減小權重引起的誤差。

第 1 和第 2 階段可以反覆迴圈迭代，直到網路對輸入的回應達到滿意的預定的目標範圍為止。

## 相關程式

網路上與反向傳播演算法相關的程式很多，最經典的便是 karpathy 的 micrograd。該專案中的 engine.py 將參數以 Value 物件的形式呈現，並搭配自動微分，在反傳遞時計算各個權重的梯度，並對其進行更新。

```py
class Value: # 含有梯度的值節點
    """ stores a single scalar value and its gradient """

    def __init__(self, data, _children=(), _op=''):
        self.data = data # 目前值
        self.grad = 0 # 梯度預設為 0
        # internal variables used for autograd graph construction
        self._backward = lambda: None # 反傳遞函數
        self._prev = set(_children) # 前面的網路節點
        self._op = _op # the op that produced this node, for graphviz / debugging / etc

    def __add__(self, other): # 加法的正向傳遞
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward(): # 加法的反向傳遞
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    def __mul__(self, other): # 乘法的正向傳遞
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward(): # 乘法的反向傳遞
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    def __pow__(self, other): # 次方的正向傳遞
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward(): # 次方的反向傳遞
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out

    def relu(self): # relu 的正向傳遞
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward(): # relu 的反向傳遞
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    def backward(self):

        # topological order all of the children in the graph
        topo = []
        visited = set()
        def build_topo(v): # 建立網路拓譜結構
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        self.grad = 1
        for v in reversed(topo): # 反向排列
            v._backward()
    # 以下這些運算，由於 + * 已被 override ，所以反向傳遞會自動建構，不需再自己加入反向傳遞函數
    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other

    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
```

## 參考資料

https://zh.wikipedia.org/zh-tw/%E5%9B%BE%E7%81%B5%E5%A5%96

https://zh.wikipedia.org/zh-tw/%E6%9D%B0%E5%BC%97%E9%87%8C%C2%B7%E8%BE%9B%E9%A1%BF

https://zh.wikipedia.org/zh-tw/%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95

https://blog.csdn.net/zbp_12138/article/details/106578443

https://www.nature.com/articles/323533a0

https://github.com/ccc-py/micrograd/blob/master/ccc/engine.py
