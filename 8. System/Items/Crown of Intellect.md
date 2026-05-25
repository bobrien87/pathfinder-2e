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

A trio of brilliant gems have been set into this elegant golden crown. You gain a +3 item bonus to checks to Recall Knowledge, regardless of the skill. When you invest the cloak, you either increase your Intelligence modifier by 1 or increase it to +4, whichever would give you a higher value. This gives you additional trained skills and languages, as normal for increasing your Intelligence modifier. You must select skills and languages the first time you invest the crown, and whenever you invest the same *crown of intellect*, you get the same skills and languages you chose the first time.

**Activate—Search Your Mind** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** You gain the effects of [[Hypercognition]].

**Source:** `= this.source` (`= this.source-type`)
