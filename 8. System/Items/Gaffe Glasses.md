---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "worneyepiece"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These wire-rim glasses appear to be [[Glasses of Sociability]], making you think they grant a +1 item bonus to Diplomacy when they grant none. The GM secretly adjusts your Diplomacy checks to ignore the bonus, and if you have multiple +1 item bonuses to Diplomacy, the glasses take precedence, negating those bonuses.

**Activate** `pf2:1` (concentrate)

**Effect** Like glasses of sociability, with the same limitations, you stare at another creature. If you've met and exchanged names, you expect to instantly remember the target's name. However, you recall the worst possible incorrect name, such as mistaking a famous artist for their hated rival. This blunder doesn't prevent you from realizing the creature's real name after you've been corrected. Once you use this activation, the glasses fuse to you.

**Source:** `= this.source` (`= this.source-type`)
