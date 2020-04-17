.text

###
### ### ECE350: Processor Checkpoint
### ### Basic Compare Test
### ### MIPS
###

add     $r0, $r0, $r0
add     $r0, $r0, $r0
add     $r0, $r0, $r0

addi    $r1, $r1, 40
addi    $r2, $r2, 50
addi    $r3, $r3, 60
addi    $r4, $r4, 70
addi    $r5, $r5, 80
bne     $r1, $r2, c1

bne     $r1, $r0, -1    # halt

c1:
addi    $r10, $r10, 200
blt     $r1, $r2, c2

bne     $r1, $r0, -1    # halt

c2:
addi    $r10, $r10, 200
