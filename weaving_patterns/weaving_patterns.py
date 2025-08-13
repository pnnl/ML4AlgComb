class WeavingPattern:
    @staticmethod
    def iterate(n, on_pattern):
        """
        Iterate through weaving patterns.
        
        Args:
            n: Size of the pattern
            on_pattern: Callback function to be called for each valid pattern
        """
        # Initialize pattern P
        P = []
        for i in range(n):
            P.append([0] * (n-1))
            for j in range(n):
                if j < i:
                    P[i][j] = j
                elif j > i:
                    P[i][j-1] = j
        
        # Initialize braids and unbraids
        braids = []
        unbraids = []
        for i in range(n):
            braids.append([0] * (n-2))
            unbraids.append([0] * (n-2))
            if i >= 2:
                braids[i][i-2] = ((i-2) << 12) | ((i-2) << 8) | ((i-1) << 4) | (i-2)
        
        WeavingPattern._iterate(P, braids, unbraids, on_pattern)
    
    @staticmethod
    def rotate(P):
        """
        Rotate the weaving pattern.
        
        Args:
            P: Weaving pattern
            
        Returns:
            Rotated pattern
        """
        n = len(P)
        ret = [[0 for _ in range(n-1)] for _ in range(n)]
        
        for i in range(n-1):
            for j in range(n-1):
                ret[i][j] = (P[i+1][j]-1+n) % n
        
        for i in range(n-1):
            ret[n-1][i] = P[0][(n-2)-i] - 1
        
        return ret
    
    @staticmethod
    def reflect(P):
        """
        Reflect the weaving pattern.
        
        Args:
            P: Weaving pattern
            
        Returns:
            Reflected pattern
        """
        n = len(P)
        ret = [[0 for _ in range(n-1)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n-1):
                ret[i][j] = (n-1) - P[(n-1)-i][j]
        
        return ret
    
    @staticmethod
    def _iterate(P, braids, unbraids, on_pattern):
        """
        Internal recursion function for iterating through patterns.
        
        Args:
            P: Current weaving pattern
            braids: Braid encodings
            unbraids: Unbraid encodings
            on_pattern: Callback function for each valid pattern
        """
        on_pattern(P)
        
        n = len(P)
        
        for z in range(n-1, -1, -1):
            for iz in range(n-2):
                braid = braids[z][iz]
                if braid == 0:
                    continue
                
                x = (braid >> 12) & 0xf
                ix = (braid >> 8) & 0xf
                y = (braid >> 4) & 0xf
                iy = (braid >> 0) & 0xf
                
                # Modify P in-place - swap adjacent elements (XOR swap)
                P[x][ix], P[x][ix+1] = P[x][ix+1], P[x][ix]
                P[y][iy], P[y][iy+1] = P[y][iy+1], P[y][iy]
                P[z][iz], P[z][iz+1] = P[z][iz+1], P[z][iz]
                
                # Compute new braids
                braids[z][iz] = 0
                to_reset = [-1, -1, -1, -1, -1]
                
                # xaz
                if iz+2 < n-1 and 0 < ix and P[x][ix-1] == P[z][iz+2] and P[x][ix-1] < z and P[x][ix-1] > x:
                    a = P[x][ix-1]
                    ia = 0
                    while P[a][ia] != x:
                        ia += 1
                    braids[z][iz+1] = (x << 12) | ((ix-1) << 8) | (a << 4) | (ia << 0)
                    to_reset[0] = (z << 4) | (iz+1)
                
                # ayz
                if 0 < iz and 0 < iy and P[z][iz-1] == P[y][iy-1] and P[y][iy-1] < y:
                    a = P[z][iz-1]
                    ia = 0
                    while P[a][ia] != y:
                        ia += 1
                    braids[z][iz-1] = (a << 12) | (ia << 8) | (y << 4) | ((iy-1) << 0)
                    to_reset[1] = (z << 4) | (iz-1)
                
                # xya
                if ix+2 < n-1 and iy+1 < n-2 and P[x][ix+2] == P[y][iy+2] and P[x][ix+2] > y:
                    a = P[x][ix+2]
                    ia = 0
                    while P[a][ia] != x:
                        ia += 1
                    braids[a][ia] = (x << 12) | ((ix+1) << 8) | (y << 4) | ((iy+1) << 0)
                    to_reset[2] = (a << 4) | (ia)
                
                # set axy = 0
                if 0 < iy:
                    a = P[y][iy-1]
                    to_reset[3] = (braids[y][iy-1] << 8) | (y << 4) | (iy-1)
                    braids[y][iy-1] = 0
                
                # set yza = 0
                if iy+2 < n-1:
                    a = P[y][iy+2]
                    ia = 0
                    while P[a][ia] != y:
                        ia += 1
                    if ia < n-2:
                        to_reset[4] = (braids[a][ia] << 8) | (a << 4) | (ia)
                        braids[a][ia] = 0
                
                # New unbraids
                unbraids_to_reset = [-1, -1, -1, -1, -1]
                unbraids[z][iz] = 1
                
                # unbraid xya = 0
                if 0 < ix and 0 < iy and P[x][ix-1] == P[y][iy-1] and P[x][ix-1] > y:
                    a = P[x][ix-1]
                    ia = 0
                    while P[a][ia] != y:
                        ia += 1
                    if ia < n-2:
                        unbraids_to_reset[0] = (unbraids[a][ia] << 8) | (a << 4) | (ia)
                        unbraids[a][ia] = 0
                
                # unbraid xaz = 0
                if 0 < iz and ix+2 < n-1 and P[z][iz-1] == P[x][ix+2] and P[z][iz-1] > x:
                    unbraids_to_reset[1] = (unbraids[z][iz-1] << 8) | (z << 4) | (iz-1)
                    unbraids[z][iz-1] = 0
                
                # unbraid ayz = 0
                if iz+2 < n-1 and iy+2 < n-1 and P[z][iz+2] == P[y][iy+2] and P[z][iz+2] < y:
                    unbraids_to_reset[2] = (unbraids[z][iz+1] << 8) | (z << 4) | (iz+1)
                    unbraids[z][iz+1] = 0
                
                # unbraid axy = 1
                if ix+2 < n-1 and iy+2 < n-1 and P[x][ix+2] == P[y][iy+2] and P[x][ix+2] < x:
                    unbraids_to_reset[3] = (unbraids[y][iy+1] << 8) | (y << 4) | (iy+1)
                    unbraids[y][iy+1] = 1
                
                # unbraid yza = 1
                if 0 < iy and 0 < iz and P[y][iy-1] == P[z][iz-1] and P[y][iy-1] > z:
                    a = P[y][iy-1]
                    ia = 0
                    while P[a][ia] != z:
                        ia += 1
                    unbraids_to_reset[4] = (unbraids[a][ia] << 8) | (a << 4) | (ia)
                    unbraids[a][ia] = 1
                
                # Check validity
                valid = True
                done = False
                for w in range(n-1, -1, -1):
                    for iw in range(n-2):
                        if unbraids[w][iw] != 0:
                            if w == z and iw == iz:
                                done = True
                            else:
                                valid = False
                        if not valid or done:
                            break
                    if not valid or done:
                        break
                
                if valid:
                    WeavingPattern._iterate(P, braids, unbraids, on_pattern)
                
                # Reset
                for i in range(5):
                    if to_reset[i] != -1:
                        braids[(to_reset[i] >> 4) & 0xf][to_reset[i] & 0xf] = to_reset[i] >> 8
                    if unbraids_to_reset[i] != -1:
                        unbraids[(unbraids_to_reset[i] >> 4) & 0xf][unbraids_to_reset[i] & 0xf] = unbraids_to_reset[i] >> 8
                
                unbraids[z][iz] = 0
                braids[z][iz] = braid
                
                # Restore P - swap back
                P[x][ix], P[x][ix+1] = P[x][ix+1], P[x][ix]
                P[y][iy], P[y][iy+1] = P[y][iy+1], P[y][iy]
                P[z][iz], P[z][iz+1] = P[z][iz+1], P[z][iz]
    
    @staticmethod
    def to_string(P):
        """
        Convert pattern to string representation.
        
        Args:
            P: Weaving pattern
            
        Returns:
            String representation of pattern
        """
        ret = ""
        n = len(P)
        for i in range(n-1, -1, -1):
            ret += str(i+1) + "|"
            for j in range(n-1):
                ret += str(P[i][j]+1) + ","
            if i != 0:
                ret += "\n"
        return ret

N = 7
with open(f"weaving_patterns_{N}.txt", "w") as f:
    WeavingPattern.iterate(N, lambda P: f.writelines(WeavingPattern.to_string(P)+"\n\n"))