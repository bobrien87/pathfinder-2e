---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 2800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The head of this imposing steel *+2 greater striking vitalizing morningstar* is shaped to resemble a cluster of snarling orc faces, their sharpened tusks serving as the spikes. Forged deep in the Hold of Belkzen and wielded by elite warriors tasked with protecting their lands from the servants of the Whispering Tyrant, this brutal weapon grants void resistance 5 to any living creature who wields it.

**Activate—Untouchable Spirit** `pf2:r` (fortune)

**Frequency** once per day

**Trigger** You fail or critically fail a saving throw against an effect originating from an undead creature that would inflict void damage

**Effect** Reroll the saving throw and take the better result.

**Source:** `= this.source` (`= this.source-type`)
