# StolenLaptop
I wrote a script that will take the picture of the thief, record the external IP and send it in an email to me. It checks every two minutes for a website I put up, if I see that it has been stolen. It requires python, some extra py packages, and a gmail account.
You can get it at my github. Unzip to whereever, customize the stuff at the top in theft.py, and put it in your cron (example below).
*/2 * * * * /Users/username/Documents/theft/theft.py
