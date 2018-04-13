#include<Servo.h>
Servo myservo;
void setup()  
{  
 Serial.begin(9600);  
 myservo.attach(9); 
 myservo.write(10);
 pinMode(4,OUTPUT);
 digitalWrite(4, HIGH); 
 myservo.write(0);
 delay(10000);
}  

void loop()  
{   digitalWrite(4, LOW); 
   while(Serial.available())  
   {  char c;
      c=Serial.read();
      Serial.println (c);
      if (c = 2)
        { digitalWrite(4, HIGH); 
          myservo.write(180);
         delay(40000);
         myservo.write(0);
         delay(10000);
         digitalWrite(4, LOW); 
        }
   }

}
