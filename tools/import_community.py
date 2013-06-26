import sys
import os

#This take a file generated by community_finder.py as input

communities = open(sys.argv[1],'r');
community = None;

for i in communities:

    i = i.strip();

    if i == '':
        community = None;
        continue;
    elif community == None:
        print('Start with community for'+i);
        community = 'input/community_'+i;
        os.mkdir(community);

    f = open('/scratch/wstoop/tweetdata/feeds/'+i);
    tweets = [];
    for j in f:
        try:
            tweets.append(j.split('||')[2]);
        except IndexError:
            print('Skipped one');

    open(community+'/'+i,'w').write(''.join(tweets));