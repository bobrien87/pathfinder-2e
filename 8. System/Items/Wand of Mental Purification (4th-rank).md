---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Emotion]]", "[[Healing]]", "[[Magical]]", "[[Mental]]", "[[Wand]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Red feathers hang from the handle of this ivory wand. Holding it brings a sense of gentle calm.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 4th-rank [[Soothe]], and can attempt to counteract one mental effect on the same target. Treat the [[Soothe]] spell's rank as 1 higher for this counteract check.

**Craft Requirements** Supply a casting of *soothe* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
