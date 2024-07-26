from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
   
class Coginzant(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text

class TCS(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Amazon(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Capgemini(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text


class Delloite(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text

class IBM(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Accenture(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Microsoft(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Atos(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text



class Netflix(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class Facebook(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text


class Apple(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text


class Google(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class Infosys(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class TM(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class Wipro(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class Adobe(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class Cisco(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class EY(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text
    
class PWC(models.Model):
    question_text = models.TextField(null=True)
    input_format = models.TextField(null=True)
    output_format = models.TextField(null=True)
    correct_ans = models.TextField(null=True)

    def __str__(self):
        return self.question_text