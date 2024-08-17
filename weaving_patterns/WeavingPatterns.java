package com.research.higherweakorder;

import java.util.function.Consumer;

public class WeavingPattern {
    public static void iterate(int n, Consumer<int[][]> onPattern) {
        int[][] P = new int[n][];
        for (int i = 0; i < n; i++) {
            P[i] = new int[n-1];
            for (int j = 0; j < n; j++) {
                if (j < i) {
                    P[i][j] = j;
                } else if (j > i) {
                    P[i][j-1] = j;
                }
            }
        }
        int[][] braids = new int[n][];
        int[][] unbraids = new int[n][];
        for (int i = 0; i < n; i++) {
            braids[i] = new int[n-2];
            unbraids[i] = new int[n-2];
            for (int j = 0; j < n-2; j++) {
                braids[i][j] = 0;
                unbraids[i][j] = 0;
            }
            if (i >= 2) {
                braids[i][i-2] = ((i-2) << 12) | ((i-2) << 8) | ((i-1) << 4) | (i-2);
            }
        }
        _iterate(P, braids, unbraids, onPattern);
    }

    public static int[][] rotate(int[][] P) {
        int n = P.length;
        int[][] ret = new int[n][n-1];
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-1; j++) {
                ret[i][j] = (P[i+1][j]-1+n) % n;
            }
        }
        for (int i = 0; i < n-1; i++) {
            ret[n-1][i] = P[0][(n-2)-i] - 1;
        }
        return ret;
    }

    public static int[][] reflect(int[][] P) {
        int n = P.length;
        int[][] ret = new int[n][n-1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-1; j++) {
                ret[i][j] = (n-1) - P[(n-1)-i][j];
            }
        }

        return ret;
    }

    // P = weaving pattern
    // braids are encoded as (x << 12) | (ix << 8) | (y << 4) | (iy << 4)
    public static void _iterate(int[][] P, int[][] braids, int[][] unbraids, Consumer<int[][]> onPattern) {
        onPattern.accept(P);
        
        int n = P.length;

        for (int z = n-1; z >= 0; z--) {
            for (int iz = 0; iz < n-2; iz++) {
                int braid = braids[z][iz];
                if (braid == 0) {
                    continue;
                }

                int x = (braid >> 12) & 0xf;
                int ix = (braid >> 8) & 0xf;
                int y = (braid >> 4) & 0xf;
                int iy = (braid >> 0) & 0xf;

                // modify P in-place
                P[x][ix] ^= P[x][ix+1];
                P[x][ix+1] ^= P[x][ix];
                P[x][ix] ^= P[x][ix+1];

                P[y][iy] ^= P[y][iy+1];
                P[y][iy+1] ^= P[y][iy];
                P[y][iy] ^= P[y][iy+1];

                P[z][iz] ^= P[z][iz+1];
                P[z][iz+1] ^= P[z][iz];
                P[z][iz] ^= P[z][iz+1];

                // compute new braids
                braids[z][iz] = 0;
                int[] toReset = {-1, -1, -1, -1, -1};
                // xaz
                if (iz+2 < n-1 && 0 < ix && P[x][ix-1] == P[z][iz+2] && P[x][ix-1] < z && P[x][ix-1] > x) {
                    int a = P[x][ix-1];
                    int ia = 0;
                    while (P[a][ia] != x) {
                        ia++;
                    }
                    braids[z][iz+1] = (x << 12) | ((ix-1) << 8) | (a << 4) | (ia << 0);
                    toReset[0] = (z << 4) | (iz+1);
                }
                // ayz
                if (0 < iz && 0 < iy && P[z][iz-1] == P[y][iy-1] && P[y][iy-1] < y) {
                    int a = P[z][iz-1];
                    int ia = 0;
                    while (P[a][ia] != y) {
                        ia++;
                    }
                    braids[z][iz-1] = (a << 12) | (ia << 8) | (y << 4) | ((iy-1) << 0);
                    toReset[1] = (z << 4) | (iz-1);
                }
                // xya
                if (ix+2 < n-1 && iy+1 < n-2 && P[x][ix+2] == P[y][iy+2] && P[x][ix+2] > y) {
                    int a = P[x][ix+2];
                    int ia = 0;
                    while (P[a][ia] != x) {
                        ia++;
                    }
                    braids[a][ia] = (x << 12) | ((ix+1) << 8) | (y << 4) | ((iy+1) << 0);
                    toReset[2] = (a << 4) | (ia);
                }
                // set axy = 0
                if (0 < iy) {
                    int a = P[y][iy-1];
                    toReset[3] = (braids[y][iy-1] << 8) | (y << 4) | (iy-1);
                    braids[y][iy-1] = 0;

                }
                // set yza = 0
                if (iy+2 < n-1) {
                    int a = P[y][iy+2];
                    int ia = 0;
                    while (P[a][ia] != y) {
                        ia++;
                    }
                    if (ia < n-2) {
                        toReset[4] = (braids[a][ia] << 8) | (a << 4) | (ia);
                        braids[a][ia] = 0;
                    }
                }

                // new unbraids
                int[] unbraidsToReset = {-1, -1, -1, -1, -1};
                unbraids[z][iz] = 1;
                // unbraid xya = 0
                if (0 < ix && 0 < iy && P[x][ix-1] == P[y][iy-1] && P[x][ix-1] > y) {
                    int a = P[x][ix-1];
                    int ia = 0;
                    while (P[a][ia] != y) {
                        ia++;
                    }
                    if (ia < n-2) {
                        unbraidsToReset[0] = (unbraids[a][ia] << 8) | (a << 4) | (ia);
                        unbraids[a][ia] = 0;
                    }
                }
                // unbraid xaz = 0
                if (0 < iz && ix+2 < n-1 && P[z][iz-1] == P[x][ix+2] && P[z][iz-1] > x) {
                    unbraidsToReset[1] = (unbraids[z][iz-1] << 8) | (z << 4) | (iz-1);
                    unbraids[z][iz-1] = 0;
                }
                // unbraid ayz = 0
                if (iz+2 < n-1 && iy+2 < n-1 && P[z][iz+2] == P[y][iy+2] && P[z][iz+2] < y) {
                    unbraidsToReset[2] = (unbraids[z][iz+1] << 8) | (z << 4) | (iz+1);
                    unbraids[z][iz+1] = 0;
                }
                // unbraid axy = 1
                if (ix+2 < n-1 && iy+2 < n-1 && P[x][ix+2] == P[y][iy+2] && P[x][ix+2] < x) {
                    unbraidsToReset[3] = (unbraids[y][iy+1] << 8) | (y << 4) | (iy+1);
                    unbraids[y][iy+1] = 1;
                }
                // unbraid yza = 1
                if (0 < iy && 0 < iz && P[y][iy-1] == P[z][iz-1] && P[y][iy-1] > z) {
                    int a = P[y][iy-1];
                    int ia = 0;
                    while (P[a][ia] != z) {
                        ia++;
                    }
                    unbraidsToReset[4] = (unbraids[a][ia] << 8) | (a << 4) | (ia);
                    unbraids[a][ia] = 1;
                }


                boolean valid = true;
                boolean done = false;
                for (int w = n-1; w >= 0 && valid && !done; w--) {
                    for (int iw = 0; iw < n-2 && valid && !done; iw++) {
                        if (unbraids[w][iw] != 0) {
                            if (w == z && iw == iz) {
                                done = true;
                            } else {
                                valid = false;
                            }
                        }
                    }
                }
                if (valid) {
                    _iterate(P, braids, unbraids, onPattern);
                }

                for (int i = 0; i < 5; i++) {
                    if (toReset[i] != -1) {
                        braids[(toReset[i]>>4)&0xf][toReset[i] & 0xf] = toReset[i] >> 8;
                    }
                    if (unbraidsToReset[i] != -1) {
                        unbraids[(unbraidsToReset[i]>>4)&0xf][unbraidsToReset[i] & 0xf] = unbraidsToReset[i] >> 8;
                    }
                }
                unbraids[z][iz] = 0;
                braids[z][iz] = braid;
                // modify P in-place
                P[x][ix] ^= P[x][ix+1];
                P[x][ix+1] ^= P[x][ix];
                P[x][ix] ^= P[x][ix+1];

                P[y][iy] ^= P[y][iy+1];
                P[y][iy+1] ^= P[y][iy];
                P[y][iy] ^= P[y][iy+1];

                P[z][iz] ^= P[z][iz+1];
                P[z][iz+1] ^= P[z][iz];
                P[z][iz] ^= P[z][iz+1];
            }
        }
    }

    public static String toString(int[][] P) {
        String ret = "";
        int n = P.length;
        for (int i = n-1; i >= 0; i--) {
            ret += (i+1) + "|";
            for (int j = 0; j < n-1; j++) {
                ret += (P[i][j]+1) + ",";
            }
            if (i != 0) {
                ret += "\n";
            }
        }
        return ret;
    }
}