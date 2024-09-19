class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Black: row and col must be even 
        # Black: row and col must be old 
        # White: row old and col even 
        # White: row even and col old 

        if (ord(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 == 0) or (ord(coordinates[0]) % 2 == 1 and int(coordinates[1]) % 2 == 1):
            return False 
        if (ord(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 == 1) or (ord(coordinates[0]) % 2 == 1 and int(coordinates[1]) % 2 == 0):
            return True   



        