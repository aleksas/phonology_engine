#ifndef TRANSCRIBE_RULES_H
#define TRANSCRIBE_RULES_H

const char * transcribeRules[] = {
    "IJ A * * 2 3 3 3 E 1 10 ",
    "IJ A * * 4 3 3 3 Ea 1 9 ",
    "IJ A * * 8 3 3 3 eA 1 8 ",
    "IJ A * * 16 3 3 1 E 1 7 ",
    "IJ A * * 17 3 3 3 e 1 6 ",
    "*  A * * 2 3 3 7 A 1 5 ",
    "*  A * * 4 3 3 7 Aa 1 4 ",
    "*  A * * 8 3 3 7 aA 1 3 ",
    "*  A * * 16 3 3 5 A 1 2 ",
    "*  A * * 17 3 3 7 a 1 1 ",

    "IJ � * * 4 3 3 3 Ea 1 6 ",
    "IJ � * * 8 3 3 3 eA 1 5 ",
    "IJ � * * 17 3 3 3 ea 1 4 ",
    "*  � * * 4 3 3 7 Aa 1 3 ",
    "*  � * * 8 3 3 7 aA 1 2 ",
    "*  � * * 19 3 3 7 aa 1 1 ",

    "* E * * 2 3 3 7 E 1 5 ",
    "* E * * 4 3 3 7 Ea 1 4 ",
    "* E * * 8 3 3 7 eA 1 3 ",
    "* E * * 16 3 3 5 E 1 2 ",
    "* E * * 17 3 3 7 e 1 1 ",

    "* � * * 4 3 3 7 Ea 1 3 ",
    "* � * * 8 3 3 7 eA 1 2 ",
    "* � * * 19 3 3 7 ea 1 1 ",

    "* � * * 4 3 3 7 Ee 1 3 ",
    "* � * * 8 3 3 7 eE 1 2 ",
    "* � * * 19 3 3 7 ee 1 1 ",

    "AEU I * * 8 3 3 3 J 1 15 ",
    "AEOU I * * 23 3 3 3 j 1 14 ",
    "* I A�OU�� * 31 3 3 5 * 1 13 ",
    "* I E * 4 3 3 4 j' 0 1 ",
    "* I E * 4 3 3 4 Ie 2 11 ",
    "* I E * 16 3 3 4 j' 0 1 ",
    "* I E * 16 3 3 4 iE 2 9 ",
    "* I E * 1 3 3 4 j' 0 1 ",
    "* I E * 1 3 3 4 ie 2 7 ",
    "* I E * 4 3 3 1 Ie 2 6 ",
    "* I E * 16 3 3 1 iE 2 5 ",
    "* I E * 1 3 3 1 ie 2 4 ",
    "* I * * 6 3 3 7 I 1 3 ",
    "* I * * 16 3 3 5 I 1 2 ",
    "* I * * 25 3 3 7 i 1 1 ",

    "* Y * * 4 3 3 7 Ii 1 3 ",
    "* Y * * 8 3 3 7 iI 1 2 ",
    "* Y * * 19 3 3 7 ii 1 1 ",

    "* � * * 4 3 3 7 Ii 1 3 ",
    "* � * * 8 3 3 7 iI 1 2 ",
    "* � * * 19 3 3 7 ii 1 1 ",

    "* O * * 4 7 3 5 O 1 6 ",
    "* O * * 4 3 3 7 Oo 1 5 ",
    "* O * * 8 3 3 7 oO 1 4 ",
    "* O * * 2 3 3 7 O 1 3 ",
    "* O * * 17 7 3 7 o 1 2 ",
    "* O * * 17 3 3 7 oo 1 1 ",

    "AEO U * * 8 3 3 3 W 1 8 ",
    "AEO U * * 23 3 3 3 w 1 7 ",
    "* U O * 4 3 3 5 Uo 2 6 ",
    "* U O * 16 3 3 5 uO 2 5 ",
    "* U O * 1 3 3 5 uo 2 4 ",
    "* U * * 6 3 3 7 U 1 3 ",
    "* U * * 16 3 3 5 U 1 2 ",
    "* U * * 25 3 3 7 u 1 1 ",

    "* � * * 4 3 3 7 Uu 1 3 ",
    "* � * * 8 3 3 7 uU 1 2 ",
    "* � * * 19 3 3 7 uu 1 1 ",

    "* � * * 4 3 3 7 Uu 1 3 ",
    "* � * * 8 3 3 7 uU 1 2 ",
    "* � * * 19 3 3 7 uu 1 1 ",

    "* B PB * 31 3 3 7 * 1 5 ",
    "* B * * 31 2 2 7 p 1 4 ",
    "* B * * 31 1 2 7 p' 1 3 ",
    "* B * * 31 2 1 7 b 1 2 ",
    "* B * * 31 1 1 7 b' 1 1 ",

    "* C H * 31 3 3 5 *  1 5 ",
    "* C * * 31 2 1 7 dz 1 4 ",
    "* C * * 31 1 1 7 dz' 1 3 ",
    "* C * * 31 2 2 7 ts 1 2 ",
    "* C * * 31 1 2 7 ts' 1 1 ",

    "* � * * 31 2 1 7 dZ 1 4 ",
    "* � * * 31 1 1 7 dZ' 1 3 ",
    "* � * * 31 2 2 7 tS 1 2 ",
    "* � * * 31 1 2 7 tS' 1 1 ",

    "* D TD * 31 3 3 7 * 1 15 ",
    "N D PBKG * 31 3 3 7 * 1 14 ",
    "MN D S�Z� * 31 3 3 3 * 1 13 ",
    "* D SZ * 31 2 2 7 ts 2 12 ",
    "* D SZ * 31 1 2 7 ts' 2 11 ",
    "* D SZ * 31 2 1 7 dz 2 10 ",
    "* D SZ * 31 1 1 7 dz' 2 9 ",
    "* D �� * 31 2 2 7 tS 2 8 ",
    "* D �� * 31 1 2 7 tS' 2 7 ",
    "* D �� * 31 2 1 7 dZ 2 6 ",
    "* D �� * 31 1 1 7 dZ' 2 5 ",
    "* D * * 31 2 2 7 t 1 4 ",
    "* D * * 31 1 2 7 t' 1 3 ",
    "* D * * 31 2 1 7 d 1 2 ",
    "* D * * 31 1 1 7 d' 1 1 ",

    "* F * * 31 2 3 7 f 1 2 ",
    "* F * * 31 1 3 7 f' 1 1 ",

    "* G KG * 31 3 3 7 * 1 5 ",
    "* G * * 31 2 2 7 k 1 4 ",
    "* G * * 31 1 2 7 k' 1 3 ",
    "* G * * 31 2 1 7 g 1 2 ",
    "* G * * 31 1 1 7 g' 1 1 ",

    "C H * * 31 2 3 3 x 1 4 ",
    "C H * * 31 1 3 3 x' 1 3 ",
    "* H * * 31 2 3 7 h 1 2 ",
    "* H * * 31 1 3 7 h' 1 1 ",

    "A�E��IY�OU�� J * * 31 3 3 3 j 1 2 ",
    "* J * * 31 3 3 7 j' 1 1 ",

    "* K KG * 31 3 3 7 * 1 5 ",
    "* K * * 31 2 1 7 g 1 4 ",
    "* K * * 31 1 1 7 g' 1 3 ",
    "* K * * 31 2 2 7 k 1 2 ",
    "* K * * 31 1 2 7 k' 1 1 ",

    "* L * * 8 2 3 3 L 1 4 ",
    "* L * * 8 1 3 3 L' 1 3 ",
    "* L * * 31 2 3 7 l 1 2 ",
    "* L * * 31 1 3 7 l' 1 1 ",

    "* M * * 8 2 3 3 M 1 4 ",
    "* M * * 8 1 3 3 M' 1 3 ",
    "* M * * 31 2 3 7 m 1 2 ",
    "* M * * 31 1 3 7 m' 1 1 ",

    "* N * * 8 2 3 3 N 1 4 ",
    "* N * * 8 1 3 3 N' 1 3 ",
    "* N * * 31 2 3 7 n 1 2 ",
    "* N * * 31 1 3 7 n' 1 1 ",

    "* P PB * 31 3 3 7 * 1 5 ",
    "* P * * 31 2 1 7 b 1 4 ",
    "* P * * 31 1 1 7 b' 1 3 ",
    "* P * * 31 2 2 7 p 1 2 ",
    "* P * * 31 1 2 7 p' 1 1 ",

    "* R * * 8 2 3 3 R 1 4 ",
    "* R * * 8 1 3 3 R' 1 3 ",
    "* R * * 31 2 3 7 r 1 2 ",
    "* R * * 31 1 3 7 r' 1 1 ",

    "* S � * 31 2 2 7 S 1 12 ",
    "* S � * 31 1 2 7 S' 1 11 ",
    "* S � * 31 2 1 7 Z 1 10 ",
    "* S � * 31 1 1 7 Z' 1 9 ",
    "* S � * 31 2 2 7 S 1 8 ",
    "* S � * 31 1 2 7 S' 1 7 ",
    "* S D � 31 2 1 7 Z 1 6 ",
    "* S D � 31 1 1 7 Z' 1 5 ",
    "* S * *  31 2 1 7 z 1 4 ",
    "* S * *  31 1 1 7 z' 1 3 ",
    "* S * *  31 2 2 7 s 1 2 ",
    "* S * *  31 1 2 7 s' 1 1 ",

    "* � SZ * 31 2 2 8 S 1 12 ",
    "* � SZ * 31 1 2 8 S' 1 11 ",
    "* � SZ * 31 2 1 8 Z 1 10 ",
    "* � SZ * 31 1 1 8 Z' 1 9 ",
    "* � SZ * 31 2 2 7 s 1 8 ",
    "* � SZ * 31 1 2 7 s' 1 7 ",
    "* � SZ * 31 2 1 7 z 1 6 ",
    "* � SZ * 31 1 1 7 z' 1 5 ",
    "* � * * 31 2 1 7 Z 1 4 ",
    "* � * * 31 1 1 7 Z' 1 3 ",
    "* � * * 31 2 2 7 S 1 2 ",
    "* � * * 31 1 2 7 S' 1 1 ",

    "* T TD * 31 3 3 7 * 1 15 ",
    "N T PBKG * 31 3 3 7 * 1 14 ",
    "MN T S�Z� * 31 3 3 7 * 1 13 ",
    "* T SZ * 31 2 2 7 ts 2 12 ",
    "* T SZ * 31 1 2 7 ts' 2 11 ",
    "* T SZ * 31 2 1 7 dz 2 10 ",
    "* T SZ * 31 1 1 7 dz' 2 9 ",
    "* T �� * 31 2 2 7 tS 2 8 ",
    "* T �� * 31 1 2 7 tS' 2 7 ",
    "* T �� * 31 2 1 7 dZ 2 6 ",
    "* T �� * 31 1 1 7 dZ' 2 5 ",
    "* T * * 31 2 1 7 d 1 4 ",
    "* T * * 31 1 1 7 d' 1 3 ",
    "* T * * 31 2 2 7 t 1 2 ",
    "* T * * 31 1 2 7 t' 1 1 ",

    "* V * * 31 2 3 7 v 1 2 ",
    "* V * * 31 1 3 7 v' 1 1 ",

    "* Z � * 31 2 2 7 S 1 12 ",
    "* Z � * 31 1 2 7 S' 1 11 ",
    "* Z � * 31 2 1 7 Z 1 10 ",
    "* Z � * 31 1 1 7 Z' 1 9 ",
    "* Z � * 31 2 2 7 S 1 8 ",
    "* Z � * 31 1 2 7 S' 1 7 ",
    "* Z D � 31 2 1 7 Z 1 6 ",
    "* Z D � 31 1 1 7 Z' 1 5 ",
    "* Z * * 31 2 2 7 s  1 4 ",
    "* Z * * 31 1 2 7 s'  1 3 ",
    "* Z * * 31 2 1 7 z  1 2 ",
    "* Z * * 31 1 1 7 z'  1 1 ",

    "* � SZ * 31 2 2 8 S 1 12 ",
    "* � SZ * 31 1 2 8 S' 1 11 ",
    "* � SZ * 31 2 1 8 Z 1 10 ",
    "* � SZ * 31 1 1 8 Z' 1 9 ",
    "* � SZ * 31 2 2 7 s 1 8 ",
    "* � SZ * 31 1 2 7 s' 1 7 ",
    "* � SZ * 31 2 1 7 z 1 6 ",
    "* � SZ * 31 1 1 7 z' 1 5 ",
    "* � * * 31 2 2 7 S 1 4 ",
    "* � * * 31 1 2 7 S' 1 3 ",
    "* � * * 31 2 1 7 Z 1 2 ",
    "* � * * 31 1 1 7 Z' 1 1 ",

    "* _ * * 31 3 3 7 _ 1 1"
};


#endif // TRANSCRIBE_RULES_H