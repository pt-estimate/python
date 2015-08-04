from inferences_about_a_population.estimation_by_ci import wilson_score_interval

def confidence_sort(samples, alpha):
    """Sorts by the lower bound of the wilson score confidence interval"""
    for k,v in samples.items():
        success_count = v[0]
        total_count = v[1]
        lb, ub = wilson_score_interval(success_count, total_count, alpha)
        samples[k]=lb
    confidence_sorted = sorted(samples, key=samples.__getitem__)
    return confidence_sorted
