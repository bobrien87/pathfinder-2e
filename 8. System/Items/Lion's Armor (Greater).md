---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 30500}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Various parts of this +3 *greater resilient half plate* are forged into the shape of a lion's head. The golden lion heads grant you a commanding presence and seem to actively growl at your enemies, granting you a +3 item bonus to Intimidation.

The lions on the armor work in tandem with the lion on a *lion's shield*. If you critically hit with the *lion's shield* using Lion Bite, the lions on the armor roar in support of the shield, causing the target of the shield's Strike to become [[Frightened]] 1.

**Activate—Roar of the Pride** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** The lions on your armor roar, attempting to cow your enemies. Attempt a check to [[Demoralize]] each enemy within 30 feet of you. On a critical success, the target is also [[Fleeing]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
