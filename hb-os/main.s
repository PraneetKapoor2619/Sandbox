section .data
	vga_start equ 0x0b8000
	vga_end equ 0x0c0000
	vga_col equ 0x50	;total number of columns is (80)10 = 0x50
	vga_row equ 0x19	;total number of rows is (25)10 = 0x19
	
	;(row), (column)
	vga_ptr dd 0x00, 0x00
	
	;(string base address), (length)
	str_ptr dd 0x00, 0x00
	
	;string and its length
	string1 db "Hello world!!"
	len1 equ $ - string1

section .text
bits 32
global start
start:
	; print `OK`
	call clear_screen
	;print the string
	mov eax, string1
	mov ecx, len1
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
	mov dword [vga_ptr], 0x00
	ret

;SUB: write_screen
;PURPOSE: write a string to the screen
printf:
	mov dword [str_ptr], eax
	mov dword [str_ptr + 4], ecx

.1:	;Calculation of effective address
	;The formula is: 
	;[row][col] = (base_address + 0x50 * row + 0x02 * col)
	;if the number of columns is 80, then increment row ptr
	mov ebx, vga_start
	mov eax, dword [vga_ptr + 4]
	mov ecx, 0x02
	mov edx, 0x00
	mul ecx
	cmp eax, 0xa0
	je .2
	jl .3

.2:	;incase of col > 80, set col = 0 and increment row pointer	
	inc dword [vga_ptr]
	mov dword [vga_ptr + 4], 0x00
	mov eax, 0x00

.3:	
	inc dword [vga_ptr + 4]
	push eax
	mov eax, dword [vga_ptr]
	mov ecx, vga_row
	mov edx, 0x00
	mul ecx
	add ebx, eax
	pop eax
	add ebx, eax

.4:	;with the effective address now available, we now have to print the string
	mov dh, 0x0f
	mov eax, dword [str_ptr]
	mov dl, byte [eax]
	mov word [ebx], dx
	inc dword [str_ptr]
	dec dword [str_ptr + 4]
	cmp dword [str_ptr + 4], 0x00
	jg .1
	ret
