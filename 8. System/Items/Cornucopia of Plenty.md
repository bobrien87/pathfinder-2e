---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This exquisite wicker horn is made of green wood and smells of fresh wheat and barley.

**Activate—Bountiful Rations** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You draw forth and consume a filling snack from this cornucopia. You gain 5 temporary Hit Points that last for 1 minute and suppress the effects of the [[Fatigued]] condition for 10 minutes.

> [!danger] Effect: Cornucopia of Plenty

**Source:** `= this.source` (`= this.source-type`)
