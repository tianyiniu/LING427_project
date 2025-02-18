*********************Readme File for the Rule-based Learner*********************

This file contains the java executable for the rule-based learner.
It can be downloaded from:
http://www.linguistics.ucla.edu/people/hayes/RulesVsAnalogy/index.htm


What you need to run the Learner:
* LearnerShell.zip file, in this archive
   (NOTE: YOU DO NOT NEED TO UNZIP THIS FILE IN ORDER TO RUN IT!)
* Java Runtime Environment (JRE)
  (available for Unix/Windows from www.java.com or from IBM (www.ibm.com)
   for Mac from www.apple.com -- I personally recommend the IBM runtime 
   environment for Windows, and using MacOS 10.1 for the Mac)
* input files (see below)

********************************************************************************
Launching the application:

The program is a Java application, so you need to run it in the JRE (not 
from a browser or applet runner).  All the necessary classes are bundled 
into the file: RuleBasedLearnerProgram.jar
The main class file is called: Learner
On my system, using the IBM JRE, I run it by typing:

jre -cp RuleBasedLearnerProgram.jar -ms150M -mx250M Learner

(See your runtime documentation for info on how to run an application -- I 
have included a .bat file for issuing the correct command for the IBM 
runtime environment; you might need to substitute 'java' for 'jre', and 
'-classpath' for '-cp'.  The -ms and -mx flag specify the amount of memory 
allotted to the java runtime environment; I have a lot of memory, so I give 
it between 150 and 250 megs.  You will need to allocate less if 
you don't have this much memory!)

********************************************************************************
Loading an input file:

When you launch the application an untitled Learner window appears.  To 
load an input file, click the button on the right labeled "Open input 
file..."  Use the open dialog to select a .in file 

For replicating the English past tense simulations in "Rules vs. Analogy in 
English Past Tenses: A Computational/Experimental Study", you can download 
the input files from: 
http://www.linguistics.ucla.edu/people/hayes/RulesVsAnalogy/index.html

********************************************************************************
Structure of the input file:

Input files for the Learner have a relatively simple structure, but there 
is also some fixed material which the program uses to make sure that it is 
reading the correct material into the correct variables.  (I have been 
Considering ways to simplify this, possibly leaving out all information 
except for the input forms, test forms, and illegal sequences)  You should 
edit input files using your favorite text editor.
The following shows a sample input file (included as samplefile.in); the 
lines which should be changed are marked with an asterisk, while lines 
which should NOT be changed are indicated to the left with a @: 

@	Phonological Learner File
	[file creator] (*)
	[language] (*)
(@)	Thu Sep 04 16:03:36  1997 [creation date] (*)
(@)	Thu Sep 04 16:03:36  1997 [modified date] (*)
	[Notes: this is a language.]  (*)
@	Morphological categories:
		[category1]	[category2] (*)
@	Input forms:
	[input1]	[output1] 	[optional token freq1]	(*)
	[input2]	[output2] 	[optional token freq2]	(*)
	etc. (*)
	etc. (*)
	etc. (*)
@	Test forms:
	[testinput1] (*)
	[testinput2] (*)
	etc. (*)
@	Illicit sequences:
	[illegal seq 1] (*)
	[illegal seq 2] (*)
	etc... (*)
@	end

(The dates may be modified, but are not important to anything, so it is 
probably easier to leave them alone)  Token frequencies are optional, but 
are of course required if you want the Learner to output comparison ratings 
using token-frequency based measures.

********************************************************************************
Loading a features file:

The features file (.fea) is automatically loaded at the same time as the 
input file.  The features file must have the same filename as the input 
file -- so if you have a blah.in file, you should also have a blah.fea file 
for the features.
The best way to see the structure of the features file is to open up one 
of the samples.  (Excel is a good program for doing this, since the file 
is tab-delimited)

********************************************************************************
Running the Learner:

To start the Learner, simply click on the "Learn Phonology..." button.  
There are a number of options which you can toggle using the check boxes 
in the lower half of the window.  These control what kinds of criteria the 
Learner will use when outputting novel forms.  By default, the Learner 
always outputs a file using reliability, adjusted using the 75% lower 
confidence limit, and employing the "impugnment" algorithm.
(When multiple boxes are selected, the Learner outputs multiple files, 
so you can compare the results using various criteria)
The options are:

* Save .con file: when checked, the Learner saves the entire mapping 
constraints file which it learns.  (These files can be huge and 
time-consuming to save, and at the moment are not terribly useful except 
on small files -- there is actually a small program to convert them to 
tab-delimited text files which can be read in Excel, contact me if you are 
interested in this)
* Unimpugned c75: uses reliability statistics corrected using lower 
confidence limits at a 75% confidence level.  the "impugning" algorithm is 
not employed.
* Unimpugned c90: same as Unimpugned c75, but with a 90% confidence level
* Raw reliability: not adjusted using confidence limits
* Type frequency: rates outputs based solely on type frequency (="hits") 
of related forms
* Weighted by length: adjusts values to reward using more specific 
neighborhoods, by multiplying the reliability by a factor of 1.2^n, where n 
is the number of segments in the string description of the neighborhood.
* Token frequency: rates outputs based on token frequency of related words, 
and also by a relative measure using the c75 of "hits tokens/scope tokens"
* Weighted by token freq: output based on type reliability X token 
reliability
********************************************************************************

Other options related to the operations of the Learner:

* Use Doppelg�ngers: the Learner explores the same neighborhoods for all 
structural changes
* Use Impugnment: the "impugnment" algorithm is employed to detect when a 
generalization is taking credit for work really done by one its subsets
* Use Phonology: the learner uses the illegal sequences to attempt to 
discover simple phonological rules, possibly improving the performance of 
some affixes
* Use Features: the features term in the structural description is allowed
* Intermediate Wug Testing: the Learner tries the Wug test forms at a 
variety of intermediate stages in the learning process.  (This is used to 
simulate a childhood -- it only works if the input forms are in some 
reasonable order to make the stages actually resemble stages in what a 
child knows!)
* Wug-time learning: the Wug test forms are treated as if they were 
learning data, and may spawn further generalization.  (The generalizations 
from a wug form are purged after that form has been considered)

********************************************************************************
Warnings:

* Excel can be very handy for importing input paradigms into a .in file, 
but it also creates a small problem when you save the file as text: it adds 
extra tabs after some lines (crucially, it often adds them after the lines 
which should not be modified, like "Input forms:", etc.)  If the Learner 
complains that no input forms or test forms were found, the lines which 
flagged those sections probably got mangled somehow.
* The Learner currently can not handle more than two morphological 
categories at a time
* Java is supposedly smart about different kinds of text files on 
different platforms.  However, I have found that it can actually be sort of 
finicky about this, and sometimes it refuses to read a text file for no 
apparent reason.  If you are trying to create input files and are having 
problems with this, contact me and I might have some suggestions.
* The Learner does output some information while it is running, so you can 
see that it is doing things.  However, I have noticed that at least in 
Windows95 and beyond, the scrolling of the Java console is screwed up and 
this is not as informative as it could be.
* The interface for the Learner is not as polished as it could be; in 
particular, you may run into troubles if you try running multiple 
simulations without quitting in between, or things like that.  (This might 
work OK, though -- I just haven't tested these things much)

For further information on how the Learner works, see:

Albright, Adam and Bruce Hayes (1998) An Automated Learner for Phonology 
    and Morphology.   UCLA ms., available at 
    http://www.humnet.ucla.edu/humnet/linguistics/people/hayes/learning/learning.htm/
    
Albright, Adam and Bruce Hayes (1999) "Burnt and "Splang":  Some Issues 
    in Morphological Learning Theory," talk presented at MIT, Cornell, 
    University of Rochester, and USC.  
    (Handout available at same location)

If you have questions or problems trying to make this program run, contact 
Adam Albright at:  aalbrigh@ucla.edu

********************************************************************************

Created 10/17/01 by Adam Albright
For additional questions and information, contact me: aalbrigh@ucla.edu