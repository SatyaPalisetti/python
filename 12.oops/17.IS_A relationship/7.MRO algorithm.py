########## Method Resolution Order (MRO) Algorithm / c3 Linearization##########
'''
This algorithm is used to solve the diamond problem in multiple inheritance or Hybrid Inheritance.
    
              A ---m1()
            *   *
          *       *
  m1()---B         C---m1()
          *       *
            *   *
              D---m1()

In the above structure we can understand that from where the m1 method can access.
1. First from D it takes.
2. In D not present it checks B and C Based on priority.
3. If not present in B and C then it checks A then object. (Here what is object).

Every class is a child of the built in object class, either directly or indirectly.
If we create a class without specifying any parent class, it automatically inherits from object.
'''
