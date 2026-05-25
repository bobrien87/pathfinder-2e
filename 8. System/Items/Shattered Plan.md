---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Recovery]]", "[[Thrown]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though the body of this *+2 striking impactful boomerang* is riddled with glowing hairline cracks, the weapon feels reassuringly solid in the hand. If you damage a target that has been struck by a *rime foil* within the last round, you bruise its chilled body, and the target takes a –5-foot penalty to all its Speeds, or a –10-foot penalty on a critical hit.

**Special** The shattered plan pairs with the *[[Rime Foil]]*.

**Source:** `= this.source` (`= this.source-type`)
