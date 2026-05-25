---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]"]
price: "{'gp': 4000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This standard-grade dawnsilver shield (Hardness 5, HP 20, BT 10) is inscribed with the symbol of a deity dedicated to healing and medicine. The shield is designed for combat medics to aid combatants or adventurers in the midst of battle. Healer's tools can be stored on the backside of this shield. This shield grants a +2 item bonus to Medicine checks.

**Activate—Adrenaline Boost** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You grant a medicinal boost to bring someone back into the fray. You Administer First Aid to stabilize an adjacent ally with the dying condition. On a success, they gain @Damage[(6d6+20)[healing]] Hit Points, can immediately [[Stand]] as a free action, and become [[Quickened]] for 1 round. They can use this extra action only to Stride or Strike.

**Source:** `= this.source` (`= this.source-type`)
