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
 05/11/2017
{% endcapture %}
{% assign dates = dates | split: " " %}


<!--
The actual lectures.  Dates are rendered automatically using Jekyll
 -->

{% include syllabus_entry dates=dates %}
### Course Overview [Gonzalez]
In this lecture we define and motivate the study of data science and outline the key ideas covered throughout the class.

##### Lecture Notes 
* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIN2d5eWJRV2ZYanc), [pdf](https://drive.google.com/open?id=0Bze55lezLJhIeVkwUFNocUhNakU), [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIN1JzZW5CM3YtRHc))

* Additional Optional Reading: Chapter 1 from [Doing Data Science](http://proquest.safaribooksonline.com/9781449363871) and [Data Science from Scratch](http://proquest.safaribooksonline.com/9781491901410)

#### Homework 1 Released
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### The Data Science Lifecycle [Gonzalez]
In this lecture we introduce the data-science life-cycle and explore each stage by analyzing tweets from the 2016 presidential election.

##### Lecture Notes 
* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIUHpPMV92ek9JNkE),
[pdf](https://drive.google.com/open?id=0Bze55lezLJhIakhySzdkaVhLdVE),
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIM1NNS2ZNNEwxdDQ))
* SF Food Safety Demo ([html](assets/notebooks/food_safety/lecture.html),
[raw](assets/notebooks/food_safety/SF_Food_Safety.ipynb), [data](assets/notebooks/food_safety/data.tar.bz2))

{% include syllabus_entry end=true %}







{% include syllabus_entry dates=dates %}
### Problem Formulation and Experimental Design [Yu]
In this lecture we provide an overview of how to formulate hypothesis, identify sources of data, and construct basic experiments to collect data.

##### Lecture Notes 
* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIVWxwMTRLM096UjQ), 
[pdf](https://drive.google.com/open?id=0Bze55lezLJhIb2MtU2ZCWEY2dlU),
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhINU5lZFEtRjdPR3c))

#### Homework 2 Released

#### Homework 1 Due

{% include syllabus_entry end=true %}







{% include syllabus_entry dates=dates %}
### Data Wrangling [Hellerstein]
In this lecture we explore the challenges of data preparation (e.g., assessing, structuring, cleaning, and rolling up data) and the kinds of errors commonly found in the real world.

