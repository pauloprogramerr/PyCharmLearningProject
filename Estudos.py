from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username = 'logins',password = 'senha')


with smart_run(session):
	session.set_do_follow(enable = True, percentage = 100)
	session.set_do_like(enable = True, percentage = 100)

	#session.like_by_tags([''], amount=5)
	#session.like_by_feed(amount = 5, randomize = True, unfollow = True, interact = True)
	#session.like_by_location(['Localização'], amount = 5)
	#session.follow_user_followers(['isetups'], amount = 5, randomize = False)
	#session.follow_user_following(['isetups'], amount = 5, randomize = False)
	#session.follow_likers(['isetups'], photos_grab_amount = 1, follow_likers_per_photo = 2, 
	#						randomizd = True, sleep_delay = 600, interact = True)
	session.followecommenters(['isetups'], amount = 5, daysold = 365, max_pic = 100, sleep_delay = 600, interact = False)
	session.unfollow_user(amount = 2, allFollowing = True, style = "FIFO", unfollow_affter= 3*60*60, sleep_delay = 450)
	session.unfollow_user(amount = 2, nonFollowing = True, style = "FIFO", unfollow_affter= 3*60*60, sleep_delay = 450)

	comentarios ['Nice shot!', 'love yours posts']
	session.set_do_comments(enable = True, percentage = 95)
	session.set_comments(comentarios, media = 'Photo')
	session.join_pods()


































