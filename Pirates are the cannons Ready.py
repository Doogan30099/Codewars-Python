def cannons_ready(gunners):
    answers = gunners.values()
    if all(answer == "aye" for answer in answers):
        return "Fire!"
    else: 
        return "Shiver me timbers!"
  