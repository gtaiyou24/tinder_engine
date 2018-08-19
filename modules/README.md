# Tinder API Documentation -- 2017

First off, I want to give a shoutout to <a href='https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md'>@rtt</a> who initially posted the Tinder API Documentation that I found most of these endpoints on. I am writing this to provide a more up-to-date resource for working with the Tinder API.

**Note: This was updated in March 2017. API might be outdated.**

**Note: As of March 30, 2017, Tinder has set their ping_time attribute to a constant and is not updated any more. Therefore, it is no longer possible (to my knowledge) to see when users were last active.**

### API Details
<table>
	<tbody>
		<tr>
			<td>Host</td>
			<td>api.gotinder.com</td>
		</tr>
		<tr>
			<td>Protocol</td>
			<td>SSL</td>
		</tr>
	</tbody>
</table>

### Required Headers
<table>
	<thead>
		<tr>
			<th>Header</th>
			<th>Example</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>X-Auth-Token</td>
			<td>See "How to get facebook_token" below</td>
		</tr>
		<tr>
			<td>Content-type</td>
			<td>application/json</td>
		</tr>
		<tr>
			<td>User-agent</td>
			<td>Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)</td>
		</tr>
	</tbody>
</table>

### Known Endpoints
Note: All endpoints are concatenated to the host url

Note: All curls must be sent with the headers as well (the only exception is that the /auth call must not have the X-Auth-Token header)
<table>
	<thead>
		<tr>
			<th>Endpoint</th>
			<th>Purpose</th>
			<th>Data?</th>
			<th>Method</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>/auth</td>
			<td>For authenticating</td>
			<td>{'facebook_token': INSERT_HERE, 'facebook_id': INSERT_HERE}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/user/recs</td>
			<td>Get match recommendations</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/user/matches/_id</td>
			<td>Send Message to that id</td>
			<td>{"message": TEXT GOES HERE}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/user/_id</td>
			<td>Get a user's profile data</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/user/ping</td>
			<td>Change your location</td>
			<td>{"lat": lat, "lon": lon}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/updates</td>
			<td>Get all updates since the given date -- inserting "" will give you all updates since creating a Tinder account (i.e. matches, messages sent, etc.)</td>
			<td>{"last_activity_date": ""} Input a timestamp: '2017-03-25T20:58:00.404Z' for updates since that time.</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/profile</td>
			<td>Get your own profile data</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/profile</td>
			<td>Change your search preferences</td>
			<td>{"age_filter_min": age_filter_min,
				"gender_filter": gender_filter,
				"gender": gender,
				"age_filter_max": age_filter_max,
				"distance_filter": distance_filter}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/meta</td>
			<td>Get your own meta data (swipes left, people seen, etc..)</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/report/_id</td>
			<td>Report someone --> There are only a few accepted causes...</td>
			<td>{"cause": CAUSE}</td>
			<td>POST</td>
		</tr>
		<tr>
			<td>/like/_id</td>
			<td>Like someone a.k.a swipe right</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/pass/_id</td>
			<td>Pass on someone a.k.a swipe left</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/like/_id/super</td>
			<td>~Super Like~ someone a.k.a swipe up</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/group/{like|pass}/_id</td>
			<td>Like or Pass on a group</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/matches/{match id}</td>
			<td>Get a match from its id (thanks <a href='https://github.com/jtabet'> @jtabet </a>)</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
		<tr>
			<td>/message/{message id}</td>
      <td>Get a message from its id (thanks <a href='https://github.com/jtabet'> @jtabet </a>)</td>
			<td>{}</td>
			<td>GET</td>
		</tr>
	</tbody>
</table>

### Status Codes
<table>
	<thead>
		<tr>
			<th>Status Code</th>
			<th>Explanation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>200</td>
			<td></td>
		</tr>
		<tr>
			<td>400</td>
			<td></td>
		</tr>
		<tr>
			<td>501</td>
			<td></td>
		</tr>
	</tbody>
</table>

