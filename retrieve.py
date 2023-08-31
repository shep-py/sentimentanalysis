import praw
from praw.models import MoreComments
reddit = praw.Reddit(client_id='CLIENT ID',
                     client_secret='SECRET', password='PASSWORD',
                     user_agent='APP NAME', username='USERNAME')
def Post_List(sub,feature):
  post_id_list = []
  subr = reddit.subreddit(sub)
  for i in subr.search(feature, limit=20):
     post_id_list.append(i)
  return post_id_list
def Comment_List(post_id_list):
    comment_list=[]
    for i in range(0, len(post_id_list)):
       submission=reddit.submission(post_id_list[i])
       submission.comments.replace_more(limit=None)
       comments = submission.comments.list()
       for com in comments:
           comment_list.append(com.body)
    return comment_list
