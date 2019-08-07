


def test_check(aggregator, instance):
    check = BurrowCheck('burrow', {}, {})
    check.check(instance)

    aggregator.assert_all_metrics_covered()