### Dependencies:
<ul>
	<li> <a href="https://docs.python.org/3/library/datetime.html"> datetime </a> </li>
	<li> <a href="https://github.com/kennethreitz/requests"> requests </a> </li>
	<li> <a href="https://docs.python.org/3.5/library/json.html"> json </a> </li>
	<li> <a href="https://docs.python.org/2/library/re.html"> re </a> </li>
	<li> <a href="https://github.com/jmcarp/robobrowser"> robobrowser </a> </li>
</ul>

### Config File
<h5> <strong> facebook_access_token and fb_user_id </strong></h5>

Simply input your facebook username/email and password in your config file. Then, the fb_auth_token.py module will programmatically retrieve your facebook_access_token and fb_user_id. These are then used to generate your tinder_auth_token in tinder_api.py which grants you access to your data! Happy Swiping!
<br>


<strong> Note: </strong> With the help of <a href=https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py> philliperemy </a>, I have included a programatic way to acquire your facebook_token. Now, in your config.py just input your facebook username and password.

<h2> features.py Key Features </h2>

<h3> Match_Info:</h3>
<h4> Creates a local dictionary containing the following keys on each of your matches </h4>

```javascript
{
	  123456: {
	    'messages': [

	    ],
	    'age': 20,
	    'match_id': '123456789123456789',
	    'name': 'Joakim',
	    'photos': [
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg'
	    ],
	    'message_count': 0,
	    'last_activity_date': '15 days, 16 hrs 46 min 57 sec',
	    'ping_time': '2017-03-11T04:58:56.433Z',
	    'gender': 1,
	    'bio': 'New York Knicks Center',
	    'avg_successRate': 0
	  },
	  56789: {
	    ...
	  }
}
```

<h3> Sorting: </h3>
<h4> Sorting matches by "age", "message_count", "successRate", and "gender" </h4>
<h5> sort_by_successRate() will return the following object: </h5>

```javascript
[
	  ('123456789123456789',
	  {
	    'messages': [

	    ],
	    'age': 19,
	    'match_id': '123456789123456789abcdefghi',
	    'name': 'Carmelo',
	    'photos': [
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg',
	      'http://images.gotinder.com/123456789123456789.jpg'
	    ],
	    'message_count': 0,
	    'last_activity_date': '0 days, 22 hrs 23 min 45 sec',
	    'ping_time': '2017-03-25T23:22:08.954Z',
	    'gender': 1,
	    'bio': 'I do not like to win sometimes', 'avg_successRate': 0.7837966008217391
	    }
	    )
]
```
<h3> Facebook Friends: </h3>
<h4> Given a name, it returns some profile information and their id. Once you have the ID, then you can call api.get_person(id) to get more in-depth information on your friends. </h4>


```javascript

{
	  'Martin Shkreli': {
	    'photo': [
	      {
	        'processedFiles': [
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=84&width=84',
	            'height': 84,
	            'width': 84
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=172&width=172',
	            'height': 172,
	            'width': 172
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=320&width=320',
	            'height': 320,
	            'width': 320
	          },
	          {
	            'url': 'https://graph.facebook.com/123456789/picture?height=640&width=640',
	            'height': 640,
	            'width': 640
	          }
	        ]
	      }
	    ],
	    'in_squad': True,
	    'name': 'Martin Shkreli',
	    'user_id': '582bf320452u3yy1217f8'
	  }
}
```


<h2> The following is no longer available due to Tinder setting their ping_time to a constant date in 2014.</h2>
```

<h3> Friends' Pingtimes: </h3>
<h4> friends_pingtimes() will return the following for each facebook friend of yours who has a Tinder
friend_pingtime_by_name("Joakim Noah") will return the pingtime for only that particular friend.
The following is a sample result for friends_pingtimes(): </h4>

`
	"Joakim Noah -----> 15 days, 16 hrs 46 min 57 sec"
	"Carmelo Anthony ------> 0 days, 22 hrs 23 min 45 sec"
	...
`
