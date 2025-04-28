def test_function(request):
    excution_count = request.node.execution_count
    if excution_count:
        print(f"当前重试轮数{excution_count}")
    assert False
