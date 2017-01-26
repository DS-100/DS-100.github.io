---
layout: page
title: "Syllabus"
description: "Course Syllabus"
group: navigation
order: 2
---
{% include JB/setup %}


This schedule is still under development and is subject to change.  


<table class="table table-striped">
   <colgroup>
      <col class="col-md-1">
      <col class="col-md-1">
      <col class="col-md-2">
      <col class="col-md-8">
   </colgroup>
<thead>
   <tr>
      <th> Week </th>
      <th> Lecture </th>
      <th> Date </th>
      <th> Topic </th>
   </tr>
</thead>
<tbody>


<!-- This is the dates for all the lectures -->
{% capture dates %}
 01/17/2017 01/19/2017
 01/24/2017 01/26/2017
 01/31/2017 02/02/2017
 02/07/2017 02/09/2017
 02/14/2017 02/16/2017
 02/21/2017 02/23/2017
 02/28/2017 03/02/2017
 03/07/2017 03/09/2017
 03/14/2017 03/16/2017
 03/21/2017 03/23/2017
 03/28/2017 03/30/2017
 04/04/2017 04/06/2017
 04/11/2017 04/13/2017
 04/18/2017 04/20/2017
 04/25/2017 04/27/2017
 05/02/2017 05/04/2017
{% endcapture %}
{% assign dates = dates | split: " " %}


<!--
The actual lectures.  Dates are rendered automatically using Jekyll
 -->

{% include syllabus_entry dates=dates %}
### Course Overview [Gonzalez]
In this lecture we define and motivate the study of data science and outline the key ideas covered throughout the class.

