import json
import facebook

def main():
	token = "EAAGdZB8LwJzwBADBX71ZCBOmvpWCjYifZAQzZC3GwSq5R5UvTy9sbSwKg3rHVbGyh5FGWCkX4jIRxRn8vZBZBrVNHo77XGdstNsQhdWw3r5YOBjyAatEz7cX0LFFgpF2FGPKVFLzmSsJhZA3W3RZBjlLUw4PvHMAmhFJnkCn8zShQQZDZD"
	graph = facebook.GraphAPI(token)
	#fields = ['first_name', 'location{location}','email','link']
	profile = graph.get_object('me',fields='first_name,last_name,birthday,hometown,age_range,gender,location{location},email,likes,posts,photos,friends')	
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()