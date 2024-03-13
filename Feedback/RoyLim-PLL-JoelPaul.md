# Properties of Laser Light (PLL)

Author of this peer review (name): Roy Lim
Author of the lab report being reviewed (name): Joel Paul
Expected mark based on the final report rubric (/10): 4

## Areas Done Well

- Theory
  - Presented very cleanly and was easy to understand
- Graphs
  - Graphs are pretty and labelled well
  - Very good Python skills and very well done data processing

## Areas For Improvement

The report is difficult to comment on since most of the data are presented without analysis.
The main thing would be focus on getting the theory and analysis right
- Explain what you are trying to get
- Explain what you got 
- Explaining the error and causes of them

Here are things to look out for
- Theory
  - What are spatial filters? (from the Lab Summaries document)

- Result
  - Most of this comes down to not really explain what your results means
    - The interpretation of your results are unclear
  - Have a small line discussing whether true value is between error bounds
  - Explain why your results may differ (i.e what are your sources of error)
  - For your Laser Output Spectrum, you need to zoom in around 600-700nm otherwise its difficult to see
  - Make sure to explain how you fitted a function in Beam Divergence graph
    - E.g. what function did you use? A gaussian? 


## Suggestions 
Print values with to 2 sig figs or 2 dp to make it more readable, for instance, this should print 5.0
```python
print(f"{5.00023:.2f}") # 2 DP
print(f"{5.00023:.2e}") # 2 Sig Fig
```

- Misc
  - In your final report, you need to include your Jupyter Notebook and any notes you took in your lab book
