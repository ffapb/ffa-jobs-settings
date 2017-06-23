from __future__ import unicode_literals


from django.core.management.base import BaseCommand, CommandError

# import additional classes/modules as needed
from ...models import Job, Email
from django.db.models.query_utils import DeferredAttribute, RegisterLookupMixin
from django.utils.encoding import (
    force_bytes, force_text, python_2_unicode_compatible, smart_text,
)



class Command(BaseCommand):
    args = '<job>'
    help = 'My custom django management command'

    def add_arguments(self, parser):
       parser.add_argument('job', nargs='+', type=str)
       
     
          # Your code goes here
        
  
    def handle(self,*args, **options):

        
          try:
            job = str(args[0])
            emails = Email.objects.get(pk=job)
          except:
            emails = Email.objects.all()
            print "bla bla"
          for email in emails:
            self.stdout.write(email.email_text)
           

            
	



        #emails = Email.objects.filter(job=self.job)
        #for email in emails:
            #print email 


       #to print all emails and fixed the issue below
        #for email in Email.objects.all():
            #print (email.email_text) 
        
      #code to print emails regarding the static Job
        #emails = Email.objects.all()
        #email1=[Email.email_text for email in emails if Email.job=='Debitors notice - LB']
	#email1=[Email for email in Email.objects.all() if Email.job==job]
        #print emails

	
	#<QuerySet [<Email: m.moawad@ffaprivatebank.com>, <Email: s.akiki@ffaprivatebank.com>, <Email: s.akiki@ffaprivatebank.com")>, <Email: m.moawad@ffaprivatebank.com>, <Email: T.Aoun@ffaprivatebank.com>, <Email: E.Rizk@ffaprivatebank.com>, <Email: broker>, <Email: s.akiki@ffaprivatebank.com>, <Email: ##m.moawad@ffaprivatebank.com>, <Email: #T.Aoun@ffaprivatebank.com>, <Ema

       # code to print emails regarding the static id

	#emails = Email.objects.filter(job='40')
        #for email in emails:
            #print email 



#for email_id in options['email_id']:
            #try:
                #email = Email.objects.filter(pk="email_id")
            #except Email.DoesNotExist:
                #raise CommandError('email "%s" does not exist' % email_id)

            #self.stdout.write('Successfully "%s"' % email_text)
