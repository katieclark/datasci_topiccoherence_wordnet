from nltk.corpus import wordnet

from bbc_topics import chisquared, mutualinfo
from statistics import median
import operator
import numpy as np

# compare one synset against all other synsets from other topics
def get_similarity_values(topic_synset, synsets):
    lch = []
    wup = []
    for synset in synsets:
        # can't compare similarity if not same pos
        if topic_synset.pos()==synset.pos():
            lch_value = topic_synset.lch_similarity(synset)
            if lch_value:
                lch.append(lch_value)

            wup_value = topic_synset.wup_similarity(synset)
            if wup_value:
                wup.append(wup_value)
            # res = topic_synset.res_similarity(synset, None)
            # jcn = topic_synset.jcn_similarity(syn2)
            # lin = topic_synset.lin_similarity(syn2)
    return lch, wup


# get similarity values for all topics synsets then calculate median value
def get_coherence(syn_topic, topic_synsets, all_synsets):
    lch = []
    wup = []
    # for each synset for a topic, compare it to all other
    # possible synsets from other topics
    for topic_synset in topic_synsets:
        for topic, synsets in all_synsets.items():
            if syn_topic == topic:
                continue
            if len(synsets) == 0:
                continue
            lch_values, wup_values = get_similarity_values(topic_synset, synsets)
            lch.extend(lch_values)
            wup.extend(wup_values)

    if len(lch)>1 and len(wup)>1:
        # return mean value for all of this topic's synsets
        return np.mean(lch), np.mean(wup)
    elif len(lch)==1 and len(wup)==1:
        return lch[0], wup[0]
    else:
        return 0, 0


def get_topic_synset_map(topics):
    synsets = {}
    for topic in topics:
        all_syns = []
        for syn in wordnet.synsets(topic):
            all_syns.append(syn)
        if len(all_syns)>0:
            synsets[topic] = all_syns
    return synsets



lch_community_label_score = {}
wup_community_label_score = {}
for community_id, topics in chisquared.items():

    synsets = get_topic_synset_map(topics)

    values_lch = {}
    values_wup = {}
    for topic, topic_synsets in synsets.items():
        # get median similarity values of topic synsets against all other synsets
        # (median of all pairwise scores for all topic synset values
        # vs. individual synsets from all other synsets)
        lch, wup = get_coherence(topic, topic_synsets, synsets)
        values_lch[topic] = lch
        values_wup[topic] = wup


    print('lch scores:') #scores per topic
    for key, value in sorted(values_lch.items(), key=operator.itemgetter(1)):
        print(key + ' ' + str(value))

    # get mean lch score for this community
    lch_keys = ','.join(values_lch.keys())
    lch_mean = median(list(values_lch.values()))
    lch_community_label_score[lch_keys] = lch_mean

    print('wup scores:')#scores per topic
    for key, value in sorted(values_wup.items(), key=operator.itemgetter(1)):
        print(key + ' ' + str(value))

    # get mean wup score for this community
    wup_keys = ','.join(values_wup.keys())
    wup_mean = median(list(values_wup.values()))
    wup_community_label_score[wup_keys] = wup_mean

print('lch community scores:')
# list communities by order of their similarity score
for key, value in sorted(lch_community_label_score.items(), key=operator.itemgetter(1)):
    print(key + ' ' + str(value))

print('wup community scores:')
for key, value in sorted(wup_community_label_score.items(), key=operator.itemgetter(1)):
    print(key + ' ' + str(value))








