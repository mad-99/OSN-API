import json
import facebook

def main():
	token = "____________________________________secret_key________________________________________________"
	graph = facebook.GraphAPI(token)
	#fields = ['first_name', 'location{location}','email','link']
	profile = graph.get_object('me',fields='first_name,last_name,birthday,hometown,age_range,gender,location{location},email,likes,posts,photos,friends')	
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()
