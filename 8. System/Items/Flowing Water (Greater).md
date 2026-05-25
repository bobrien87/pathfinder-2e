---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 1200}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The Flood Truce is a season of relative peace, and this tattoo of a river can soothe your temper when you might otherwise lash out. You gain a +1 item bonus to Diplomacy checks made against orcs who honor the Flood Truce.

**Activate—Embody the Truce** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** A mental effect would compel you to harm an ally or bystander

**Effect** Attempt a counteract check with a counteract rank of 6 to end the effect.

**Source:** `= this.source` (`= this.source-type`)
