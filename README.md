Topic Coherence Using WordNet
=============================

Topic label groups that were generated using both chi-squared and mutual information methods are listed in
`bbc_topic.py`.

In addition, two extra topic groups have been added for comparison. The two extra groups were made up and *should*
return high topic coherence. These are a group of colours (`pink`,`purple`,`blue`,`yellow`,`green`,`white`,`orange`,
`brown`,`red`) and fruits (`apple`,`orange`,`pear`,`banana`,`plum`,`apricot`,`mango`,`grape`,`pineapple`).

`coherence_lch_wup.py` uses NLTK implementations of the LCH and WUP algorithms, this should be run in Python3. You will
need to download NLTK resources by running nltk.download()

`coherence_lesk.py` uses an implementation of LESK written in Python2.7, the code for this is included in the pyswd
directory.