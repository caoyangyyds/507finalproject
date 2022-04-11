from tree import BSTNode
import json

cache_file = open("song_dict.json", 'r')
cache_file_contents = cache_file.read()
cache = json.loads(cache_file_contents)
cache_file.close()
tree_singer = BSTNode()
for i in range(len(cache)):
    tree_singer.insert(cache[i], i)


def main():
    print("Hello, can I help you?")
    while True:
        print("Here are 100 singers in billboard 2021, please give a rank of a singer you want to see.")
        print("Surprise! You can see more than one singer if you give a range. Please enter like: 20 30." )
        num = input()
        if len(num) == 1:
            ll_singer = [tree_singer.find(int(num) - 1)]
            list_singer = [ll_singer['name']]
        else:
            nm_split = num.split('')
            ll_singer = []
            list_singer = []
            for e in range(int(nm_split[0])-1, int(nm_split[1])-1):
                ll_singer.append(tree_singer.find(e))
                list_singer.append(tree_singer.find(e)['name'])
        
        ###flask
        
        print("Please see the result in the host page!")

        aws = input('Please input the number of the singer to get his/her/their details')
        if int(aws) > len(ll_singer):
            print("You are out of list.")
        else:
            keyname = ll_singer.find(int(aws)-1)['songs'][0].keys()
            valuefirst = ll_singer.find(int(aws)-1)['songs'][0].values()
            dance_list = []
            energy_list = []
            tempo_list = []
            for val in valuefirst:
                dance_list.append(val["danceability"])
                energy_list.append(val["energy"])
                tempo_list.append(val["tempo"])
        ###flask
            
        print("The information has been mentioned in the website.")
        print("Do you want to play again?")
        ans = input()
        if ans == 'no':
            print('bye!')
            return

if __name__ == '__main__':
    main()

                

        