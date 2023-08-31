import retrieval
import comment_processing
sentiment_list=[]
d=0
neg_sum=0
pos_sum=0
neu_sum=0
neg_avg=0
neu_avg=0
pos_avg=0
subreddit=input("enter the subreddit to search:")
feature=input("enter the feature to search:")
post_list=retrieval.Post_List(subreddit,feature)
comment_list=retrieval.Comment_List(post_list)
for i in comment_list:
    sentiment_list.append(comment_processing.vader_analyse(i))
for i in range(0,len(sentiment_list)):
    neg_sum=neg_sum+sentiment_list[i][0]
    neu_sum=neu_sum+sentiment_list[i][1]
    pos_sum=pos_sum+sentiment_list[i][2]
neg_avg=neg_sum/len(sentiment_list)
neu_avg=neu_sum/len(sentiment_list)
pos_avg=pos_sum/len(sentiment_list)
print(neg_avg)
print(neu_avg)
print(pos_avg)