#### Lecture Notes
* Slides ([pptx](https://drive.google.com/open?id=0B2k285AK-3KEZFhsQzRKQWFaN00), [pdf](https://drive.google.com/open?id=0B2k285AK-3KEbE5GQ3BCZXI1V28), [pdf 6up](https://drive.google.com/open?id=0B2k285AK-3KESmplRWlpc2F3Tnc))
* Wrangler [Software](https://www.trifacta.com/start-wrangling/) (optional)
* Additional reading for the curious:
  * [Quartz Bad Data Guide](https://github.com/Quartz/bad-data-guide)
  * [Bad Data Handbook](http://proquest.safaribooksonline.com/book/databases/9781449324957/bad-data-handbook/index_html?query=((bad+data))#snippet) (O'Reilly book, free on berkeley.edu networks)
  * [Research Directions in Data Wrangling, Heer et al. 2011.](http://vis.stanford.edu/papers/data-wrangling)
  * [Quantitative Data Cleaning For Large Databases, Hellerstein 2008](https://scholar.google.com/scholar?cluster=7843444941770972724&hl=en&as_sdt=0,5)
  * [Exploratory Data Mining and Cleaning, Dasu and Johnson](https://www.amazon.com/Exploratory-Data-Mining-Cleaning/dp/0471268518) (book)

{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Exploratory Data Analysis [Nolan]
In this lecture we provide an overview of exploratory data analysis (EDA).

##### Lecture Notes 
* Slides ([pptx](https://drive.google.com/open?id=0B7gkaDYGT5X5SDd1MndCY0NZQnM), [pdf](https://drive.google.com/open?id=0B7gkaDYGT5X5X2ZKaHZtZkVWVUE), [pdf 6up](https://drive.google.com/open?id=0B7gkaDYGT5X5X2ZKaHZtZkVWVUE))
* Additional reading for the curious:
  * [Exploratory Data Analysis, Tukey 1977](https://www.amazon.com/Exploratory-Data-Analysis-John-Tukey/dp/0201076160/ref=sr_1_1?ie=UTF8&qid=1487888547&sr=8-1&keywords=exploratory+data+analysis) (book)
  * [Now You See It, Few 2009](https://www.amazon.com/Now-You-See-Visualization-Quantitative/dp/0970601980/ref=sr_1_7?ie=UTF8&qid=1487888659&sr=8-7&keywords=exploratory+data+analysis) (book)

{% include syllabus_entry end=true %}








{% include syllabus_entry dates=dates %}
### Visualization and Communication [Nolan]

This lecture covers how to effectively visualize and communicate complex results to a broader audience.

##### Lecture Notes:
* Slides ([pptx](https://drive.google.com/open?id=0B7gkaDYGT5X5LUVVa1JuM3RZeTQ), [pdf](https://drive.google.com/open?id=0Bze55lezLJhITWROdV9PNEE2RGs), [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhISVpKUU95VmFRcUU))

{% include syllabus_entry end=true %}








{% include syllabus_entry dates=dates %}
### Advanced Python Data Science Tools [Gonzalez]
In this lecture we will introduce Pandas, dataframe manipulation, python visualization, and some of the batch oriented philosophy of scalable data processing.

##### Lecture Notes:
* Summary Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIWnMzS0FuNFdqM3M), [pdf](https://drive.google.com/open?id=0Bze55lezLJhIZVVza0RUeEVsckU), [pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhISjNYRHdGOGM4YmM))
* Extended Notebook ([html](assets/notebooks/python_tools/lec7.html), [ipynb](assets/notebooks/python_tools/lec7.ipynb))


#### Homework 3 Released

#### Homework 2 Due

{% include syllabus_entry end=true %}









{% include syllabus_entry dates=dates %}
### Prediction and Inference [Yu]
In this lecture we will explore the key types and challenges of inference and predictions.  We will provide an overview of the categories of prediction problems and introduce some of the key machine learning tools in python.

#### Lecture Notes:
* Slides ([pptx](https://drive.google.com/open?id=0B9WpyRE9TsDYS0dQNmV5S2htSk0), 
[pdf](https://drive.google.com/open?id=0B9WpyRE9TsDYYlZQcEJnc0ZXb1k),
[pdf 6up](https://drive.google.com/open?id=0B9WpyRE9TsDYX0h2ZUdKd29oV28))

{% include syllabus_entry end=true %}






{% include syllabus_entry dates=dates %}

### Relational Algebra and SQL [Hellerstein]
In this lecture we introduce SQL and the relational model.


#### Lecture Notes:
* Slides ([pptx](https://drive.google.com/open?id=0B2k285AK-3KERXR0Ri1OZlR2Z0k), 
[pdf](https://drive.google.com/open?id=0B2k285AK-3KEMGFhU0NXLXhMYTQ), 
[pdf 6up](https://drive.google.com/open?id=0B2k285AK-3KEUmsyZ09LUGdDNkU)).
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### SQL Continued [Hellerstein]
In this lecture we will introduce data analysis techniques with a focus on aggregation and summary statistics.

#### Lecture Notes:
* Slides (continued from last lecture)
* Extended Notebook:  ([html no output](assets/notebooks/sql/sql_lecture_part1_without_output.html), [ipynb no output](assets/notebooks/sql/sql_lecture_part1_without_output.ipynb), [data](https://drive.google.com/open?id=0Bze55lezLJhIay1qcWp4aWJiSW8))
* Additional resources for the curious
  * CS186 Slides, 2016. [PPTX](https://www.google.com/url?q=https://drive.google.com/file/d/0B2k285AK-3KEY2w0cEwySlJxSzA/view), [PDF](https://www.google.com/url?q=https://drive.google.com/file/d/0B2k285AK-3KEX1ZhRzZmTlVBdzg/view), [Lecture Video 1](https://www.youtube.com/watch?v=4Kdpo1xim8U#t=01h03m16s), [Lecture Video 2](https://www.youtube.com/watch?v=ZZ7OwN6_s-0), [Lecture Video 3](https://www.youtube.com/watch?v=AUdts0N_5hk)
  * [PostgreSQL Manual](https://www.postgresql.org/docs/9.6/static/sql.html)
  * [SQLfiddle](http://sqlfiddle.com/)
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Advanced SQL [Hellerstein]

In this lecture we will cover SQL joins, views, and CTEs, as well as advanced aggregation including order statistics, window functions and user-defined aggregates.
* Extended Notebook:  ([html no output](assets/notebooks/sql/sql_lecture_part2_without_output.html), [ipynb no output](assets/notebooks/sql/sql_lecture_part2_without_output.ipynb))
* Gonzalez follow-up notebook ([html](assets/notebooks/sql/sql_lecture_part2-gonzalez-followup.html), [ipynb](assets/notebooks/sql/sql_lecture_part2-gonzalez-followup.ipynb))

#### Homework 4 Released

#### Homework 3 Due

{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}

### Basic Modeling using Statistical Distributions [Nolan]
In this lecture we provide an overview of several basic distributions and discuss some of the challenges of working with skewed data.

#### Lecture Notes:
* Slides ([pptx](https://drive.google.com/open?id=0B7gkaDYGT5X5Yl8wLXAzdnZ5aVE), 
[pdf](https://drive.google.com/open?id=0Bze55lezLJhIWEFiMndKRlA2SVk), 
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIb2RuS3pRRTJyRG8)).
{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Maximum Likelihood Estimation [Nolan]

In this lecture we fit basic models to data by applying the method of maximum likelihood estimation.

* Slides ([pptx](https://drive.google.com/open?id=0B7gkaDYGT5X5bnd1X2VuOWJKXzg), 
[pdf](https://drive.google.com/open?id=0B7gkaDYGT5X5Vzh6QXZHaHRzSzQ), 
[pdf 6up](https://drive.google.com/open?id=0B7gkaDYGT5X5TDYzRm5kcFE1NEk)).


{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Maximum Likelihood Estimation Continued [Nolan]

This lecture will continue discussion on the method of maximum likelihood.

* Slides ([pptx](https://drive.google.com/open?id=0B7gkaDYGT5X5UzRkTnF0YklMX0U), 
[pdf](https://drive.google.com/open?id=0B7gkaDYGT5X5dWRJWGJKZFhoVWs), 
[pdf 6up](https://drive.google.com/open?id=0B7gkaDYGT5X5bWlSdWN3NVlYQ0E)).

{% include syllabus_entry end=true %}






{% include syllabus_entry dates=dates %}
### Midterm Review [Gonzalez]
* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIVUthZ2xSblBlblk), 
[pdf](https://drive.google.com/open?id=0Bze55lezLJhIc29JMHVKb0EzZFE), 
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIRnNaam5MUkRyd28)).
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
## Midterm
This may change in the weeks before class starts as we adjust the schedule.
{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Least Squares Regression and Hypothesis Testing [Yu]
In this lecture dives into the details of least squares regression through the lens of empirical risk minimization while discussing some of the key modeling assumptions.

* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIZkVhN0ZaaU1DdUk), 
[pdf](https://drive.google.com/open?id=0Bze55lezLJhINnk3ejFzZmE2YlE), 
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIeW5OTU5tQkhZYkk)).

#### Homework 4 Due

#### Homework 5 Released

{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}

### Least Squares Regression and Hypothesis Testing [Yu]
In this lecture dives into the details of least squares regression through the lens of empirical risk minimization while discussing some of the key modeling assumptions.

* Slides ([pptx](https://drive.google.com/open?id=0Bze55lezLJhIaHRoYm51WHZqczA), 
[pdf](https://drive.google.com/open?id=0Bze55lezLJhIclZGSFpUczVMWXc), 
[pdf 6up](https://drive.google.com/open?id=0Bze55lezLJhIQWE0emd6bWh3N0k)).


{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}

### Feature Engineering, Over-fitting, and Cross Validation [Gonzalez]
In this lecture we will begin to do some machine learning.  We will explore how simple linear techniques can be used to address complex non-linear relationships on a wide range of data types.  We will start to use scikit-learn to build and visualize models in higher dimensional spaces. We will address a key challenge in machine learning -- over-fitting and discuss how cross-validation can be used to address over-fitting.

* Notebook Review of Least-Squares Linear Regression: ([html](assets/notebooks/linear_regression/Linear_Regression.html), [ipynb](assets/notebooks/linear_regression/Linear_Regression.ipynb)) this has some fun visualizations (in 3D!) as well as alternative derivations and notational clarifications.


{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}

### Regularization and the Bias Variance tradeoff [Gonzalez]

In this lecture will continue our exploration of over-fitting and derive the fundamental bias variance tradeoff for the least squares model.  We will then introduce the concept of regularization and empirical risk minimization.

{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### Spring Break
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### Spring Break
{% include syllabus_entry end=true %}



{% include syllabus_entry dates=dates %}
### Generalized Linear Model and Loss Functions [Gonzalez]

This lecture extends the earlier discussion on least squares regression to categorical data and introduce the gradient descent algorithm.

#### Homework 5 Due

#### Homework 6 Released

{% include syllabus_entry end=true %}





{% include syllabus_entry dates=dates %}
### Generalized Linear Model and Loss Functions [Gonzalez]

We continue our earlier discussion on Generalized linear models.

{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}
### Classification and Regression Trees [Nolan]

This lecture introduces an alternative approach to feature engineering using classification and regression trees (CART).

{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}

### Dimensionality Reduction [Gonzalez]

This lecture introduces the Singular Value Decomposition algorithm for dimensionality reduction.

{% include syllabus_entry end=true %}




{% include syllabus_entry dates=dates %}

### Clustering and the EM [Yu]

This lecture explores unsupervised learning techniques to aid in exploratory data analysis.  In this lecture we will cover mixture of guassians and th EM algorithm.


#### Homework 6 Due

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

#### Homework 7 Due (optional extension)

{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
### RRR Review
{% include syllabus_entry end=true %}


{% include syllabus_entry dates=dates %}
# Final Exam 

The final exam will be from 3:00 to 6:00 PM.  For details about exam scheduling visit [the Berkeley Exam Calendar](http://registrar.berkeley.edu/sis-SC-message).
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

