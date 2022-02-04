section .data
	vga_start equ 0x0b8000
	vga_end equ 0x0c0000
	vga_ptr dd 0x0b8000

section .text
bits 32
global start
start:
	; print `OK`
	mov dword [0xb8000], 0x2f4b2f4f
	;call clear_screen
	;string and its length
	string db "Hello, world!!", 0x0a
	len equ $ - string
	;print the string
	;call printf
	hlt

;SUB: clear_screen 
;PURPOSE: Used for clearing the 16-bit VGA buffer
clear_screen:
	mov dword [vga_ptr], vga_start
	mov ebx, dword [vga_ptr]
clrs_1:
	;operation start
	mov word [ebx], 0x0000
	;operation end
	add ebx, 0x02
	cmp ebx, vga_end
	jb clrs_1
	ret

;SUB: write_screen
;PURPOSE: write a string to the screen
printf:
	mov eax, len
	mov ecx, 0x00
	mov ebx, dword [vga_ptr]
printf_1:
	;operation start
	mov dl, byte [string + ecx]
	mov dh, 0x0f
	mov word [ebx], dx
	add ebx, 0x02
	;operation end
	inc ecx
	cmp eax, ecx
	jne printf_1
	je printf_2
printf_2:
	mov dword [vga_ptr], ebx
	ret