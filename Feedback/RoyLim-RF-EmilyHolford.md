# Radiation Fundamentals (RF)

Author of this peer review (name): Roy Lim
Author of the lab report being reviewed (name): Emily Holford
Expected mark based on the final report rubric (/10): 6

## Areas Done Well

- Derivation of uncertainty was clear 
- Graphs were really well done with line of best fit and standard deviation included

## Areas For Improvement

- From the PHYS3112 Lab Summaries for Radiation Fundamentals:
  - you need to explain how a Geiger Muller counter works and experimental considerations
    - Your explanation of the device should be the first thing in the report, rather than in your conclusion.
  - Didn't really see you talk about how magnetic field affect radiation?

### Statistics of Radioactive Decay
- Method
  - Method feels very simplistic
  - Maybe refer to operating instructions (add a note saying the notes or operating instructions includes more details
    on how the experiment is conducted)

- Uncertainty / Background
  - Should explain why we use a Poisson distribution for radiation. 
  - Maybe just add a bit talking about how radiation follows Poisson Distribution + source

- Background
  - Maybe include that we expect $s/\sqrt{A} = 1$ in your background 

- Causes of error?
  - What causes error within the experiment? 
    - How might the equipment affect measurements?
  - Why would the decay follow a more Gaussian distribution?


### Geiger-Muller Tube Characters (Count rate vs Voltage)

- Method
  - Same as first experiment, needs more detail or reference to notes/operating instructions

- Background / Discussion
  - Not really sure what you expect 
    - How does voltage affect count? Include some physical reasoning.
  - How did you create the fit?
    - What function did you use? E.g Power Function

### Geiger-Muller Tube Characters (Dead Time)

- Background
  - Not sure what dead time is or what your expected answers are
  - Is there a distribution we expect? E.g. exponential distribution for time between detection events?

### Absorption of Radiation Matter

- Results
  - What are the units for absorption?
  

## Suggestions 
In LaTeX, you can use the functions \ref{} and \label{} to make it clearer on what you are referring to.
For example:
```
\begin{figure}
    \centering
    \includegraphics[width=0.5\textwidth]{figures/figure.png}
    \caption{Caption}
    \label{fig:graph_name}
\end{figure}

As seen in figure \ref{fig:graph_name}...
```
- Misc
  - In your final report, you need to include your Jupyter Notebook and any notes you took in your lab book
