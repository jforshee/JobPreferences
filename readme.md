Job Preferences
===============

Purpose
-------

Given a preference mapping of individuals for a set of jobs, we want to assign jobs based on those preferences to each person. As a quick illustration, consider the following preference model with strict, unweighted orderings:

    p1 : r1 > r2 > r3 > r4 > r5
	p2 : r3 > r4 > r1 > r5 > r2
	p3 : r2 > r5 > r3 > r1 > r4
	p4 : r2 > r4 > r1 > r3 > r5
	p5 : r5 > r1 > r3 > r2 > r4
	
We first assume that all individuals receive their most preferred role. However, in this instance, a collision occurs: both p3 and p4 want r2 the most. In this case, we move to the next level of preferences, where p3 wants r5 and p4 wants r4. One of these roles has not been assigned (r4), thus we assign r4 to p4 and r2 to p3, since p4 (in theory, since we have unweighted orderings) wants r4 more than p3 wants r4. We continue traversing down the tree until one person wants another role more than the other. In the event that two people have the same preference ordering, the job pick order is assigned randomly at runtime.

Files
-----

ranked_prefs.py: The library.
test_prefs.py: A sample test run that illustrates how to use the library.