---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Divine]]", "[[Magical]]", "[[Vitality]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

These roasted soybeans are blessed by a priest to ward against all various forms of otherworldly influence, but are most effective against incorporeal evils, such as wraiths or path maidens. They can be safely eaten by living creatures and taste delicious when paired with rice wine. When you activate this item, choose an adjacent square to exhale into. You fill that square with soothing vapors that harm any fiend, fey, ghost, spirit, or undead creature that ends their turn in that square for the next minute, causing them to take @Damage[(4d8+4)[spirit]] damage (DC 28 [[Will]] save). An incorporeal creature that takes this damage must also attempt a DC 28 [[Fortitude]] save to resist being affected as follows.
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes [[Off Guard]] until the start of your next turn.
- **Failure** The creature becomes [[Slowed]] 1 for 1 round.
- **Critical Failure** The creature becomes [[Stunned]] 1 and is then slowed 1 for 1 round after the stun effect ends.

**Source:** `= this.source` (`= this.source-type`)
