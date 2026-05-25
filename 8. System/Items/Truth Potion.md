---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Potion]]"]
price: "{'gp': 46}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

For 10 minutes after drinking this astringent potion, you can't intentionally lie and may be compelled to tell the truth. Upon drinking the potion, attempt a DC 19 [[Will]] save. You can voluntarily fail or critically fail.
- **Success** The potion does not affect you.
- **Failure** When you speak, you must tell the truth.
- **Critical Failure** As failure, and when someone asks you a question, you must attempt another DC 19 [[Will]] save saving throw. If you fail this saving throw, you must answer the question truthfully if you are able to do so; if you succeed, you are temporarily immune to further attempts to ask the same question within the potion's duration.

**Source:** `= this.source` (`= this.source-type`)
