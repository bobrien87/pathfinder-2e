---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 4500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand is composed of ash that has been compressed, shaped, and sealed with a clear lacquer. When you trace the wand's tip along a solid surface, it leaves a black trail of charcoal. Writing with the wand in this way never damages or wears the wand down.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Disintegrate]]. If the spell reduces a living creature to fine powder, you animate that creature's ashes into a [[Sulfur Zombie]] with the same general appearance as the disintegrated creature. You control this sulfur zombie, which gains the minion and summoned traits. You can issue a verbal command to the sulfur zombie as a single action with the auditory and concentrate traits. The sulfur zombie crumbles into inanimate ash when reduced to 0 Hit Points or after 1 minute, whichever comes first.

**Craft Requirements** Supply a casting of *disintegrate*.

**Source:** `= this.source` (`= this.source-type`)
