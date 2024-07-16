
hashtags=list(range(6))
def create_youtube_video (title,description):
	for w in range(5):
		hashtag=input("Enter a hashtag")
		hashtags.append(hashtag)
	youtubevideo={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}, "hashtags":hashtags}
	
	return youtubevideo
def add_like (youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"]+=1
	return youtubevideo
def add_dislike (youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"]+=1
	return youtubevideo
def add_commment (youtubevideo,username,commenttext):
	if "comments" in youtubevideo:
		youtubevideo["comments"][username]=commenttext

newvideo=create_youtube_video("Hasan the great","Hasan beats up Sari Khamis")
for i in range(495):
	updated_dictionary=add_like(newvideo)

new_d=add_commment(newvideo,"Sari","I AM MAD")

print(updated_dictionary)
lill=create_youtube_video("HASAN THE GREAT#2","Hasan beating up Lill")
lill_like=add_like(lill)
lilldis=add_dislike(lill)
lillcom=add_commment(lill,"lill","I AM GOING TO GIVE YOU GOOD AT CS!")
counter=0
def similarity_videos(newvideo,lill):

	if lill["likes"]==newvideo["likes"]
		counter+=1