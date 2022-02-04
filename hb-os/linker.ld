ENTRY(start)

SECTIONS
{
	. = 1M;

	.boot :
	{
		KEEP(*(.multiboot_header))
	}
	
	.data :
	{
		*(.data)
	}

	.text :
	{
		*(.text)
	}
}