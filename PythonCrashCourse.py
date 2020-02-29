# In[2]:


my_list = ['a', 'b', 4, True]


# In[3]:


my_list[3]


# In[4]:


my_list[3] = False


# In[7]:


my_list = [1,2,3,'a', True]


# In[8]:


print(my_list)


# In[9]:


dictionary = { 1 : 'Alex',
            2 : 'Kobi',
            3 : 'Helly',
            4 : 'Mike'}


# In[13]:


print(dictionary[1])
print(dictionary[4])


# In[14]:


dic = {'dog_names': {1: 'max',
                    2: 'humus'},
      'human_names' : {1: 'Mike',
                      2: 'Alex'}}


# In[17]:


print(dic['dog_names'][1])
print(dic['human_names'][2])


# In[19]:


t = (1,2,3,4,5,"Alex") #List that cannot be mutated


# In[23]:


s = {1,1,1,1,1,2,2,3,3,3,3,4,5,6} #List that cannot have duplicates (removes them automatically)
print(s)


# conditions:

# In[24]:


if ((1+2) == 3) and ((1-1) == -1):
    print("egarg")
elif (1+1 ==2) or (1-1 == -1):
    print("aegag")
else:
    print("afaef")


# Loops (for & while)

# In[30]:


seq = [1,2,3,4,5,True,False,"Alex", True, "Kobi"]
for item in seq:
    print(item)


# In[33]:


seq = [1,2,3,4,5,True,False,"Alex", True, "Kobi"]
i = 0
while seq[i] < 4:
    print(seq[i])
    i = i+1


# In[35]:


li = [2,3,6,5,8,7,4]       #List comprihension. 
[num**3 for num in li]     #creating a new list with every number from li powered by 3


# FUNCTION

# In[41]:


def my_func(name='Hillary'):
    print("Hello " +name)
my_func('Alex')


# In[46]:


def squre(num1, num2):
    number = num1**num2
    if(number%2 == 0):
        print(str(number)+ " is even!")
    else:
        print(str(number) + " is not even!")
squre(23,5)


# Lambda Expression and Mapping

# In[49]:


li = [1,2,3,4,5,6,7]                 #instead of def a function. you use a lambda expression (also known as Annonymous Function)
print(list(map(lambda num: num**3, li)))    #which allows you to write a function in 1 line


# In[71]:


tweet = """
Work from home? 
Stay safe with our complimentary remote security!
#checkpoint #vpn #mobilesecurity #endpointsecurity #workfromhome
"""
tweet.split()
tweet_word_list = list(map(lambda word: '#' in word ,tweet.split()))
tweet_word_list







