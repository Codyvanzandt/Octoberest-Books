---
title: "The Octoberest Books: a Cultural Analytics Bottle Project"
slug: "The-Octoberest-books"
categories: 
- cultural-analytics
- python
date: 2021-10-05
---

## In Search of Spooky Time

For the last few Octobers, my inner tech geek and inner October fanatic have been desperate to collaborate on a spooky data science project.
It's a competitive field, though! There's Janelle Shane's always-excellent neural-net-generated [Halloween costumes](https://www.aiweirdness.com/halloween-costumes-by-the-neural-19-10-14/)
and [tasty(ish) treats](https://www.aiweirdness.com/easy-halloween-treats-generated-by-19-10-31/). There's 538's silly-and-sporty [Candy Power Ranking](https://fivethirtyeight.com/videos/the-ultimate-halloween-candy-power-ranking/).
And of course, there are the veteran spooky statisticians of the National Retail Federation, who've been running an annual [Halloween Trends Report](https://nrf.com/topics/holiday-and-seasonal-trends/halloween) for some years now.

As for my own entry into this amusingly large body of Halloween hackery, I've decided to stick to my literary roots and launch what I'm calling a cultural analytics "bottle project" (*a la* television's [bottle episodes](https://en.wikipedia.org/wiki/Bottle_episode)) --
a short-and-sweet single-method, single-dataset, single-day investigation into a simple question: which fantasy books are the "Octoberest." The great hope of the project, of course, is that the "Octoberest" books are also the spookiest, most-Halloweenest books!

## Computing Octoberness

Here's the idea: I've taken [UCSD's dataset of Goodreads reviews for fantasy books](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home) and calculated for each book how many reviews it receives in October vs. how many it receives in the non-October months.
After making the arbitrary-ish decision to divide the number of non-October reviews by 11 (to account for the fact that there are 11-times as many non-October months!), 
I'm left with my "Octoberness" score, which measures how evenly distributed a book's reviews are between October and the average non-October month.

An Octoberness score of 1, for example, means that a book receives a equal number of reviews in October as it does in an average non-October month.
A score of 2 means that a book receives twice as many reviews in October compared to an average non-October month.
And a score of 0.5 means it receives half as many reviews in October compared to an average non-October month.

After unscrupulously tossing out books with too few reviews<sup>[1](#myfootnote1)</sup> to yield a meaningful Octoberness score, I sorted by Octoberness and collected the top "most-Octoberest" books in a handy little list. I am excessively proud to report that the result speak -- or really, *shriek* -- for themselves. I've detailed top 5 below with clickable book covers that whisk you away to Goodreads.com. The extra-curious reader can find the top 150 on this project's [little Github page.](https://github.com/Codyvanzandt/Octoberest-Books)

## The Most Octoberest Books

# 1. *Book Title* by Author, XX Octoberness

[![name](link-to-image)](link-to-good-reads)

> Block quote containing summary

# 2. *Book Title* by Author, XX Octoberness

[![name](link-to-image)](link-to-good-reads)

> Block quote containing summary

# 3. *Book Title* by Author, XX Octoberness

[![name](link-to-image)](link-to-good-reads)

> Block quote containing summary

# 4. *Book Title* by Author, XX Octoberness

[![name](link-to-image)](link-to-good-reads)

> Block quote containing summary

# 5. *Book Title* by Author, XX Octoberness

[![name](link-to-image)](link-to-good-reads)

> Block quote containing summary


## Celebrations and Limitations

It's always such a joy to see a simple method yield compelling results! The full list is jam-packed with magic, mystery, and all manner of Things That Go Bump in the Night. The top Octoberness-getter, Neil Gaiman's tiny scary story "Click Clack the Rattle Bag," is especially lovely and completely new to me. If you can spare 10 minutes, you really must to listen to [Gaimain's New York Public Library reading of the story](https://www.youtube.com/watch?v=imLja6Emezo). It's quite the October mood-setter!

Of course, this little bottle project is (by design!) full of omissions, missed-opportunities, ignored-problems, and more besides I'm sure. 

<a name="footnote1">1</a>: Some quick and drity exploratory analysis suggested that 100 total reviews was a reasonable cutoff
