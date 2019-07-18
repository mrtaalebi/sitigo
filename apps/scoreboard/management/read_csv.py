
def wow(csv_path, contest_tier_id):
    with open(csv_path) as f:
        for line in f:
            l = line.split(',')
            name = l[0]
            country = l[1]
            ruler = l[2]
            rank = l[3]
            scores = l[4:]
            
            if country.objects.filter(name=country).count() == 0:
                Country.objects.create(name=country)
            country = Country.objects.get(name=country)

            if Ruler.objects.filter(name=ruler).count() == 0:
                Ruler.objects.create(name=ruler)
            ruler = Ruler.objects.get(name=ruler)
            
            c = Contestant.objects.create(name=name,
                    country=country,
                    ruler=ruler,
                    rank=int(rank)
                )

            for i, sc in enumerate(scores):
                ProblemScore.objects.create(p_id=i+1, score=int(sc), contestant=c)

        return 0

    return 1


