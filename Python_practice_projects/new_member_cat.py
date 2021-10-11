def open_or_senior(data):
    output_list = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output_list.append("Senior")
        else:
            output_list.append("Open")
          
            
   
    print(output_list)
open_or_senior([(43, 2), (11, 14), (44, 13), (11, 26), (29, 22), (85, -1), (26, 21)])