with open("initialdata.txt", encoding='utf-8') as f:
    data = f.read()
chunks = data.split("\n\n")
def parse_chunk(chunk): 
        chunk = chunk.strip()
        sep_chunk = chunk.split('\n')
        username = sep_chunk[0]
        no_of_posts = int(sep_chunk[1].split(" post")[0].replace(",", ""))
        no_of_followers = float(sep_chunk[2].split(" follower")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in sep_chunk[2]):
            no_of_followers = int(no_of_followers * 1000)
        elif("M" in sep_chunk[2]):
            no_of_followers = int(no_of_followers * 1000000)
        else:
            no_of_followers = int(no_of_followers)
             

    
        no_of_following = float(sep_chunk[3].split(" following")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in sep_chunk[3]):
            no_of_following = int(no_of_following * 1000)
        elif("M" in sep_chunk[3]):
            no_of_following = int(no_of_following * 1000000)
        else:
            no_of_following = int(no_of_following)

            
        name = sep_chunk[4]
        if(len(sep_chunk)> 5):
            type_of_page = sep_chunk[5]
            bio = "\n".join(sep_chunk[6:])
        else:
            type_of_page = "Unknown"
            bio = ""
        # print(username, no_of_posts, no_of_followers, no_of_following, name, type_of_page, bio, sep="\n")
        return {"username": username, "no_of_posts": no_of_posts, "no_of_followers": no_of_followers, 
                "no_of_following": no_of_following, "name": name, "type_of_page": type_of_page, "bio": bio}

all_chunks = [] 
for chunk in chunks:  
    if chunk.strip():
        parsed_chunk = parse_chunk(chunk)
        all_chunks.append(parsed_chunk)
import json
json.dump(all_chunks, open("clean_data.json","w"),indent=4)   
max = 0

#chunk with max post
print("chunk with max post\n")
for chunk in all_chunks:
    if(max<chunk['no_of_posts']):
        max = chunk['no_of_posts']
        chunk_with_max_post = chunk
print(chunk_with_max_post)
max=0
#chunk with max followers
print("\nchunk with max following\n")
for chunk in all_chunks:
    if(max<chunk['no_of_following']):
        max = chunk['no_of_following']
        chunk_with_max_following = chunk
print(chunk_with_max_following)
#chunk with max followers
max=0
print("\nchunk with maxfollowers\n")
for chunk in all_chunks:
    if(max<chunk['no_of_followers']):
        max = chunk['no_of_followers']
        chunk_with_max_followers = chunk
print(chunk_with_max_followers)
categories = set()
for chunk in all_chunks:
    categories.add(chunk['type_of_page'])
print(categories, len(categories))
