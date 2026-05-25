---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 24000}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These sturdy leather sandals feature straps that wrap up to the knees. Etched in the leather are intricate patterns of stags leaping through the forest. You gain a +5-foot item bonus to your land Speed and a +3 item bonus on Athletics checks when attempting to [[High Jump]] or [[Long Jump]]. When you invest the sandals, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** R (concentrate)

**Frequency** once per minute

**Trigger** You attempt a High Jump or Long Jump but you didn't Stride at least 10 feet

**Effect** You can attempt the jump normally. It doesn't automatically fail.

**Source:** `= this.source` (`= this.source-type`)
