section .data
	vga_start equ 0x0b8000
	vga_end equ 0x0c0000
	vga_col equ 0x50
	vga_ptr dd 0x0b8000
	;string and its length
	string1 db "Hello world!!", 0x0a
	len1 equ $ - string1
	string2 db "This is P.K.'s Personal Operating System!!", 0x0a, 0x0a
	len2 equ $ - string2
	string3 db "Welcome, children!!", 0x0a
	len3 equ $ - string3

section .text
bits 32
global start
start:
	; print `OK`
	call clear_screen
	;print the string
	mov eax, len1
	mov ecx, string1
	call printf
	mov eax, len2
	mov ecx, string2
	call printf
	mov eax, len3
	mov ecx, string3
	call printf
	hlt

;SUB: clear_screen 
;PURPOSE: Used for clearing the 16-bit VGA buffer
clear_screen:
	mov dword [vga_ptr], vga_start
	mov ebx, dword [vga_ptr]
.1:
	;operation start
	mov word [ebx], 0x0000
	;operation end
	add ebx, 0x02
	cmp ebx, vga_end
	jb .1
	ret

;SUB: write_screen
;PURPOSE: write a string to the screen
printf:
	add eax, ecx
	mov ebx, dword [vga_ptr]
.1:	;operation start
	cmp byte [ecx], 0x0a
	je .3
	mov dl, byte [ecx]
	mov dh, 0x0f
	mov word [ebx], dx
	;operation end
.2	add ebx, 0x02
	inc ecx
	cmp eax, ecx
	jne .1
	mov dword [vga_ptr], ebx
	ret
	
.3:
	mov dl, 0x00
	mov dh, 0x0f
	mov word [ebx], dx
	push eax
	mov eax, ebx
	sub eax, vga_start		;total columns = vga_ptr - vga_start
	push ebx
	mov edx, 0x00
	mov ebx, 0x02			;because 1 column = (character + bgfg)
	div ebx				;eax = total columns
	mov edx, 0x00
	mov ebx, vga_col
	div ebx				;divide total col by no. of col
	pop ebx
	pop eax
	cmp edx, 0x00			;if total col % 0x50, then edx = 0x00
	je .4				;first fix the ptr
	add ebx, 0x02
	jmp .3				;check again
.4:	sub ebx, 0x02
	jmp .2				;now return to print the rest of string