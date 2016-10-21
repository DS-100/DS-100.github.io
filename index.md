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


* **Prepare** students for advanced Berkeley courses in data-management ([CS186](http://www.cs186berkeley.net)), machine learning [CS189](https://people.eecs.berkeley.edu/~jrs/189/)), and statistics ([Stat-154](http://www.stat.berkeley.edu/~rabbee/s154/)), by providing the necessary foundation and context

* **Enable** students to start careers as data scientists by providing the necessary experience on real-world data, tools, and techniques

* **Empower** student to apply computational and inferential thinking to tackle  real-world problems




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
      <img src="http://www.stat.berkeley.edu/~nolan/images/Deb-Nolan.jpg" alt="Deborah Nolan" style="height: 150px;"/>
      <address>
        <strong>Deborah Nolan</strong><br>
        <script type="text/javascript"> email_address("stat.", "nolan") </script>
      </address>
    </div></div>
    <div class="col-sm-3"><div class="text-center">
      <img src="https://www.stat.berkeley.edu/~binyu/Site/Welcome_files/Yu_Bin13.jpg" alt="Bin Yu" style="height: 150px;"/>
      <address>
        <strong>Bin Yu</strong><br>
        <script type="text/javascript"> email_address("stat.", "binyu") </script>
      </address>
    </div></div>
  </div>
</div>



