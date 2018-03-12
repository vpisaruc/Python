program Butolin;

{$APPTYPE CONSOLE}

uses
  Utils;

const
  MaxRow = 13;  //Максимальное количество строк матрицы W
  MaxColumn = 7;  //Максимальное количество столбцов матрицы W
  MaxElementsB = 26;  //МАксимальное количество элементов вектора B
  
var
  W:array [1..MaxRow,1..MaxColumn] of Real;  //Матрица
  D:array [1..MaxRow] of Real; 
  J,K:Integer;  //Параметры цикла
  N,M:Integer;  //Количество строк и столбцов матрицы W
  //B:array [1..MaxElementsB] of Real;
  B:array of Real;
  X:Real; //Переменная для заполнения матрицы W
  Current_Value:Real; //Текущее значение произведения элементов столбца матрицы W
  Kmax,Kmin:Integer;  //Номера столбцов с максимальным и минимальным
                      //произведением элементов стодбцов матрицы W
  Max_Value,Min_Value:Real;  //Максимальное и минимальное значения произведения
                             //столбцов матрицы W 
  
 
begin
  {Ввод количества строк в матрице W}
  X := 0.5;
  Write('Введите количество строк матрицы W от 1 до ', MaxRow,': ');
  Readln(N);
  While(N<1) or (N>MaxRow) do
    begin
      Write('Введите количество строк матрицы W от 1 до ', MaxRow,': ');
      Readln(N)
    end;
  
 {Вводи количества столбцов матрицы W}
 Write('Введите количество столбцов матрицы W от 1 до ', MaxColumn,': ');
  Readln(M);
  While(M<1) or (M>MaxColumn) do
    begin
      Write('Введите количество столбцов матрицы W от 1 до ', MaxColumn,': ');
      Readln(M)
    end;
    
  Writeln('Введите ',N,' элемента(ов) массива D в одну строку через пробел');
  For J := 1 to N do
    Read(D[J]);
  
  {Вывод введеного массива D}
  Writeln('Введённый массив D:');
  For J := 1 to N do
    Write(D[J]:7);
  Writeln();
    
  {Заполнение матрицы W}
  For J := 1 to N do
    begin
      For K := 1 to M do
        begin
          W[J,K] := cos(D[J]) * (exp(ln(X)*(1/3))); // где exp(ln(X)*(1/3)) - корень 3 степени
          X := X + 0.2;
        end;
      X := 0.5;
    end;
  
  {Вывод матрицы W}
  Writeln(' ');
  Writeln('Матрицы W:');
  For J := 1 to N do
   begin
     For K := 1 to M do
       Write(W[J,K]:7:3,' ');
     Writeln;
   end;
    
    
  {Нахождения столбцов с максимальным и минимыльным поризведением}
  Writeln(' ');
  Current_Value := 1;
  Max_Value := -99999;
  Min_Value := 99999;
  For K := 1 to M do
    begin
      For J :=1 to N do
        Current_Value := Current_Value * W[J,K]; //Подсчёт текуего значения
      if Current_Value > Max_Value then          //в столбце
        begin
          Max_Value := Current_Value;
          Kmax := K;
        end;
      if Current_Value < Min_Value then
        begin
          Min_Value := Current_Value;
          Kmin := K;
        end;
      Writeln(Current_Value:7:4,' - Значение произведения элементов для столбца ',K );
      Current_Value := 1;
    end;
    
   Writeln(' ');
   Writeln(Kmin,' - номер столбца с минимальным произведением');
   Writeln(Kmax,' - номер столбца с максимальным произведением');
   Writeln(' ');
        
  {Формирование вектора B}
  SetLength(B,0);
  
  For K := 1 to M do
    For J := 1 to N do
      if K=Kmin then
        begin
          SetLength(B,Length(B)+1); //Добавление в вектор B 
          B[High(B)] := W[J,K];     //новых ячеек (динамический массив)
        end;                        //из столбца с мин. произведением
          
  For K := 1 to M do
    For J := 1 to N do
      if K=Kmax then
        begin
          SetLength(B,Length(B)+1);  //Добавление в вектор B
          B[High(B)] := W[J,K];      //новых ячеек (динамический массив)
        end;                         //из столбца с макс. произведением
          
  {Вывод вектора B}
  Writeln('Вектор B: ');
  For J := 0 to High(B) do
    Write(B[J]:7:3);
 
 end.