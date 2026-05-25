---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Concussive]]", "[[Fatal d8]]", "[[Magical]]", "[[Wand]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Used by gunwitches who want a bit more power each day, a *pistol wand* is a firearm that also contains an [[Enfeeble]] spell that can be cast using the same rules as a wand. Many other variants exist with different 1st-rank spells. This *+1 flintlock pistol* has a [[Reinforced Stock]] permanently attached to it, and the pistol's *potency rune* (and any other runes) applies to Strikes with the stock as well.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast *enfeeble*.

**Source:** `= this.source` (`= this.source-type`)
