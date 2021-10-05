---
title: "The Octoberest Books: a Cultural Analytics Bottle Project"
slug: "The-Octoberest-books"
categories: 
- cultural-analytics
- python
date: 2021-10-05
---

For the last few Octobers, my inner tech geek and inner October fanatic have been desperate to collaborate on a spooky data science project.
It's a competitive field, though! There's Janelle Shane's always-excellent neural-net-generated [Halloween costumes](https://www.aiweirdness.com/halloween-costumes-by-the-neural-19-10-14/)
and [tasty(ish) treats](https://www.aiweirdness.com/easy-halloween-treats-generated-by-19-10-31/). There's 538's silly-and-sporty [Candy Power Ranking](https://fivethirtyeight.com/videos/the-ultimate-halloween-candy-power-ranking/).
And of course, there are the veteran spooky statisticians of the National Retail Federation, who've been running an annual [Halloween Trends Report](https://nrf.com/topics/holiday-and-seasonal-trends/halloween) for some years now.

As for my own entry into this amusingly large body of Halloween hackery, I've decided to stick to my literary roots and launch what I'm calling a cultural analytics "bottle project" (*a la* television's [bottle episodes](https://en.wikipedia.org/wiki/Bottle_episode)) --
a short-and-sweet single-method, single-dataset, single-day investigation into which fantasy books are the "Octoberest." The great hope of the project, of course, is that the "Octoberest" books are also the spookiest, most-Halloweenest books!

Here's the idea: I've taken [UCSD's dataset of Goodreads reviews for fantasy books](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home) and calculated for each book how many reviews it receives in October vs. how many it receives in the non-October months.
After making the arbitrary-ish decision to divide the number of non-October reviews by 11 (to account for the fact that there are 11-times as many non-October months!), 
I'm left with my "Octoberness" score, which measures how evenly distributed a book's reviews are across the October and non-October months.

An Octoberness score of 1, for example, means that a book receives a equal number of reviews in October as it does in an average non-October month.
A score of 2 means that a book receives twice as many reviews in October compared to an average non-October month.
And a score of 0.5 means it receives half as many reviews in October compared to an average non-October month.

After unscrupulously tossing out books with too few reviews<sup>[1](#myfootnote1)</sup> to comupute a meaningful Octoberness score, I sorted the books in by their Octoberness and collected the top 150 "most-Octoberest" books in a handy little list.
The results -- which I'm disproportionately proud to share -- are so satisfyingly spooky:






<a name="footnote1">1</a>: Some quick and drity exploratory analysis suggested that 100 total reviews was a reasonable cutoff
