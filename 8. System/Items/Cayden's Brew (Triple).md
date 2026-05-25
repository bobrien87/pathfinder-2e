---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Poison]]", "[[Potion]]"]
price: "{'gp': 3200}"
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

Cayden's brew is like rich beer or ale, with a golden-brown color and foamy head. For 1 hour after you drink it, you have a +1 item bonus to saving throws against fear effects. Also, you can use a single action to breathe out a @Template[cone|distance:15] of intoxicating vapor with a burp that can be heard for 100 feet. Any creature in the vapor must attempt a DC 40 [[Fortitude]] save saving throw. After you use this breath weapon, you can't do so again for 1d4 rounds.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Clumsy]] 1 and [[Stupefied 1]] for 1 round.
- **Failure** The creature is clumsy 1 and stupefied 1 for 1d4 rounds.
- **Critical Failure** The creature becomes [[Clumsy]] 2, [[Stupefied 2]], and [[Sickened]] 1. The clumsy and stupefied conditions last until 1d4 rounds after the sickened condition ends.

> [!danger] Effect: Cayden's Brew

**Source:** `= this.source` (`= this.source-type`)
