---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Monk]]", "[[Parry]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 240}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking bo staff* is covered in scales shed by or harvested from a dragon. When benefiting from the circumstance bonus to AC granted by the bo staff's parry trait, you also gain a +1 circumstance bonus to saving throws against magical effects of the tradition matching the dragon who provided the scales, plus resistance 5 to a damage type determined by that tradition: force for arcane, spirit for divine, mental for occult, or fire for primal. For instance, a *dragonscale bo staff* made with scales taken from an omen dragon would provide a +1 circumstance bonus to saves against occult effects and resistance 5 to mental damage.

**Craft Requirements** The initial raw materials must include scales from one type of dragon.

**Source:** `= this.source` (`= this.source-type`)
