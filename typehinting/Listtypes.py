from typing import List, Dict, Union


x : List[List[int]] = []


y : Dict[str, str] = {"a":"b"}   #for strings 

b : Dict[str, Union[str, int]] = {"a": "b", "b": 3, "c":"d", "e":4 }



for i in b :
    print(b[i])