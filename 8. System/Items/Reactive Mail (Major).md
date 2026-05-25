---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 14000}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Often heavily battle scared from use, this *+2 greater resilient chain mail* is commonly issued to frontline soldiers who are tasked with battling through enemies to reach high-value targets across the battlefield.

**Activate–Quick Spike** `pf2:r` (manipulate, metal)

**Frequency** once per hour

**Trigger** A creature within 15 feet uses a manipulate action

**Effect** An iron spike launches from your armor at the target, dealing 7d8 piercing damage to the target (DC 36 [[Reflex]] save). If the target critically fails, the triggering action is disrupted.

**Source:** `= this.source` (`= this.source-type`)
