import optparse
def merge(items1, items2):
    items3 = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if items1[index1] < items2[index2]:
            items3.append(items1[index1])
            index1 += 1
        else:
            items3.append(items2[index2])
            index2 += 1
    return items3
print(__name__)
print( __name__ == '__main__')
if __name__ == "__main__":
    print('start:')
    print(merge([1,2,3,6], [2,4,8]))
    usage="[-m  md5 decryption]"
    parser=optparse.OptionParser(usage)
    parser.add_option('-m',dest='md5',help='md5 decryption')
    (options,args)=parser.parse_args()
    print(options)
    print("args:%s"%args)