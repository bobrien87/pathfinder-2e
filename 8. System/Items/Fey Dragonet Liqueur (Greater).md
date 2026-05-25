---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Potion]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Each draft of fey dragonet liqueur has a different flavor. For 1 hour after you drink it, you can use a single action to breathe out a @Template[type:cone|distance:15] of euphoric gas. Each creature in the cone must attempt a DC 37 [[Will]] save. After you expel this magical breath, you can't do so again for 1d4 rounds.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Stupefied 1]] for 1 round.
- **Failure** The creature is stupefied 1 for 1 minute and [[Slowed]] 1 for 1d4 rounds.
- **Critical Failure** The creature is [[Stupefied 2]] and slowed 1 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
