---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Disarm]]", "[[Magical]]", "[[Metal]]", "[[Sweep]]", "[[Trip]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The handle, chain, and spiked ball of this *+1 striking corrosive flail* are all made of iron so rusted that the weapon appears nonfunctional at first glance. On Strikes against a creature that's primarily made of metal, it gains the deadly d10 trait.

**Activate—Rusting Disarm** R

**Trigger** You critically succeed at a [[Disarm]] attempt with the flail against a metal weapon

**Effect** Flakes of acid-laden rust are deposited on the disarmed weapon. The weapon takes 2d6 untyped damage, ignoring the weapon's Hardness.

**Source:** `= this.source` (`= this.source-type`)
