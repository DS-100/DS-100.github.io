---
layout: header_page
title: Data Science 100
tagline: Principles and Techniques of Data Science
---
{% include JB/setup %}



This document contains early descriptions of a course that is actively under development.
I am sharing this information to collect feedback and help students plan for future courses.
Students who are interested in either taking or helping to TA DS100 and would like more details please fill out <a href="https://goo.gl/forms/od8j3HcBsOH1pLWA3"> this Google form</a>.

<br/>
<br/>

<!-- # DS100: Principles & Techniques of Data Science -->

<div class="container-fluid">
<div class="row">
<div markdown="1" class="col-sm-9">
**Summary:** Combining data, computation, and inferential thinking, data science is redefining how people and organizations solve challenging problems and understand the world.
This intermediate level class bridges between [Data 8](http://data8.org/fa16/) and upper division computer science and statistics courses as well as methods courses in other fields.
In this class, students will master the data science life-cycle and learn many of the basic principles and techniques of data science spanning algorithms, statistics, machine learning, visualization, and data systems.
Skills and expertise developed in this class will enable students to pursue careers in data science or apply data-science to research.


### Goals

* Students will build the basic understanding of the concepts in data science enabling them to apply computational and inferential thinking to real-world problems

* Students will develop the foundation needed to learn new data science techniques and concepts quickly thereby excelling in advanced Berkeley courses in data-management ([CS186](http://www.cs186berkeley.net)), machine learning ([CS189](https://people.eecs.berkeley.edu/~jrs/189/)), and statistics

* Students will develop skills needed to start careers as data scientists


</div>
<div class="col-md-3" markdown="1">
![lifecycle](assets/images/lifecycle3_cropped.png){:height="200px"}
<!-- <img src="{{ site.baseurl }}assets/images/lifecycle2.png" alt="Lifecycle Logo" style="height: 300px"/> -->
</div>
</div>
</div>



## Context

This course is a gateway to upper division courses in both the foundations and the application of data science principles and techniques.
We expect that DS100 will be widely enrolled by students in many majors, as well as graduate students in many fields, but it will be held to a moderate size in the first offering.
<!-- It will fill a substantial hole in current offerings that will be essential to cover if future minors or major in data science are to be offered.
 -->
In the first offering of this class we would like to keep enrollment relatively small, around 100, to enable closer interaction with students as challenges arise.  We expect later offerings to be substantially larger.


## Prerequisites

While we are working to make this class widely accessible in the initial ([beta](https://en.wikipedia.org/wiki/Software_release_life_cycle)) version of the class we plan to require the following (or equivalent):

1. **Foundations of Data Science:** [**CS/INFO/Stat C8**](http://data8.org/fa16/)  This is an *excellent* class that covers much of the material in DS100 but at a higher level.  This class provides basic exposure to python programming and working with tabular data as well as visualization, statistics, and ML.


1. **Computing:** *The Structure and Interpretation of Computer Programs* [**CS61a**](http://cs61a.org)  or *Computational Structures in Data Science* [**CS88**](http://cs88-website.github.io:)   These courses will provide additional background in python programming (e.g., *for loops*, *lambdas*, *debugging*, and *complexity*) that will enable DS100 to focus more on the concepts in Data Science and less on the details of programming in python.  However, students that are proficient in python may request to have these pre-requisites waived.


1. **Math:** *Calculus and Linear Algebra* ([Math 54](https://math.berkeley.edu/~nadler/54fall2015.html) or [EE 16a](http://inst.eecs.berkeley.edu/~ee16a/fa16/)): We will need some basic concepts like linear operators, eigenvectors, derivatives, and integrals to enable statistical inference and derive new prediction algorithms.  Students with a strong mathematics background may be able to skip this prerequisite.  *This may be satisfied concurrently to DS100*


## Textbooks:

Because data science is a relatively new and rapidly evolving discipline there is no single *ideal* textbook for the course.
Instead we plan to use reading from a collection of books all of which are free.
However, we have listed a few optional books that will provide additional context for those who are interested.

#### Primary Books
* **[Introduction to Statistical Learning:](http://www-bcf.usc.edu/~gareth/ISL/)** (Free online PDF) This book is a great reference for the machine learning and some of the statistics material in the class

* **[Data Science from Scratch:](http://shop.oreilly.com/product/0636920033400.do)** (Free to Berkeley students) This more applied book covers many of the topics in this class using Python but doesn't go into sufficient depth for some of the more mathematical material.

#### Secondary Books
*  **[Doing Data Science:](http://shop.oreilly.com/product/0636920028529.do)** This books provides a unique case-study view of data science but uses R and not Python.




## Current *Tentative* Course Outline

{% assign counter = 1 %}

### Module 0: *Course Overview*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Course Overview*:** What is data science and how does this class relate to it?


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *The Data Science Lifecycle*:** In this lecture we will work through the entire data science lifecycle by exploring the "presidential" tweets.


### Module 1: *Data Science Lifecycle*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Problem Formulation and Domain Understanding*:**
In this lecture we will discuss the challenges of experimental design (sampling, observational, controlled), and data collection.

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Data Acquisition Cleaning*:**
In this lecture we will explore the process of collecting and cleaning data from a variety of sources and formats. We will also introduce the dataset we will study for the next two weeks (tweets around the debates) and discuss some of the challenges in collecting and cleaning the data.  In this lecture we will begin to introduce dataframes.

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Descriptive Analysis*:**
In this lecture we will analyze the tweets around the debates in conjunction with debate transcripts to get a better understanding of the data, the questions we wanted to answer and the types of questions we may want to explore.  In this lecture we will emphasize visualization.

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Inferential Analysis*:**
In this lecture we will explore basic techniques around regression and uncertainty measures to infer properties of the data and evaluate our earlier hypothesis.  We will also discuss some of the challenges around communicating these results.



The remainder of the course is then divided into topic areas that dive deeper into the concepts and principles in data science.  While these lectures are organized topically they will make frequent references to concepts through-out the data science lifecycle.



### Module 2: *Data System*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Working with relational data, introduction to SQL*:**

<!-- In this lecture students will be introduced to SQL and learn hot to manipulate and access data in a relational database.
 -->
* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Database design: schemas and normalization*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Analytics at Scale: Understanding Data Parallel Algorithms and Physical Layout (partitioning, indexing and replication)*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Overview of the big-data ecosystem: Data Warehouses, Data Lakes, and MapReduce*:**

### Module 3: *Descriptive and Inferential Statistics*


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Data summarization, visualization and communication*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Dimensionality Reduction with PCA*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Modeling data: random variables and distributions*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Power-laws and the challenges of data skew*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Hypothesis testing and false discovery*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Review of Inferential Statistical Methods*:**




### Module 4: *Statistics and Machine Learning*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*The Taxonomy of Machine Learning Methods*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Least Squares regression and Loss Functions*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Feature Engineering*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Overfitting and the bias variance Trade-off*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Regularization and Cross Validation*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Generalization of loss functions to logistic regression*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Classification and Regression Trees*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Overview of Deep Learning and its Connection to Regression*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Clustering and Mixture of Gaussians*:**

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %}
*Course Review*:**



<!--
* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Course Overview*:** What is data science and how does this class relate to it?

{% include collapse begin="true" %}
This lecture will setup the importance of data centric thinking by discussing how data is shaping society and how data science is quickly becoming a driving force across government, industry, and research.  We will introduce the data science life-cycle and describe the skills required in data science. Finally, we will provide background on the teach staff and organization of the class.

#### Learning Objectives:
* The importance of data and computational thinking in society
* The roles and skills of data scientists
* Organization of the class

{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *The Data Science Lifecycle*:** What is the workflow of a data scientist and what should I have learned in DS8?

{% include collapse begin="true" %}
This lecture will work through each state of the data science life-cycle by examining a real dataset.  This lecture we will refresh the students on the DS8 dataframe and the notebook interface.  The lecture will span data acquisition, some basic cleaning, visualization, statistical summarization, and ultimately we will build a basic predictive model.

#### Learning Objectives:
* The stages of the data science life-cycle
* Recall how to work with dataframes and notebooks
* Concepts covered throughout the rest of the class

{% include collapse end="true" %}


### Module 1: *Kinds of Data*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Working with Text and Semi-Structured Data*:** How do I transform textual and semi-structured data into easy to manipulate tabular representations?

{% include collapse begin="true" %}
In this lecture we will begin to get our hands dirty with real data.  In particular we will work with CSV and JSON log data and discuss how to transform this data into a table.

#### Learning Objectives:
* Become familiar with the challenges of operating on text and semi-structured data
* Learn basics of regular expressions
* Learn how to manipulate and traverse DOM/JSON

{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Spatial and Temporal Data*:** How do I reconcile time and space across different datasets.

{% include collapse begin="true" %}
This lecture will discuss the ubiquity of spatial and temporal data and discuss some of the key questions and challenges surrounding this data.  In particular, where and why do we study spatial and temporal data, how do we align space and time across datasets, the need for smoothing, interpolation, and extrapolation, as well as the various representations of space and time.
{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Multimedia Data*:** How do I extract and encode information from images and videos?

{% include collapse begin="true" %}
This lecture will deal with the various formats of multimedia data and the challenges of working with this data.  We will discuss issues around meta-data as well as the use of techniques in computer vision to extract important signal from this data that we can later analyze.  This will bring some discussion about machine learning earlier into the class.
{% include collapse end="true" %}

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Network Data*:** How do I reason about relationships between data?

{% include collapse begin="true" %}
This lecture will discuss the use of graphs as a mechanism to represent data.  We will review the various types of graphs (directed, undirected, bipartite, DAGs) and their interpretations as data.  We will discuss how graphs can be stored in dataframes and some of the important questions we will want to answer about graphs as we move through the course.
{% include collapse end="true" %}


### Module 2: *SQL and Data Management*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Introduction to SQL*:**
   What and why is SQL and how do I use it? (Basic queries)

{% include collapse begin="true" %}
This lecture will introduce the SQL language by motivating the use of a common declarative specification for data transformations.  We will introduce the concept of a database as a system to store, manage, and retrieve data.  We will describe the concept of a table with a schema and introduce basic queries to access the data (select where and groupby).  In this lecture we will assume that the schema and data have already been determined.
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Advanced SQL*:** How do I bring tables together, build complex queries, and reason about their costs?

{% include collapse begin="true" %}
This lecture picks up where the previous left off by introducing joins and more complex nested SQL queries.
{% include collapse end="true" %}

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Data Modeling and Normalization*:** How do I organized for easy access and error free updates.

{% include collapse begin="true" %}
This lecture will cover schema design by introducing the concept of normalization.  We will organize data for one of our running examples.  We will introduce the star-schema as a common mechanism to organize information in a normalized form. Finally we will discuss how to insert and update tuples in a database.
{% include collapse end="true" %}

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Physical Data Management*:** How do I organize data for fast access at scale?

{% include collapse begin="true" %}
This lecture will cover techniques to improve data access performance in database systems.  In particular we will discuss how indexes can be used to improve point lookups and range queries and some of the tradeoffs of adding indexes.   We will also introduce distributed data-processing in the BSP/Map-Reduce paradigm and discuss data partitioning.
{% include collapse end="true" %}

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Big Data Ecosystem*:** How is data stored and managed in large organizations?

{% include collapse begin="true" %}
This lecture will provide a survey of the terms and technologies used to manage data in large organizations.  In particular we will discuss the differences between Data Warehouses, Datamarts and Data Lakes.  We will discuss the disaggregation of data processing systems across HDFS -- (Hadoop, Spark) -- (HIVE, PIG, SparkSQL, Dataframes).  We will also mention some of the non-relational technologies including the common KV-Stores: Casandra and Mongo as well as the Pub-sub/stream systems like Kafka and Storm.  The goal is not to understand the details behind how these technologies work but instead their motivations and the implications on getting data from them.
{% include collapse end="true" %}


### Module 3: *Understanding the Data*

* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Summary Tables and Plots*:** What does the data look like?

{% include collapse begin="true" %}
**To be finished soon!**

* Use of aggregation, rollup, and slicing as mechanism to understand data
* Scatter plots, histograms, whisker plots
* Log scales
* Summarizing text and image data
{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Sketching and Stream Summarization*:** How can I summarize data efficiently at scale?

{% include collapse begin="true" %}
**To be finished soon!**

* Challenges of working with streams of data: limited memory
* Bloom Filters
* Count-Min Sketch
* Reservoir Sampling
{% include collapse end="true" %}




* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Working with Random Variables*:** What do I expect to see?

{% include collapse begin="true" %}
**To be finished soon!**

* Compute expectations
* Manipulate expectations
* Compute marginals and conditionals
* Concept of independence
{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Power Laws*:** What if my data is far from normal?

{% include collapse begin="true" %}
**To be finished soon!**

* Common pattern in many real-world datasets
* Why so common
* How to visualize
* Forms of power-laws
* Implications on statistics
{% include collapse end="true" %}




* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Parameter Estimation*:**How do I estimate the parameters of data distributions?

{% include collapse begin="true" %}
**To be finished soon!**

* Concept of maximum likelihood
* Derivation of maximum likelihood estimators
* Bias and Variance
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Bayesian Posteriors*:** How can I encode prior knowledge into my estimates?

{% include collapse begin="true" %}
**To be finished soon!**

* Motivation and role of priors
* Bayes Theorem
* MAP estimation
* Philosophical discussion about differences in perspectives between Bayesians and frequentists
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Confidence and Credibility Intervals*:** What is a reasonable range of values I might expect?

{% include collapse begin="true" %}
**To be finished soon!**

* Meaning of intervals
* How to compute from data
* Implications of frequentist vs Bayesian

{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Hypothesis Testing*:** Did my treatment have a significant effect?

{% include collapse begin="true" %}
**To be finished soon!**

* Experimental design
* A-B testing (Welch's T-test)
* Likelihood ratio tests
* Bootstrap/Permutation Tests
{% include collapse end="true" %}




### Module 4: *Making Predictions*


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Overview of Machine Learning*:** What is machine learning?

{% include collapse begin="true" %}
**To be finished soon!**

* Applications of ML
* Taxonomy of ML (from 186 lecture)
* Fundamental challenges: noise, signal, objective
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Linear Regression*:** How do I model linear relationships?

{% include collapse begin="true" %}
**To be finished soon!**

* Linear relationships in data
* Likelihood/Loss Functions
* MLE estimation
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Logistic Regression*:** How do I make predictions on categorical data?

{% include collapse begin="true" %}
**To be finished soon!**

* Logistic Likelihood/loss function
* Gradient descent
* Stochastic gradient descent as an estimator of gradient
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Feature Engineering*:** What if there is a non-linear relationship between $X$ and $Y$?

{% include collapse begin="true" %}
**To be finished soon!**

* Categorical data: one-hot-encoding
* Text data: Bag-of-words
* Image data: histograms, filters
* Basis functions
* Allude to over-fitting
{% include collapse end="true" %}




* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Overfitting and the Bias Variance Tradeoff*:** Why don't my predictions generalize?

{% include collapse begin="true" %}
**To be finished soon!**

* Bias / Variance tradeoff at a high-level
* Derive fundamental bias / variance tradeoff for squared loss
* Introduce regularization and connect to priors
* Cross validation algorithm

{% include collapse end="true" %}




* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Classification and Regression Trees*:**  How do I model complex discontinuous relationships?

{% include collapse begin="true" %}
**To be finished soon!**

* Ability to capture piecewise non-linearity
* Basic algorithm (C4.5)
* Challenges of over-fitting pruning and model averaging

{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Advanced Techniques in Supervised Learning*:** To infinite dimensions and beyond.

{% include collapse begin="true" %}
**To be finished soon!**

* The kernel trick as a generalization of feature engineering  SVMs
   * Demonstrate how to use library and discuss tradeoffs
* Deep Learning as a generalization of LR and feature engineering
   * Demonstrate how to use library and discuss tradeoffs
* Ensemble methods and model averaging (connect back to boostrap)
{% include collapse end="true" %}


* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Clustering for unsupervised Learning*:** How do I find groups of similar data.

{% include collapse begin="true" %}
**To be finished soon!**

* Problem formulation
   * Important discussion on distance functions ...
* K-Means clustering algorithm
* Choosing a good initialization
* Distance based clustering (DBSCAN)
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Dimensionality Reduction*:** How do I project my data into a lower dimensional space.

{% include collapse begin="true" %}
**To be finished soon!**

* Curse of dimensionality: challenges of working with high-dimensional data
* Simple techniques to reduce dimension: random projections and hashing
* SVD/PCA as more advanced technique
{% include collapse end="true" %}



* **(Lecture {{ counter }}) {% assign counter = counter | plus: 1 %} *Course Review*:** What did I learn in this class?

{% include collapse begin="true" %}
**To be finished soon!**

* Far too much!
{% include collapse end="true" %}

 -->


## Instructors

<!-- The following block is for faculty info -->
<div class="container-fluid">
  <script type="text/javascript">
    function email_address(dep, name) {
      domain = dep + 'berkeley';
      tld = 'edu';
      document.write(
        '<a href="mailto:' + name + '@' + domain + '.' + tld + '">' +
        name + '@' + domain + '.' + tld + '</a>');
  }
  </script>
  <div class="row">
    <div class="col-sm-3"><div class="text-center">
      <img src="https://jegonzal.github.io/assets/jegonzal.jpg" alt="Joey Gonzalez" style="height: 150px;"/>
      <address>
        <strong>Joseph E. Gonzalez</strong><br>
        <script type="text/javascript"> email_address("cs.", "jegonzal") </script>
      </address>
    </div></div>
    <div class="col-sm-3"><div class="text-center">
      <img src="https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/hellerstein.jpg" alt="Joseph Hellerstein" style="height: 150px;"/>
      <address>
        <strong>Joseph Hellerstein</strong><br>
        <script type="text/javascript"> email_address("cs.", "hellerstein") </script>
      </address>
    </div></div>
    <div class="col-sm-3"><div class="text-center">
      <img src="https://www.stat.berkeley.edu/~binyu/Site/Welcome_files/Yu_Bin13.jpg" alt="Bin Yu" style="height: 150px;"/>
      <address>
        <strong>Bin Yu</strong><br>
        <script type="text/javascript"> email_address("stat.", "binyu") </script>
      </address>
    </div></div>
    <div class="col-sm-3"><div class="text-center">
      <img src="http://www.stat.berkeley.edu/~nolan/images/Deb-Nolan.jpg" alt="Deborah Nolan" style="height: 150px;"/>
      <address>
        <strong>Deborah Nolan</strong><br>
        <script type="text/javascript"> email_address("stat.", "nolan") </script>
      </address>
    </div></div>
  </div>
</div>


<!-- | <img src="https://jegonzal.github.io/assets/jegonzal.jpg" alt="Joey Gonzalez" style="height: 150px;"/> | <img src="https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/hellerstein.jpg" alt="Joseph Hellerstein" style="height: 150px;"/> | <img src="https://people.eecs.berkeley.edu/~raluca/RalucaPreVeil.jpg" alt="Raluca Ada Popa" style="height: 150px;"/> | <img src="https://people.eecs.berkeley.edu/~istoica/ion_picture_small.jpg " alt="Ion Stoica" style="height: 150px;"/> |
|:-:|:-:|:-:|:-:|
| Joseph E. Gonzalez | Joe Hellerstein | Raluca Ada Popa | Ion Stoica |
| <script type="text/javascript"> email_address("jegonzal") </script>| <script type="text/javascript"> email_address("hellerstein") </script>| <script type="text/javascript"> email_address("raluca.popa") </script> | <script type="text/javascript"> email_address("istoica") </script> | -->




