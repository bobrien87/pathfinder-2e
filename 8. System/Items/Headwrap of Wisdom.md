---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worncirclet"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple scarf is designed for wrapping around the head and comes with a gemmed pin for decoration. When you invest the headwrap, you either increase your Wisdom modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Consider the Consequences** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** When you are considering a course of action, you get a gut feeling about whether it's a good idea. You gain the effects of an [[Augury]] spell, except that you receive the result from your own instincts rather than an external source.

**Activate—Reclaim Your Mind** R (concentrate, fortune)

**Frequency** once per hour

**Trigger** You fail a saving throw against an effect that makes you [[Confused]], [[Fascinated]], or [[Stupefied]]

**Effect** The *headwrap of wisdom* clears your mind. You can reroll the saving throw and use the better result.

**Source:** `= this.source` (`= this.source-type`)
