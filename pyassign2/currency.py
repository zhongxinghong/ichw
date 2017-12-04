from urllib.request import urlopen


'''working part'''

def Url(cfrom, cto, afrom):
    '''generate URL'''
    
    url1 = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    url2 = 'from=' + cfrom.upper() + '&to=' + cto.upper() + '&amt=' + afrom
    url = url1 + url2
    return url

def count(url):
    '''exchange by http://cs1110.cs.cornell.edu/2016fa/a1server.php? '''
    
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def amountto(result):
    '''separate the exchange amount'''
    
    xi = result.find('"to"')
    i = xi + 8
    while result[i] != ' ' :
        i += 1
    amount_to = float(result[xi + 8 : i])
    return amount_to
    
def exchange(currency_from, currency_to, amount_from):
    '''Returns: amount of currency received in the given exchange.'''
    
    url = Url(currency_from, currency_to, amount_from)
    result = count(url)
    amount_to = amountto(result)
    return amount_to

def main():
    currency_from = input()
    currency_to = input()
    amount_from = input()
    amount_to = exchange(currency_from, currency_to, amount_from)
    print(amount_to)

    
'''test part'''
    
def test_Url():
    '''test the 'Url' function'''
    assert(Url('USD', 'EUR', '2.5') == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    
def test_count():
    '''test the 'test_count' function'''
    assert(count('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5') == '{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')
    
def test_amountto():
    '''test the 'test_amountto' function'''
    assert(amountto('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }') == 2.0952375)    

def test_exchange():
    '''test the 'test_exchange' function'''
    assert(exchange('USD', 'EUR', '2.5') == 2.0952375)
    
def testAll():
    """test all cases"""
    test_Url()
    test_count()
    test_amountto()
    test_exchange()
    print("All tests passed")
    

if __name__ == '__main__':
    main()
