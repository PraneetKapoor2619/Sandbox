source_files := $(wildcard *.s)
object_files := $(patsubst %.s, %.o, $(source_files))

all: $(object_files)
	clear
	x86_64-elf-ld -n -T linker.ld $(object_files) -o kernel.bin
	mkdir -p isodir/boot/grub
	cp -p kernel.bin isodir/boot/
	cp -p grub.cfg isodir/boot/grub/grub.cfg
	grub-mkrescue isodir -o kernel.iso

$(object_files): $(source_files)
	$(foreach file, $(source_files), nasm -f elf64 $(file) -o $(patsubst %.s,%.o, $(file));)