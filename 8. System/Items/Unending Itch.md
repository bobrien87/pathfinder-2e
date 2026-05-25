---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 700}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Invented to cause a lengthy and unpleasant demise, this poison manifests as an itch that can't be soothed. The victim experiences the poison damage as irritation rather than pain or sickness and must succeed at a DC 34 [[Perception]] check to realize they're poisoned. The poison can also be identified with a DC 34 [[Medicine]] check. Once the victim has lost half or more of its Hit Points, the DC drops to 30 for either check. As long as the victim doesn't realize it's poisoned, the GM makes its saving throws in secret.

**Saving Throw** DC 34 [[Fortitude]] save (secret)

**Maximum Duration** 5 minutes

**Stages 1–5** 1d6 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
