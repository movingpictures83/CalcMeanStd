import sys
import math

class CalcMeanStdPlugin:
   def input(self, inputfile):
      infile = inputfile
      noafile = open(infile, 'r')

      count = 0
      self.scores = []
      for line in noafile:
         if count == 0:
            count = 1
            pass
         else: 
            vals = line.split('\t')
            self.scores.append(float(vals[1]))
      
   def run(self):
      sum = 0
      for score in self.scores:
         sum += score
      self.mean = sum / len(self.scores)

      sum = 0
      for score in self.scores:
         sum += (abs(score - self.mean))**2
      self.std = math.sqrt(sum / len(self.scores))


   def output(self, outputfile):
      print ("[CalcMeanStdPlugin] Two left:  "+str(self.mean - 2*self.std))
      print ("[CalcMeanStdPlugin] One left:  "+str(self.mean - self.std))
      print ("[CalcMeanStdPlugin] Mean:  "+str(self.mean))
      print ("[CalcMeanStdPlugin] One right:  "+str(self.mean + self.std))
      print ("[CalcMeanStdPlugin] Two right:  "+str(self.mean + 2*self.std))
