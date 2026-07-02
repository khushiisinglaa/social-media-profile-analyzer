with open("initialdata.txt", encoding='utf-8') as f:
    data = f.read()
chunks = data.split("\n\n")
def parse_chunk(chunk): 
    try:
            chunk = chunk.strip()
            sep_chunk = chunk.split('\n')
            username = sep_chunk[0]
            no_of_posts = sep_chunk[1]
            no_of_followers = sep_chunk[2]
            no_of_following = sep_chunk[3]
            name = sep_chunk[4]
            if(len(sep_chunk)> 5):
                 type_of_page = sep_chunk[5]
                 bio = "\n".join(sep_chunk[6:])
            else:
                 type_of_page = "Unknown"
                 bio = ""
            return {"username": username, "no_of_posts": no_of_posts, "no_of_followers": no_of_followers, 
                "no_of_following": no_of_following, "name": name, "type_of_page": type_of_page, "bio": bio}
    except Exception as e:
         return [e,chunk] 
all_chunks=[]            
for chunk in chunks:  
    if chunk.strip():
        parsed_chunk = parse_chunk(chunk)
        all_chunks.append(parsed_chunk)
for i, chunk in enumerate(all_chunks):
     print(f"{i+1},{chunk}\n")

