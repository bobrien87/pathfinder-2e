---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Although the simple pies that fill this glass plate every minute are edible, they don't last long enough to sate hunger or provide any real nutritive value. Instead, they can be magically guided at targets, unleashed harmlessly by even the most uncoordinated child.

**Activate—Project Pastry** `pf2:1` (manipulate)

**Frequency** once per minute

**Effect** You magically hurl the pie at a creature within 30 feet. Unless the target succeeds at a DC 15 [[Reflex]] save, they're splattered with a harmless but tasty mess, which remains until it is wiped away with an Interact action or is otherwise cleaned off (like if the target is submerged in water). After a minute, the mess disappears, and the pieplate refills with another kind of pie.

**Source:** `= this.source` (`= this.source-type`)
