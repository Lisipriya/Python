
import prettytable
table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Azumarill", "Water"])
table.add_row(["Bellossom", "Grass"])
print(table)
table1 = prettytable.PrettyTable()
table1.add_column("Pokemons", ["Combee", "Bulbasaur", "Squirtle"])
table1.add_column("Types", ["Flying", "Poison", "Water"])
table1.align = "l"
print(table1)

