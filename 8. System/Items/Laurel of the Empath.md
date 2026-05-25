---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Fortune]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 70000}"
usage: "worncirclet"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silvery, woven ring of leaves sits on top of the head. While wearing it, when you roll Perception for initiative, you can roll twice and take the higher result. This is a fortune effect. Whenever you spend at least 1 minute talking with a living creature, you automatically become aware of its attitude toward you. When you invest the laurel, you either increase your Wisdom modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** R (concentrate)

**Frequency** once per minute

**Trigger** You're hit by an attack

**Effect** You take half damage from the triggering attack.

**Activate** R (concentrate)

**Frequency** once per hour

**Trigger** You fail, but don't critically fail, a saving throw

**Effect** You anticipate the danger and guard against it, often in unconventional or almost inconceivable ways. Treat the failed saving throw as a success.

**Activate** 10 minutes (concentrate, fortune, mental)

**Frequency** once per day

**Effect** You spend 10 minutes talking with one living creature, conversing in inspirational, religious, or philosophical terms. You gain valuable insights into the personality of your target—their hopes, dreams, and fears. When the ritual is over, you gain a +4 item bonus to all Perception checks made concerning the target for one month. Also, the target gains inspirational insight, allowing the target to use one of the two reactions listed above once during the next 24 hours.

**Source:** `= this.source` (`= this.source-type`)
