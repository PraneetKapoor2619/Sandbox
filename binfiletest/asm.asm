bits 16
align 16
mov bx, 0xb800
mov es, bx
xor bx, bx
mov word [es:bx], 0x0c58
retf
