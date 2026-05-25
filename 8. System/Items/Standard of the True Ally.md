---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner reminds those who view it of the strong bond they have with their comrades on the battlefield. Whenever you or an ally within the banner's aura uses an action on your turn to prepare to help with Aid, they can Step or Stride towards an ally as part of that action. They then become immune to this effect for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
