Reddit Project: 
=================================

reddit.com has an easy way to get their feeds via JSON.

http://www.reddit.com/hot.json
http://www.reddit.com/top.json

You will not need any API integration or Oauth.

Users should be able to create an account with a username and password. 

Once they have an account users will go to a page and view reddit posts and be able to favorite links/posts they like.

Use these JSON endpoints to create a simple Reddit reader with lists Hot or Top. You do not have to support pagination (but bonus points if you do).

Just print out the links, titles, number of comments, and embed information if applicable (e.g. images, videos). The design doesn't have to be beautiful so don't worry much about the design.

We also want the ability to favorite (e.g. star, like) any post. This is different than Reddit's standard up/down vote. You will store this data on your own datastore as we're not integrating with Reddit directly.

You should allow the user the ability to then view all of the posts they liked on a separate page. 

You will then need to host this solution somewhere online so that we can see it in action. 

We'd also like you to share your source code via Github or Bitbucket. 

My github username is courtstarr and if you can share privately (but not required).

You can use any language and datastore that you want and host this wherever you'd like.

Database Project: 
=================================

Goal is to keep track of people who have multiple addresses and multiple phone numbers

Please create a relational database schema that would work for this.

Show an example of the following queries:

- Display people and their phone numbers
- Display people and their addresses
- Display people and their addresses only if they are in the state of California
- Show how many people have addresses in each state
- Show the % of people that have multiple addresses

You do not have to create the database specifically but just show the schema and SQL from standard relational SQL databases like mysql or psql.
