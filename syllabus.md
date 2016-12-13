---
layout: page
title: "Syllabus"
description: "Course Syllabus"
group: navigation
order: 2
---
{% include JB/setup %}



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
{% endcapture %}
{% assign dates = dates | split: " " %}


<!-- 
The actual lectures.  Dates are rendered automatically using Jekyll
 -->

{% include syllabus_entry dates=dates %}
#### Course Overview
In this lecture we define and motivate the study of data science and outline the key ideas covered throughout the class.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### The Data Science Lifecycle
In this lecture we introduce the data-science lifecycle and explore each stage by analyzing tweets from the 2016 presidential election.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Problem Formulation and Experimental Design 
In this lecture we provide an overview of how to formulate hypothesis, identify sources of data, and construct basic experiments to collect data.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Data Wrangling and Regular Expressions
In this lecture we explore the challenges data cleaning and preparation (e.g., parsing and processing unstructured text data, semi-structured formats like JSON, and XML) 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Exploratory Data Analysis and Visualization
In this lecture we provide an overview of the bid ideas in exploratory data analysis and data visualization.  
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Prediction and Inference
In this lecture we will explore the key types and challenges of inference and predictions and introduce a few standard prediction and inference techniques.  
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Pandas
In this tools oriented lecture we develop regular expressions and learn some of the more advanced software tools and concepts that will be used throughout the class. 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Version Control and Lineage
In this tools oriented lecture we will cover version control and techniques around managing data and code development to ensure repeatedly analysis.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Basic Modeling using Statistical Distributions
In this lecture provide an overview of several basic distributions and how to estimate the parameters of those distributions from data.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Power-laws and the Challenges of working with Skewed Data
In this lecture we discuss common power-law patterns in data and their implications on modeling and analysis.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Bayesian Models and Working with Priors
In this lecture we introduce the concept of priors and explore the use Bayes Rule in model design.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Hypothesis Testing and False Discovery
In this lecture will go into more detailed hypothesis testing procedures and highlight some of the challenges of false discovery in the setting of repeated hypothesis tests.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### _Tentative_ Midterm 
This may change in the weeks before class starts as we adjust the schedule.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### SQL and Relational Databases
In this lecture we introduce SQL and relational database systems. 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Database Schema Design
In this lecture we describe how to create and organize tables in a database to mitigate errors and improve access efficiency.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Analytics at Scale 
In this lecture we introduce the design of map-reduce and data parallel compute frameworks and discuss issues around physical data-layout and its implications on analysis.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Overview of the Big-data Ecosystem
In this lecture we provide an overview of the data technologies commonly used today and their implications on data analysis. 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### The Taxonomy of Machine Learning
This lecture provides an overview of the categories of problems addressed by machine learning techniques and some guidance on how to frame machine learning problems.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Least Squares Regression and Loss Functions
In this lecture dives into the details of least squares regression through the lens of empirical risk minimization while discussing some of the key modeling assumptions.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Generalization of Loss Functions to Logistic Regression
This lecture extends the earlier discussion on least squares regression to categorical data and introduce the gradient descent algorithm.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Feature Engineering
This lecture explores how simple linear techniques can be used to address complex non-linear relationships on a wide range of data types.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Over-fitting and Cross Validation 
This lecture introduces the critical challenges of over-fitting and discuss how to address over-fitting through regularization and cross validation.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Overview of Deep Learning
This lecture connects deep learning to the earlier lectures on regression and touches on recent developments in predictive modeling using neural networks.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Classification and Regression Trees
This lecture introduces an alternative approach to feature engineering using CART.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Unsupervised Learning Clustering
This lecture explores unsupervised learning techniques to aid in exploratory data analysis.  In particular we focus on mix-membership models and introduce the EM algorithm.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Dimensionality Reduction
This lecture introduces the Singular Value Decomposition algorithm for dimensionality reduction.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Text Modeling 
This lecture explores techniques used to model text data including n-gram models, TF-IDF, LSA, and LDA. 
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### Collaborative Filtering
This lecture explores nearest neighbor, graph similarity, and matrix factorization techniques for content recommendation.
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
#### TBD
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Course Review
{% include syllabus_entry end=true %}




</tbody>
</table>


<!--

A little script to highlight the week that is next

-->
<script type="text/javascript">
var current_date = new Date();
var rows = document.getElementsByTagName("tr");
var finished =  false;
for (var i = 1; i < rows.length && !finished; i++) {
   var r = rows[i];
   var date_text = r.getElementsByTagName("td")[1].textContent;
   console.log(date_text)
   var d = new Date(date_text + " 14:00:00");
   if (current_date <= d) {
      finished = true;
      var children = r.childNodes
      children[1].style.background = "orange"
      children[1].style.color = "black"
      children[3].style.background = "red"
      children[3].style.color = "white"
   }
}
</script>

