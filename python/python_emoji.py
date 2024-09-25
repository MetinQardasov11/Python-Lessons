from emoji import emojize, is_emoji, demojize

text = 'Python is :thumbs_up:'
print(emojize(text))

emoji = '👍'
print(is_emoji(emoji))

# ---------------------------------------------------------------------------------------------------------------------------------------

text = 'Python is 👍'
print(demojize(text))

# ---------------------------------------------------------------------------------------------------------------------------------------

text = 'Please subscribe :grinning_face:'
print(emojize(text))