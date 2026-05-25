---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cypress onusa rod is decorated with a number of paper streamers that rustle when shaken to direct purification magic. Wands of purification contain either [[Cleanse Affliction]], [[Clear Mind]], or [[Sound Body]], decided when the wand is created.

**Activate** [[Cast a Spell]]

**Frequency** once per day, plus overcharge

**Effect** You cast *cleanse affliction*, *clear mind*, or *sound body* of the indicated level. If your counteract check would be sufficient only to suppress the effect until the beginning of your next turn, instead of to fully counteract it, then you can Sustain the Activation of the wand each round to suppress the effect for an additional round, to a maximum of 1 minute. You Sustain the Activation by shaking the wand, so if at any point you release or otherwise drop the wand, the effect immediately stops being suppressed and resumes on the target as normal.

**Craft Requirements** Supply a casting of *cleanse affliction*, *clear mind*, or *sound body*, as appropriate.

**Source:** `= this.source` (`= this.source-type`)
