def get_outfit(answer1, answer2, answer3):
  if(answer1 == "1"):
    if(answer2 == "1"):
      if(answer3 == "1"):
        return "111"
      else:
        return "112"
    else:
      if(answer3 == "1"):
        return "121"
      else: 
        return "122"
  else:
    if(answer2 == "1"):
      if(answer3 == "1"):
        return "211"
      else:
        return "212"
    else:
      if(answer3 == "1"):
        return "221"
      else:
        return "222"