---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Adjusted]]", "[[Extradimensional]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 8000}"
bulk: "1"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made from the finest plates of monstrous insect chitin, this *+2 greater resilient mantis shell* offers superior protection from Mediogalti's hot weather while also allowing the wearer to blend into almost any situation and strike with hidden blades. While wearing this armor, you are protected from extreme heat and severe heat effects. *Vernai shell* armor includes two extradimensional spaces built into each of the armor's gloves, granting the wearer two places to store items. Each glove can hold one item of 1 Bulk or less. While an item is stored in one of the two gloves, there is nothing to indicate that an item is being held inside it.

**Activate—Store Item** `pf2:1` (manipulate)

**Requirements** At least one of the *Vernai shell's* two extradimensional spaces is empty

**Effect** One item you're holding with a Bulk of 1 or less vanishes into one of the armor's extradimensional spaces.

**Activate—Retrieve Item** `pf2:f` (manipulate)

**Requirements** An item is stored in at least one of the *Vernai shell's* extradimensional spaces, and you have a free hand

**Effect** One item of your choice in either extradimensional space appears in your hand. You can't Retrieve Item again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
