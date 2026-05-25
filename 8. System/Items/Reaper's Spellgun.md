---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Attack]]", "[[Consumable]]", "[[Magical]]", "[[Spellgun]]", "[[Void]]"]
price: "{'gp': 600}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Strike

A rod of blackened bone with a bulb at one end comprises a *reaper's spellgun*, which feels heavier than it looks. You Activate the spellgun by aiming it at one creature and making your choice of a spell attack roll or a firearm attack roll against the target's AC. This spellgun has a range increment of 30 feet. The spellgun fires a shadowy ray, then dissolves into gray mist.
- **Critical Success** The target takes 4d6 void and is [[Drained]] 2 and [[Doomed]] 1. If it had fewer than half its maximum Hit Points after taking the void damage, it's [[Drained]] 3 instead. If the Hit Point loss from being drained drops the creature to 0 Hit Points, it dies.
- **Success** As critical success, but for the drained condition, the target is [[Drained]] 1, or drained 2 if it had fewer than half its maximum HP.

**Source:** `= this.source` (`= this.source-type`)
