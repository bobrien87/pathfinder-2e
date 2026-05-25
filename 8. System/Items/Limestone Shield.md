---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Earth]]", "[[Magical]]"]
price: "{'gp': 350}"
bulk: "4"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tower shield is a slab of limestone, shaved to a portable size and weight. The shield has Hardness 7 and 28 Hit Points.

**Activate—Limestone Wall** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You set the shield down as it expands up to 60 feet wide and 10 feet tall. Each square of the wall has AC 10, Hardness 7, and 28 Hit Points, and it's immune to critical hits and precision damage. If a section is destroyed, this effect ends, and your limestone shield is broken. You can Dismiss this activation, which otherwise lasts for 1 minute.

**Activate—Block Elements** R (concentrate)

**Frequency** once per day

**Trigger** You're targeted by an effect with the air, fire, or water trait

**Effect** The shield expands to block the triggering effect, granting you standard cover from that effect.

**Source:** `= this.source` (`= this.source-type`)
