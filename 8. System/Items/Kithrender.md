---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]", "[[Sweep]]"]
price: "{'gp': 10000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The head of this heavily notched +2 greater striking fearsome greataxe is crudely inscribed with the face of a hideous fiend, its fangs bared in a twisted leer. The name of the fiend has been lost to history, but legends say it took a particular delight in turning the bonds between mortal beings against them, and that it created these weapons for its mortal acolytes so that they might carry on its cruel work.

When you make a successful Strike with a kithrender, it deals 1d6 mental damage to all other enemies within 30 feet who consider the target an ally. All mental damage dealt by this weapon is doubled if the target is uniquely connected by a strong bond, such as family or a creature with the minion trait, or any kind of magical connection, such as telepathy.

**Activate—Render Connection** `pf2:f` (concentrate)

**Frequency** once per 10 minutes

**Trigger** You reduce an enemy to 0 Hit Points with this weapon

**Effect** Each foe within 30 feet who considers the target an ally takes an additional 6d8 mental damage (DC 35 [[Will]] save).

**Source:** `= this.source` (`= this.source-type`)
