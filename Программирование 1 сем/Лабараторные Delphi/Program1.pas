program Butolin;

{$APPTYPE CONSOLE}

uses
  Utils;

const
  MaxRow = 13;  //������������ ���������� ����� ������� W
  MaxColumn = 7;  //������������ ���������� �������� ������� W
  MaxElementsB = 26;  //������������ ���������� ��������� ������� B
  
var
  W:array [1..MaxRow,1..MaxColumn] of Real;  //�������
  D:array [1..MaxRow] of Real; 
  J,K:Integer;  //��������� �����
  N,M:Integer;  //���������� ����� � �������� ������� W
  //B:array [1..MaxElementsB] of Real;
  B:array of Real;
  X:Real; //���������� ��� ���������� ������� W
  Current_Value:Real; //������� �������� ������������ ��������� ������� ������� W
  Kmax,Kmin:Integer;  //������ �������� � ������������ � �����������
                      //������������� ��������� �������� ������� W
  Max_Value,Min_Value:Real;  //������������ � ����������� �������� ������������
                             //�������� ������� W 
  
 
begin
  {���� ���������� ����� � ������� W}
  X := 0.5;
  Write('������� ���������� ����� ������� W �� 1 �� ', MaxRow,': ');
  Readln(N);
  While(N<1) or (N>MaxRow) do
    begin
      Write('������� ���������� ����� ������� W �� 1 �� ', MaxRow,': ');
      Readln(N)
    end;
  
 {����� ���������� �������� ������� W}
 Write('������� ���������� �������� ������� W �� 1 �� ', MaxColumn,': ');
  Readln(M);
  While(M<1) or (M>MaxColumn) do
    begin
      Write('������� ���������� �������� ������� W �� 1 �� ', MaxColumn,': ');
      Readln(M)
    end;
    
  Writeln('������� ',N,' ��������(��) ������� D � ���� ������ ����� ������');
  For J := 1 to N do
    Read(D[J]);
  
  {����� ��������� ������� D}
  Writeln('�������� ������ D:');
  For J := 1 to N do
    Write(D[J]:7);
  Writeln();
    
  {���������� ������� W}
  For J := 1 to N do
    begin
      For K := 1 to M do
        begin
          W[J,K] := cos(D[J]) * (exp(ln(X)*(1/3))); // ��� exp(ln(X)*(1/3)) - ������ 3 �������
          X := X + 0.2;
        end;
      X := 0.5;
    end;
  
  {����� ������� W}
  Writeln(' ');
  Writeln('������� W:');
  For J := 1 to N do
   begin
     For K := 1 to M do
       Write(W[J,K]:7:3,' ');
     Writeln;
   end;
    
    
  {���������� �������� � ������������ � ����������� �������������}
  Writeln(' ');
  Current_Value := 1;
  Max_Value := -99999;
  Min_Value := 99999;
  For K := 1 to M do
    begin
      For J :=1 to N do
        Current_Value := Current_Value * W[J,K]; //������� ������� ��������
      if Current_Value > Max_Value then          //� �������
        begin
          Max_Value := Current_Value;
          Kmax := K;
        end;
      if Current_Value < Min_Value then
        begin
          Min_Value := Current_Value;
          Kmin := K;
        end;
      Writeln(Current_Value:7:4,' - �������� ������������ ��������� ��� ������� ',K );
      Current_Value := 1;
    end;
    
   Writeln(' ');
   Writeln(Kmin,' - ����� ������� � ����������� �������������');
   Writeln(Kmax,' - ����� ������� � ������������ �������������');
   Writeln(' ');
        
  {������������ ������� B}
  SetLength(B,0);
  
  For K := 1 to M do
    For J := 1 to N do
      if K=Kmin then
        begin
          SetLength(B,Length(B)+1); //���������� � ������ B 
          B[High(B)] := W[J,K];     //����� ����� (������������ ������)
        end;                        //�� ������� � ���. �������������
          
  For K := 1 to M do
    For J := 1 to N do
      if K=Kmax then
        begin
          SetLength(B,Length(B)+1);  //���������� � ������ B
          B[High(B)] := W[J,K];      //����� ����� (������������ ������)
        end;                         //�� ������� � ����. �������������
          
  {����� ������� B}
  Writeln('������ B: ');
  For J := 0 to High(B) do
    Write(B[J]:7:3);
 
 end.