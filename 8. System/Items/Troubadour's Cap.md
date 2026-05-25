---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This jaunty cap can take the form and color of any type of hat you wish upon investing the item, but it always has a peacock feather jutting out from one side. You gain a +2 item bonus to Diplomacy and Performance checks while wearing the cap. When you invest the cap, you either increase your Charisma modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You cast [[Hypnotize]] (DC 37).

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** Picking the feather from your cap, you throw it toward a target, casting [[Prismatic Spray]] (DC 35).

**Source:** `= this.source` (`= this.source-type`)
