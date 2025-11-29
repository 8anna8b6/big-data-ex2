Exercise 1
Q1. How many files are there now?

6 output files,plus the _SUCCESS file, but _SUCCESS is not considered a data file

Q2. Did number of mappers change?

No (mappers are based on input splits, not reducers)

Q3. Did number of reducers change?

Yes.The reducer count changed to 6 because we specified -numReduceTasks 6

Q4. Did number of output files change? Why?

Yes. Hadoop creates one output file per reducer, so more reducers = more output files.

Q5. What does “Merged Map outputs” represent?

It represents the total number of intermediate map output files that reducers merge before running reduce().

Exercise 2

Q1. Is your change in the mapper or in the reducer?

In the mapper.

Q2. Submit code in GitHub

Exercise 3

Q1. Is your change in the mapper or the reducer?

In the reducer.

Both must be done before counting, so the mapper emits normalized keys.

