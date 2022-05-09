#!/usr/bin/env python3  

depthNode = 0

if __name__ == "__main__":
    while depthNode == 0:
        print ("Welcome to node 0 this is begin")
        node = input("Choose node\n")
    #------------------------------------ node 1 ----------------------------------------#
        if node in {'1','node1'}:
            depthNode = depthNode + 1
            while depthNode == 1:
                print ("Welcome to node 1")
                node = input("Choose node\n")
    #------------------------------------ node 1-1 ----------------------------------------#           
                if node in {'1','1-1','node1-1','restart'}:
                    print ('Welcome to node 1-1')
                    depthNode = 0
                    print ('Now you will back to begin')
    #------------------------------------ node 1-2 ----------------------------------------#
                elif node in {'2','1-2','node1-2','back'}:
                    print ('Welcome to node 1-2')
                    depthNode = depthNode-1
                    print ('Now you will back to one step before')
                else:
                    print ('Plz choose node i have')
                    depthNode = depthNode-1

    #------------------------------------ node 2 ----------------------------------------#

        elif node in {'2','node2'}:
            depthNode = depthNode + 1
            while depthNode == 1:
                print ("Welcome to node 2")
                node = input("Choose node\n")
    #------------------------------------ node 2-1 ----------------------------------------#
                if node in {'1','2-1','node2-1','go to deepnode'}:
                    depthNode = depthNode + 1
                    while depthNode == 2:
                        print ("Welcome to node 2-1")
                        node = input("Choose node\n")
    #------------------------------------ node 2-1-1 ----------------------------------------#
                        if node in {'1','2-1-1','node2-1-1'}:
                            print ('Welcome to node 2-1-1')
                            depthNode = int(input("Choose depth_node you need\n"))
                            print ('Now you will back to that node')
    #------------------------------------ node 2-1-2 ----------------------------------------#
                        elif node in {'2','2-1-2','node2-1-2'}:
                            print ('Welcome to node 2-1-2')
                            print ('Now exit')
                            exit() #Can instead of function you need to do
                        else:
                            print ('Plz choose node i have')
                else:
                    print ('Plz choose node i have')
                    depthNode = depthNode-1
    #------------------------------------ no node ----------------------------------------#
        else:
            print ('Plz choose node i have')