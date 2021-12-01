import argparse

def BANNER():
    print(r"""
                                                                      
                ,----..            ,--.                           
  .--.--.      /   /   \         ,--.'|   ,---,       ,-.----.    
 /  /    '.   /   .     :    ,--,:  : |  '  .' \      \    /  \   
|  :  /`. /  .   /   ;.  \,`--.'`|  ' : /  ;    '.    ;   :    \  
;  |  |--`  .   ;   /  ` ;|   :  :  | |:  :       \   |   | .\ :  
|  :  ;_    ;   |  ; \ ; |:   |   \ | ::  |   /\   \  .   : |: |  
 \  \    `. |   :  | ; | '|   : '  '; ||  :  ' ;.   : |   |  \ :  
  `----.   \.   |  ' ' ' :'   ' ;.    ;|  |  ;/  \   \|   : .  /  
  __ \  \  |'   ;  \; /  ||   | | \   |'  :  | \  \ ,';   | |  \  
 /  /`--'  / \   \  ',  / '   : |  ; .'|  |  '  '--'  |   | ;\  \ 
'--'.     /   ;   :    /  |   | '`--'  |  :  :        :   ' | \.' 
  `--'---'     \   \ .'   '   : |      |  | ,'        :   : :-'   
                `---`     ;   |.'      `--''          |   |.'     
                          '---'                       `---'       
                                                                  
                                                                  
    """)

def main():
    parser = argparse.ArgumentParser(description='A simple command line tool created to solve the Advent of Code - Challenge 1.')
    parser.add_argument('file', metavar='<filepath>', type=str,
                        help='file containing data to be sorted')
    args = parser.parse_args()

    def sonar(file):
        list_cur = []
        with open(file, 'r') as f:
            list_num = [i.strip() for i in f]
        for i,x in enumerate(list_num):
            pre = int(list_num[i-1])
            cur = int(list_num[i])
            if i == 0:
                pass
            if cur - pre > 0:
                print(str(cur), " :Increase")
                list_cur.append(cur)
            else:
                print(str(cur), " :Decrease")
        x = len(list_cur)
        print("Number of Increases: ", x)

    if args.file:
        sonar(args.file)

if __name__=='__main__':
    BANNER()
    main()
