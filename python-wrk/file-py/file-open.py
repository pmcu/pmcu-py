with  open('am-tae.jpg','rb') as rf:
    with  open('am-tae-copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



        # for line in rf:
        #     wf.write(line)








    # with  open('test_copy.txt','w') as wf:
    #     for line in rf:
    #         wf.write(line)





    # pass
    # f.write('Test\n')
    # f.write('Test\n')







    # size_to_read = 10
    #
    # f_contents = f.read(size_to_read)
    # print(f_contents, end = '')

    # f.seek(0)
    #
    # f_contents = f.read(size_to_read)
    # print(f_contents)




    # while len(f_contents) > 0:
    #     print(f_contents, end = '*')
    #     f_contents = f.read(size_to_read)



    # for line in f:
    #     print(line, end='')











# f=open('test.txt','r')
# print(f.name)
#
# f.close()
# f_contents = f.readline()
# print(f_contents, end='')
#
# f_contents = f.readline()
# print(f_contents, end='')
