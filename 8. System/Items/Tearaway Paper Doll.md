---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 11}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate, manipulate)

A humanoid shape has been cut out of a single sheet of colored paper with a face and clothes drawn on. The face looks slightly worried, as if the doll knows what it was made for. You hold up the paper doll in two hands and rip it half, focusing your thoughts on a creature within 20 feet that you can see. That creature takes 3d6 slashing damage (DC 18 [[Fortitude]] save) as the tears of the paper doll are mimicked on its body.

**Source:** `= this.source` (`= this.source-type`)