##### Lecture Notes 
* [pptx with animations](https://drive.google.com/open?id=0Bze55lezLJhIN2d5eWJRV2ZYanc) 
* [pdf](https://drive.google.com/open?id=0Bze55lezLJhIeVkwUFNocUhNakU)
* [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIN1JzZW5CM3YtRHc) 

#### Homework 1 Released
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### The Data Science Lifecycle [Gonzalez]
In this lecture we introduce the data-science lifecycle and explore each stage by analyzing tweets from the 2016 presidential election.

##### Lecture Notes 
* [pptx with animations](https://drive.google.com/open?id=0Bze55lezLJhIUHpPMV92ek9JNkE)
* [pdf](https://drive.google.com/open?id=0Bze55lezLJhIakhySzdkaVhLdVE)
* [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIM1NNS2ZNNEwxdDQ) 
* [Jupyter Notebook (HTML)](assets/notebooks/food_safety/lecture.html)
* [Jupyter Notebook (Raw)](assets/notebooks/food_safety/SF_Food_Safety.ipynb) 
* [Data Needed for the Notebook](assets/notebooks/food_safety/data.tar.bz2) 


{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Problem Formulation and Experimental Design [Yu]
In this lecture we provide an overview of how to formulate hypothesis, identify sources of data, and construct basic experiments to collect data.

##### Lecture Notes 
* [pptx with animations](https://drive.google.com/open?id=0Bze55lezLJhIVWxwMTRLM096UjQ)
* [pdf](https://drive.google.com/open?id=0Bze55lezLJhIb2MtU2ZCWEY2dlU)
* [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhINU5lZFEtRjdPR3c) 

#### Homework 1 Due

#### Homework 2 Released
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Data Wrangling [Hellerstein]
In this lecture we explore the challenges of data preparation (e.g., assessing, structuring, cleaning, and rolling up data) and the kinds of errors commonly found in the real world.

#### Lecture Notes
* [pptx with animations](https://drive.google.com/open?id=0B2k285AK-3KEVlllcndGTWdaVGM) 
* [pdf](https://drive.google.com/open?id=0B2k285AK-3KESWpNOWN2MVZkZjg)
* [pdf 6up](https://drive.google.com/open?id=0B2k285AK-3KEaGsycTgyWFZ1M3c) 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Exploratory Data Analysis [Nolan]
In this lecture we provide an overview of exploratory data analysis (EDA).
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Visualization and Communication [Nolan]

This lecture covers how to effectively visualize and communicate complex results to a broader audience.

#### Homework 2 Due
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### Prediction and Inference [Yu]

In this lecture we will explore the key types and challenges of inference and predictions.  We will provide an overview of the categories of prediction problems and introduce some of the key machine learning tools in python.

#### Homework 3 Released
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Advanced Python Data Science Tools [Gonzalez]
In this lecture we will introduce Pandas, dataframe manipulation, python visualization, and some of the batch oriented philosophy of scalable data processing.

{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Transforming Data to Tables in Python [Hellerstein]
In this lecture we talk about the process of converting unstructured and semi-structured data to tables and arrays.  We will cover text processing, regular expressions, and structural transformations.
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### SQL and Big Data [Hellerstein]
In this lecture we introduce SQL and the relational model.

#### Homework 3 Due
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### SQL Continued [Hellerstein]
In this lecture we will introduce data analysis techniques with a focus on aggregation and summary statistics.

#### Homework 4 Released
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}

### Basic Modeling using Statistical Distributions [Nolan]
In this lecture we provide an overview of several basic distributions and discuss some of the challenges of working with skewed data.

<!-- Let's connect summary statistics to the SQL discussion in the previous lecture. -->

{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Maximum Likelihood Estimation [Nolan]

In this lecture we fit basic models to data by applying the method of maximum likelihood estimation.

{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### TBD
<!--
### Bayesian Models and Working with Priors [Gonzalez]
In this lecture we introduce the concept of priors and explore the use Bayes Rule in model design.
 -->

#### Homework 4 Due

{% include syllabus_entry end=true %}






{% include syllabus_entry dates=dates %}
### Midterm Review [Gonzalez]

{% include syllabus_entry end=true %}

{% include syllabus_entry dates=dates %}
## _Tentative_ Midterm
This may change in the weeks before class starts as we adjust the schedule.
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Least Squares Regression and Hypothesis Testing [Yu]
In this lecture dives into the details of least squares regression through the lens of empirical risk minimization while discussing some of the key modeling assumptions.

#### Homework 5 Released
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Loss Functions and Generalized Linear Models [Yu]
This lecture extends the earlier discussion on least squares regression to categorical data and introduce the gradient descent algorithm.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Feature Engineering and the Bias Variance Trade-off [Gonzalez and Nolan]
This lecture explores how simple linear techniques can be used to address complex non-linear relationships on a wide range of data types.  This will bring us to a fundamental challenging in learning and statistical inference (the bias-variance trade-off)
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Regularization and Cross Validation [Gonzalez and Nolan]

This lecture will continue our discussion on the bias variance trade-off by introducing the concept of regularization.  We then introduce cross validation as a mechanism to optimize the trade-off between bias and variance.

#### Homework 5 Due
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### Spring Break
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Spring Break
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Classification and Regression Trees [Nolan and Yu]

This lecture introduces an alternative approach to feature engineering using classification and regression trees (CART).

#### Homework 6 Released
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Non-Parametric Models [Gonzalez]

This lecture introduces non-parametric modeling techniques and discusses k-nearest neighbor and kernel regression.

{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### Dimensionality Reduction [Gonzalez]

This lecture introduces the Singular Value Decomposition algorithm for dimensionality reduction.

{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Clustering and the Mixed Membership Model [Nolan and Yu]

This lecture explores unsupervised learning techniques to aid in exploratory data analysis.  In particular we focus on mix-membership models and introduce the EM algorithm.

#### Homework 6 Due

{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Data Acquisition [Hellerstein]
This lecture discusses how to get data from a variety of common sources and includes the topics of crawling, scraping, the DOM, XML, HTTP req., and REST APIs.


#### Homework 7 Released
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Analytics at Scale [Hellerstein]

Streaming algorithms and online estimation: sketching and sampling.

<!-- joey finish -->

{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### The Big-data Ecosystem and Technologies [Gonzalez]

In this lecture we provide an overview of the data technologies commonly used today and their implications on data analysis, map-reduce, etl ...


{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### TBD

#### Homework 7 Due

{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### RRR Review
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### RRR Review
{% include syllabus_entry end=true %}





<!--
Topics Dropped from lecture outline for first teaching
-->



<!--
{% include syllabus_entry dates=dates %}
### Database Schema Design [Hellerstein]
In this lecture we describe how to create and organize tables in a database to mitigate errors and improve access efficiency.
{% include syllabus_entry end=true %}
-->


<!--
{% include syllabus_entry dates=dates %}
### Hypothesis Testing and False Discovery
In this lecture will go into more detailed hypothesis testing procedures and highlight some of the challenges of false discovery in the setting of repeated hypothesis tests.
{% include syllabus_entry end=true %}
 -->


<!--
{% include syllabus_entry dates=dates %}
### Text Modeling
This lecture explores techniques used to model text data including n-gram models, TF-IDF, LSA, and LDA.
{% include syllabus_entry end=true %}
 -->


<!--
{% include syllabus_entry dates=dates %}
### Collaborative Filtering
This lecture explores nearest neighbor, graph similarity, and matrix factorization techniques for content recommendation.
{% include syllabus_entry end=true %}
 -->

<!--
{% include syllabus_entry dates=dates %}
###  Deep Learning
This lecture connects deep learning to the earlier lectures on regression and touches on recent developments in predictive modeling using neural networks.
{% include syllabus_entry end=true %}
 -->


<!--
{% include syllabus_entry dates=dates %}
### Version Control [Gonzalez]
In this tools oriented lecture we will cover version control and techniques around managing data and code development to ensure repeatedly analysis.
{% include syllabus_entry end=true %}
 -->

</tbody>
</table>


<!--

A little script to highlight the week that is next

There is currently a bug in this script which someone needs to fix.  When I wrote this script for my graduate seminar class we only had one lecture a week. We should modify the Jekyll code to render the syllabus with each row tagged so we can automatically identify the week and lecture day.

-->



<script type="text/javascript">
var current_date = new Date();
var rows = document.getElementsByTagName("th");
var finished =  false;
for (var i = 1; i < rows.length && !finished; i++) {
   var r = rows[i];
   if (r.id.startsWith("counter_")) {
      var fields = r.id.split("_")
      var week_div_id = "week_" + fields[2]
      var lecture_date = new Date(fields[1] + " 23:59:00")
      if (current_date <= lecture_date) {
         finished = true;
         r.style.background = "orange"
         r.style.color = "black"
         var week_td = document.getElementById(week_div_id)
         week_td.style.background = "#043361"
         week_td.style.color = "white"
      }
   }
}
</script>

