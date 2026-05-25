---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Misfortune]]", "[[Talisman]]"]
price: "{'gp': 700}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You damage an [[Off Guard]] creature with the affixed weapon

This bone statuette of a sneering gremlin crumbles to dust when activated, imparting a fraction of its subject's infamous misfortune unto those you strike. The damaged creature must attempt a DC 33 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature must roll twice and take the worse result on the next check it attempts.
- **Failure** The creature must roll twice and take the worse result on all checks until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
