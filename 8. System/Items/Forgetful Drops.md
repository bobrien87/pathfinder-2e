---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Member of a secret society

These innocuous, colorless drops can be poured directly into a victim's mouth, or slipped into their food or drink. They initially haze a victim's mind slightly, making them easier to fool; in later stages, they can lead to the victim entering a murderous [[Confused]] state. Secret societies use these drops to befuddle a target or to frame them for violence.

**Saving Throw** DC 18 [[Fortitude]] save

**Onset** 5 minutes

**Maximum Duration** 1 hour

**Stage 1** [[Stupefied 1]] (10 minutes)

**Stage 2** stupefied 1 and [[Clumsy]] 1 (20 minutes)

**Stage 3** stupefied 1, clumsy 1, and [[Confused]] (30 minutes)

**Source:** `= this.source` (`= this.source-type`)
