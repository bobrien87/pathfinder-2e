---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]", "[[Shove]]"]
price: "{'gp': 70000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sturdy head of this *+3 major striking [[Flaming]] [[Shock]] orichalcum warhammer* is shaped like a blazing comet.

**Activate—Comet Fall** R (concentration)

**Trigger** Your attack roll with the *sky hammer* is a critical success

**Effect** A 6th-rank arcane [[Fireball]] spell explodes, centered on the *sky hammer*. The spell DC is 45. You are immune to the *fireball's* effect, though your allies are not.

**Craft Requirements** Supply a casting of *fireball* (6th rank), and the initial raw materials must include 12,375 gp of orichalcum.

**Source:** `= this.source` (`= this.source-type`)
