Lists are mutable and not hashable. When we change a list , in memory the same object is changed.This is why during recursion with list we do result.append(value.copy()) , otherwise when during recursion call backs the value changes, value in result also keeps changing. 

Set , string ,tuple they are hashable. when we change these , the earlier memory doesn't change ,a new memory location is made with new value .  

So in a set only hashable types can be added . 