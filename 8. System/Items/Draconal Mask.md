---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This dragon-themed half-mask helps you to navigate through darkness and to notice things from afar—such as helping to find seats in a theater after a show begins, or to pick up details from a show even if you're seated in the back row! You gain a +3 item bonus to Perception checks and never take a penalty to Perception checks based on distance or weather. You gain darkvision, or greater darkvision if you have darkvision. When you invest in the mask you either increase your Wisdom score by 2 or increase it to 18, whichever would give you a higher score. If you are unholy, you become [[Blinded]] as long as you wear the mask.

**Activate—Dragons See the Truth** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You fail a saving throw against an illusion effect

**Effect** The mask attempts to counteract the triggering illusion with a counteract rank of 9 and a counteract modifier of +31. You then gain the effects of truesight for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
