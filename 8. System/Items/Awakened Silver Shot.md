---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 2300}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

These bullets are formed from a liquefied high-grade precious metal and enchanted to unlock that metal's true potential.

The shot is a high-grade silver bullet. The awakened silver gleams with altered celestial moonlight designed to weaken and expose devils and werecreatures. On a hit, it attempts to counteract any polymorph effect on the target. The counteract rank is 9, and the counteract modifier is +27. If you fail (but don't critically fail) the counteract check against a devil or a werecreature, you get a success instead. If you counteracted the Change Shape ability, the creature can't use that ability again for 1 round, or 1 minute on a critical success. If you hit a devil or werecreature not under a polymorph effect, the target is [[Enfeebled]] 1 for 1 minute instead.

**Source:** `= this.source` (`= this.source-type`)
