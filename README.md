# spelling_correction_using_ngram
This is Out Information Retrieval Project.
Build On Django Framework


this is the flow of our spelling correction : 
- extract big.text into list of string
- preprocess the list of string
- make a n-gram index (bigram)
- make a query into a bigram
- look up into bigram index
- count the probability using jaccard
- return the suggestion word if probability more than or equal 0.5
