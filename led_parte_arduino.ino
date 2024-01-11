const int led = 13;
int valor_dato = 0;

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("Conexión Establecida");
}

void loop(){
  
  while(Serial.available())
  {
    valor_dato = Serial.read();
  }
  
  if (valor_dato == '1')
  {
    digitalWrite (led, HIGH);
  }
  else if (valor_dato == '0')
  {
    digitalWrite (led, LOW);
  }
}