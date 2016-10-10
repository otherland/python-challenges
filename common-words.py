checkio = lambda one, two: ",".join(sorted(i for i in two.split(",") if i in one.split(",")))
checkio = lambda one, two: ",".join(sorted(set(one.split(",")) & set(two.split(","))))


checkio("hello,world", "hello,earth") == "hello"

checkio("one,two,three", "four,five,six") == ""

checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

