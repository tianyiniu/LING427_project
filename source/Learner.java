/* This is the new unambitious and apprehensive learner.Instead of trying to jump immediately to the most general hypothesis,it takes the cautious approach and only generalizes by tiny shuffles.*/import java.awt.*;import java.io.*;import java.util.*;public class Learner{ 	public Learner()	{  		try {			LearnerFrame learnerframe = new LearnerFrame();			learnerframe.initComponents();			learnerframe.setVisible(true);		}		catch (Exception e) {				e.printStackTrace();		}		} 	static public void main(String[] args) 	{		new Learner();	} } 