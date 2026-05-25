---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Bulwark]]", "[[Entrench ranged]]", "[[Ponderous]]"]
price: "{'gp': 1000}"
bulk: "5"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of bone-based fortress plate is a masterpiece of alchemical science. This armor has a receiver that can hold a single lodestone bomb, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** A lodestone bomb is installed in the armor.

**Effect** The bomb shifts numerous small plates and hinges, offering a wide variety of protections, granting you resistance to cold, electricity, fire, piercing, and slashing damage equal to the loaded lodestone bomb's splash damage. These effects last for 20 minutes, but each time you're hit by an attack that deals damage of one of these types, decrease the remaining duration by 1 minute. Once activated, the armor can't be deactivated. The activation uses up the lodestone bomb, and the armor can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
