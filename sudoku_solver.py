# Autor: 
# Datum:
# Version: 
# Beschreibung: 

# Hier kann man das Sudoku einfüllen welches gelöst werden muss
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Hier wird die grösse vom Sudoku bestummen.
S = 9  # Sudoku grid (9x9)

# Eine Funktion welche das Sudoku-Gitter druckt im Terminal
def buildSudokuGrid(a):
    # Printet den oberen Rand des Sudoku
    print("+-------+-------+-------+")
    # Eine schlaufe über jede Zeile des Sudoku
    for i in range(S):
        # Printet die linke seite des Sudoku
        print("| ", end="")
        # Eine Schlaufe über jede Spalte des Sudoku
        for j in range(S):
            # Printet den aktuellen Wert der Zelle
            print(a[i][j], end=" ")
            # Printet einen Vertikalen strich alle 3 Zellen
            if (j + 1) % 3 == 0:
                print("| ", end="")
            elif j == 8:
                print("| ", end="")
        # Printet einen horinzonalen strich alle 3 Spalten
        if (i + 1) % 3 == 0:
            print("\n+-------+-------+-------+")
        else:
            print("\n", end="")


# Diese Funktion prüft ob eine bestimmte Zahl in einer bestimmten Zelle platziert werden kann.
def possiblSolve(grid, row, column, number):
    
    # Ist die Zahl in der angegebenen Zeile?
    for v in range(S):
        if grid[row][v] == number:
            return False
    # Ist die Zahl in der angegebenen Spalte?
    for v in range(S):
        if grid[v][column] == number:
            return False
    # Ist die Zahl in der angegebenen Platz?
    xCol = column - column % 3
    yRow = row - row % 3
    for i in range(3):
        for j in range(3):
            if grid[i + yRow][j + xCol] == number:
                return False
    # Wenn die Zahl noch nicht vorhanden ist dann kann sie eingesetzt werden.
    return True

# Diese Funktion löst das Sudoku dabei wird der Backtracking-Algorithmus verwendet
def SudukoSolver(grid, row, column):
    # Wenn alle Zeilen erfolgreich ausgefüllt worden sind gibt es ein True zurück
    if row == S - 1 and column == S:
        return True

    # Wenn alle Zellen in dem Aktuellen Reihe ausgefüllt worden ist geht es zur nechsten Reihe.
    if column == S:
        row += 1
        column = 0

    # Wenn die aktuelle Zelle ausgefüllt ist geht es zur nechsten Zelle
    if grid[row][column] > 0:
        return SudukoSolver(grid, row, column + 1)

    # Iteriert über jede Zahl von 1 bis 9 und versuchen Sie in die aktuelle Zelle zu einsetzen
    for number in range(1, S + 1, 1):
        if possiblSolve(grid, row, column, number):
            # Wenn die Zahl in der aktuellen Zelle platziert werden kann setzen wir die Zahl ein
            grid[row][column] = number
            # Recursively call the Suduko function with the next cell as the starting point
            if SudukoSolver(grid, row, column + 1):
                return True

        # Wenn die Zahl nicht eingesetzt werden kann bei der aktuellen Zelle dann wird ein Schritt zurückgegeangen und die nechste Zahl probiert. 
        grid[row][column] = 0

    # Wenn keine Zahl eingesetzt werden kann ohne die Sudoku-Regeln zu verletzen wird ein False zurückgegben
    return False

# Überprüfe ob das Sudoku gelöst werden kann indem man der SudokuSolver funktion mit den Anfangscoridnaten 0, 0 aufgerufen wird
if (SudukoSolver(grid, 0, 0)):
    print("")
    print("The solved Sudoku")
    # Erstellt das Sudoku Gitter mit der buildSudoGrid funktion und gibt es aus
    buildSudokuGrid(grid)
    print("")
else:
    print("")
    # Wenn das Sudoku nicht gelöst werden kann wird diese Fehlermeldung ausgegeben.
    print("Das gegebene Sudoku kann nicht gelöst werden:(")
    print("")
