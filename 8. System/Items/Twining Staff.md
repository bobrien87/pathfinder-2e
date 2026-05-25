---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Monk]]", "[[Two hand d8]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Appearing to be just a small, flat disk made of twigs, this item can grow and shrink. Once formed, this oak staff is carved with twisting patterns along its length.

**Activate—Form Staff** A (manipulate)

**Effect** You cause the twigs to rapidly grow or contract, reshaping into a *+1 striking staff*, a *+1 striking bo staff*, or its disk form. In its disk form, it has negligible Bulk and must be held in one hand to be activated. In the other forms, it has the same Bulk as a normal weapon of its type. You can switch your grip as part of the activation.

When you expand the item, you can use the force of the expansion to High Jump or to try to Force Open a door or the like by wedging the disk into a gap before activation. The staff makes the Athletics check with a `r 1d20+15` modifier.

**Source:** `= this.source` (`= this.source-type`)
