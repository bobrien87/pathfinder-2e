---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 30}"
usage: "worn"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This rare gadget uses Stasian technology to grant someone a burst of activity, though its use can be painful. The electromuscular stimulator must be carefully attached to you, requiring 1 minute to do so. You can attach an electromuscular stimulator to yourself. When you Activate an attached electromuscular stimulator, roll a [[Crafting]] check, using the Crafting modifier of the creature who attached the stimulator to you, with a DC equal to the standard DC for your level. The effects of the activation depend on the result of the Crafting check.
- **Critical Success** You gain the [[Quickened]] condition for 1 minute and can use the extra action each round only to Stride or Strike.
- **Success** As critical success, but you also take 3 persistent electricity damage.

> [!danger] Effect: Electromuscular Stimulator
- **Failure** You gain the quickened condition for 2 rounds and can use the extra action each round only to Stride or Strike. You take 3 persistent electricity damage.

> [!danger] Effect: Electromuscular Stimulator (Failure)
- **Critical Failure** You take @Damage[2d6[electricity],3[persistent,electricity]]{2d6 electricity damage and 3 persistent electricity damage}.

**Source:** `= this.source` (`= this.source-type`)
