.text

###
### ### ECE350: Processor Checkpoint
### ### Basic Misc. Test
### ### MIPS
###

add     $r0, $r0, $r0
add     $r0, $r0, $r0
add     $r0, $r0, $r0

addi    $r1, $r1, 10
addi    $r2, $r2, 6
addi    $r3, $r3, 12
addi    $r4, $r4, -5

and     $r5, $r1, $r2
or      $r6, $r2, $r3

blt     $r1, $r2, c1
j       c2

c1:
addi    $r7, $r7, 200
bne     $r1, $r0, -1    # halt

c2:
addi    $r7, $r7, 300
bne     $r1, $r0, -1    # halt
