---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 475}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A mask of the cursed eye is decorated with at least one wide, staring eye. The first time each day you're targeted with a detection, prediction, revelation, or scrying spell by a creature on your plane that you can't perceive, the creature targeting you must attempt a DC 24 [[Will]] save. This effect is automatic and does not require you to Activate the item.
- **Critical Success** The creature is unaffected.
- **Success** The creature is unaffected. You know you've been targeted with a divination spell, but the mask gives you no additional information.
- **Failure** The creature is [[Sickened]] 1 and [[Dazzled]] for 1 minute. You know you've been targeted with a divination spell, but the mask gives you no additional information.
- **Critical Failure** The creature is [[Sickened]] 2 and dazzled for 10 minutes, and the spell is disrupted. You gain a brief mental glimpse of the triggering creature and learn its approximate distance and direction.

**Source:** `= this.source` (`= this.source-type`)
