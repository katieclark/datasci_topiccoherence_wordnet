from bbc_topics import chisquared
from pyswd.pywsd import adapted_lesk

for community_id, topics in chisquared.items():
    score = 0
    print(' '.join(topics))
    for topic in topics:
        all_other_topics = [t for t in topics if t!=topic]
        # for t in all_other_topics:
        sent = ' '.join(all_other_topics)
        print(topic)
        top = adapted_lesk(sent, topic)#, stem=False, nbest=True, keepscore=True)
        if top:
            print('Top result:' + top.definition())

        results = adapted_lesk(sent, topic, nbest=True)
        if results:
            for result in results:
                print(str(result.definition()))

        correct = raw_input("Correct choice? ")
        if correct=='y':
            score+=1
    print('Score: ' + str(score/float(len(topics))))
    print