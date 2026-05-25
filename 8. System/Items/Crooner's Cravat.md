---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "wornnecklace"
bulk: "—"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long, silky neckcloth has the ability to be tied into a convincing semblance of an elegant evening scarf, a worker's neck kerchief, an elaborate cravat, or any other neckwear. It also provides a boost to vocal performances, enhancing both projection and the emotive qualities of a performance. In its natural state, this item appears as a long, white silk scarf. A *crooner's cravat* grants a +1 item bonus to all Performance checks, but this increases to a +2 item bonus for Performance checks to sing.

**Activate—Adjust Cravat** `pf2:2` (illusion, manipulate, visual)

**Frequency** once per hour

**Effect** You make adjustments to the crooner's cravat, transforming it into any type of stylish chosen neckwear; as you do so, you cast a 1st-rank [[Illusory Disguise]] on yourself.

**Activate—Influential Croon** `pf2:2` (auditory, emotion, linguistic)

**Frequency** once per day

**Effect** You pour emotion into your vocal performance, projecting an empathetic bond that fascinates listeners. You cast enthrall (DC 30 [[Will]] save). When you first activate Influential Croon, you can also cast [[Subconscious Suggestion]] on one creature within 30 feet (DC 30 [[Will]] save).

**Source:** `= this.source` (`= this.source-type`)
