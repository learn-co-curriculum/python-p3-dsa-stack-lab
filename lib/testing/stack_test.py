from Stack import Stack

class TestStack:
    '''Class Stack in Stack.py'''

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for item in expected:
            assert(item in stk.items)

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for index in range(0,len(expected)):
            assert(expected[index] == stk.items[index])

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1,2,3,4,5])
        stk.push(0)
        expected = [0,1,2,3,4,5]
        for index in range(0,len(expected)):
            assert(expected[index] == stk.items[index])

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1,2,3,4,5])
        stk.pop()
        expected = [2,3,4,5]
        for index in range(0,len(expected)):
            assert(expected[index] == stk.items[index])

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        assert(stk.size() == len(expected))
        
    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack([])
        assert(stk.isEmpty())
        stk2 = Stack([1,2,3,4,5])
        assert(not stk2.isEmpty())

    def test_full(self):
        '''Test Stack empty() method'''
        stk = Stack([1,2,3], 1)

        assert(stk.full())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1,2,3], 1)

        assert(stk.full())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

    def test_search(self):
        '''Test Stack search() method. How far element '''
        stk = Stack([5,6,7,8,9,10])

        assert(stk.search(5) == 0)
        assert(stk.search(6) == 1)
        assert(stk.search(7) == 2)
        assert(stk.search(8) == 3)
        assert(stk.search(9) == 4)
        assert(stk.search(10) == 5)

        # Case with target not in Stack
        assert(stk.search(15) == -1)
